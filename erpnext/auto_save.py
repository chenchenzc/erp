from __future__ import unicode_literals

import frappe

@frappe.whitelist()
def auto_save(doc, method):
    doc.submit()