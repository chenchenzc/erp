frappe.provide('frappe.dashboards.chart_sources');

frappe.dashboards.chart_sources["Task prompt statistics"] = {
	method: "erpnext.projects.dashboard_chart_source.task_prompt_statistics.task_prompt_statistics.get",
	filters: [
		{
			fieldname: "status",
			label: __("Status"),
			fieldtype: "Select",
			options: "Open\nWorking\nPending Review\nOverdue\nTemplate\nCompleted\nCancelled"	
		}
	],
};
