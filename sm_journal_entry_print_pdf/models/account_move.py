# -*- coding: utf-8 -*-

from odoo import _, models
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = "account.move"

    def _get_report_journal_entry_filename(self):
        if any(move.is_invoice(include_receipts=True) for move in self):
            raise UserError(_("Only journal entries can be printed with this report."))
        return _("Journal Entry - %s") % ", ".join(self.mapped("name"))

    def _get_journal_entry_analytic_lines(self, line):
        if not line.analytic_distribution:
            return []

        analytic_ids = []
        for key in line.analytic_distribution:
            analytic_ids.extend(int(analytic_id) for analytic_id in key.split(",") if analytic_id)

        analytic_names = {
            account.id: account.display_name
            for account in self.env["account.analytic.account"].browse(analytic_ids).exists()
        }
        values = []
        for key, percentage in line.analytic_distribution.items():
            names = [
                analytic_names.get(int(analytic_id), analytic_id)
                for analytic_id in key.split(",")
                if analytic_id
            ]
            values.append("%s: %s%%" % (", ".join(names), percentage))
        return values

