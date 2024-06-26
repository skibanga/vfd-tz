# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "vfd_tz"
app_title = "vfd-tz"
app_publisher = "Aakvatech"
app_description = "VFD TZ"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@aakvatech.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/vfd_tz/css/vfd_tz.css"
# app_include_js = "/assets/vfd_tz/js/vfd_tz.js"

# include js, css files in header of web template
# web_include_css = "/assets/vfd_tz/css/vfd_tz.css"
# web_include_js = "/assets/vfd_tz/js/vfd_tz.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {
    "Sales Invoice": "vfd_tz/api/sales_invoice.js",
    "Customer": "vfd_tz/api/customer.js",
}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "vfd_tz.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "vfd_tz.install.before_install"
# after_install = "vfd_tz.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "vfd_tz.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Sales Invoice": {
        "on_submit": "vfd_tz.vfd_tz.api.sales_invoice.auto_enqueue",
        "before_cancel": "vfd_tz.vfd_tz.api.sales_invoice.validate_cancel",
        "before_submit": "vfd_tz.vfd_tz.api.sales_invoice.vfd_validation",
    },
    "Customer": {
        "validate": "vfd_tz.api.utils.clean_and_update_tax_id_info",
    },
}
# Scheduled Tasks
# ---------------

scheduler_events = {
    # "all": [
    # 	"vfd_tz.tasks.all"
    # ],
    # "daily": [
    # 	"vfd_tz.tasks.daily"
    # ],
    "cron": {
        "0 2 * * *": [
            "vfd_tz.vfd_tz.doctype.vfd_z_report.vfd_z_report.make_vfd_z_report",
            "vfd_tz.api.utils.check_vfd_status",
        ],
        "0 * * * *": [
            "vfd_tz.vfd_tz.doctype.vfd_z_report.vfd_z_report.send_multi_vfd_z_reports",
        ],
        "0,15,30,45 * * * *": [
            "vfd_tz.vfd_tz.api.sales_invoice.posting_all_vfd_invoices",
            "vfd_tz.vfd_tz.doctype.vfd_tax_invoice.vfd_tax_invoice.posting_all_vfd_invoices",
        ],
        "*/5 0-4 * * *": [
            "vfd_tz.vfd_tz.api.sales_invoice.posting_all_vfd_invoices_off_peak",
            "vfd_tz.vfd_tz.doctype.vfd_tax_invoice.vfd_tax_invoice.posting_all_vfd_invoices_off_peak",
        ],
    },
    # "weekly": [
    # 	"vfd_tz.tasks.weekly"
    # ]
    # "monthly": [
    # 	"vfd_tz.tasks.monthly"
    # ]
}

# Testing
# -------

# before_tests = "vfd_tz.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "vfd_tz.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "vfd_tz.task.get_dashboard_data"
# }

fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                (
                    "Customer-vfd_custid",
                    "Customer-vfd_custidtype",
                    "Sales Invoice-column_break_vfd",
                    "Sales Invoice-vfd_z_number",
                    "Item Tax Template-vfd_taxcode",
                    "Mode of Payment-vfd_pmttype",
                    "POS Profile-is_auto_generate_vfd",
                    "POS Profile-is_not_vfd_invoice",
                    "Sales Invoice-column_break_vfd",
                    "Sales Invoice-is_auto_generate_vfd",
                    "Sales Invoice-is_not_vfd_invoice",
                    "Sales Invoice-vfd_cust_id_type",
                    "Sales Invoice-vfd_cust_id",
                    "Sales Invoice-vfd_date",
                    "Sales Invoice-vfd_dc",
                    "Sales Invoice-vfd_details",
                    "Sales Invoice-vfd_gc",
                    "Sales Invoice-vfd_posting_info",
                    "Sales Invoice-vfd_rctnum",
                    "Sales Invoice-vfd_rctvnum",
                    "Sales Invoice-vfd_status",
                    "Sales Invoice-vfd_time",
                    "Sales Invoice-vfd_verification_url",
                    "Sales Taxes and Charges Template-vfd_vatrate",
                    "Sales Invoice-vfd_z_report",
                ),
            ]
        ],
    },
    {"doctype": "Property Setter", "filters": [["name", "in", ()]]},
]
