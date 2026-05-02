# -*- coding: utf-8 -*-
{
    "name": "Print Journal Entry PDF",
    "summary": "Print clean PDF reports for journal entries",
    "description": """
Print Journal Entry PDF
=======================

Add a dedicated PDF report for journal entries with journal information, reference, partner, analytic distribution, taxes, debit, credit, and approval signature blocks.
    """,
    "version": "19.0.1.0.0",
    "author": "Steven Marp",
    "website": "https://apps.odoo.com/apps/browse?repo_maintainer_id=512936",
    "category": "Accounting",
    "license": "OPL-1",
    "depends": ["account"],
    "data": [
        "report/journal_entry_report.xml",
    ],
    "images": ["static/description/banner.jpg"],
    "installable": True,
    "application": False,
    "auto_install": False,
    "price": 9.98,
    "currency": "USD",
}
