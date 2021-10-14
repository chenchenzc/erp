// Copyright (c) 2016, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Global cost accounting"] = {
	"filters": [
		{
			"fieldname": "from_date",
			"label": __("From Date"),
			"fieldtype": "Date"
		},
		{
			"fieldname": "to_date",
			"label": __("To Date"),
			"fieldtype": "Date"
		},
		{
			"fieldname": "project_type",
			"label": __("Project Type"),
			"fieldtype": "Link",
			"options": "Project Type"
		},
		{
			"fieldname": "customer",
			"label": __("Customer"),
			"fieldtype": "Link",
			"options": "Customer"
		}
	]
};
