# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# License: GNU General Public License v3. See license.txt
from __future__ import unicode_literals

import frappe
from frappe import _


def execute(filters=None):
	columns = get_columns()
	proj_details = get_project_details(filters)

	data = []
	totalmaoli= 0
	for project in proj_details:
		maoli=(project.total_billed_amount)-(project.total_purchase_cost)
		totalmaoli += maoli
		data.append([project.name, project.project_name,
			project.project_type,project.customer,
			project.total_purchase_cost, 
			project.total_billed_amount,
			maoli])
		
	data.append(['总计','','','','','',totalmaoli]) 
	return columns, data

def get_columns():
	return [_("项目编号") + ":Link/Project:120", _("项目名称") + "::150",
		_("项目类型") + "::120", _("客户") + ":Link/Customer:120",
		_("总采购成本") + ":Currency:170",
		_("总账单金额") + ":Currency:170", 
		_("毛利")+":Currency:150"]

def get_project_details(filters):
	conditions = get_conditions(filters)
	print(conditions)
	projectList = frappe.get_all("Project",
			  filters = conditions,
			  fields=["name","project_name",
			  		"project_type","customer",
			  		"total_purchase_amount","total_purchase_cost",
					"total_sales_amount","total_billed_amount"],
			  order_by="creation"
		)
	return projectList

def get_conditions(filters):
	conditions = frappe._dict()
	keys = ["project_type","customer"]
	for key in keys:
		if filters.get(key):
			conditions[key] = filters.get(key)
	if filters.get("from_date"):
		conditions.expected_start_date = [">=", filters.get("from_date")]
	if filters.get("to_date"):
		conditions.expected_end_date = ["<=", filters.get("to_date")]
	return conditions