from __future__ import unicode_literals

import frappe
from frappe import _
from frappe.utils.dashboard import cache_source
import time

@frappe.whitelist()
@cache_source
def get(chart_name = None, chart = None, no_cache = None, filters = None, from_date = None,
    to_date = None, timespan = None, time_interval = None, heatmap_year = None):
    # 最后返回值中的当天任务总数
    totalNumber=[]
    # 最后返回值中的当天截止任务数
    ddlNumber=[]
    timeStatus=''
    labels = ["低","中","高","紧急"]
    degree=["Low","Medium","High","Urgent"]

    filters = frappe.parse_json(filters)
    status = filters.get('status')
    # 找到所有状态为open的task,组成 list 
    listall=frappe.get_list('Task')
    listopen=frappe.get_list('Task',filters={"status":status},fields=["name"])
    listcurrentday=[[],[],[],[]]
    listcurrentdue=[[],[],[],[]]
    Mlist=[listcurrentday,listcurrentdue]

    # 需要对日期筛选
    for item in listopen:
        doc = frappe.get_doc('Task',item.name)
        # 存在预期时间就需要比较时间差，筛选1.当天比预计早2.当天即预计结束
        if doc.exp_end_date:
            timeStatus=TimeStatus(frappe.utils.nowdate(),doc.exp_end_date)
            # 根据难度添加进不同的list的位置
            if(timeStatus=="inExpected" or timeStatus=="atExpected"):
                for x in range(0,4):
                    if doc.priority == degree[x]:
                        listcurrentday[x].append(item)
            if(timeStatus=="atExpected"):
                for x in range(0,4):
                    if doc.priority == degree[x]:
                        listcurrentdue[x].append(item)

    for i in range(0,4):
        totalNumber.append(len(listcurrentday[i]))
        ddlNumber.append(len(listcurrentdue[i]))
        
    return {
        "labels": labels,
        "datasets": [
            {
                "name":"当日截止",
                "values":ddlNumber
            },
            {
            "name":"当日总和",
			"values": totalNumber
            }
        ]    
    }
def TimeStatus(now,expend) :
    # expend/now是“yy-mm-dd”格式
    # 转换成时间戳1.获取时间2.转换成时间数组time.strptime()3.转换成时间戳time.mktime()
    exp_end_dateArray=time.strptime(str(expend),"%Y-%m-%d")
    nowdateArray=time.strptime(str(now),"%Y-%m-%d")
    exp_end_dateStamp=time.mktime(exp_end_dateArray)
    nowdateStamp=time.mktime(nowdateArray)
    timeDelta=exp_end_dateStamp-nowdateStamp
    if (timeDelta<0):
        return "outExpected"

    if (timeDelta==0):
        return "atExpected" 
    
    if (timeDelta>0):
        return "inExpected" 