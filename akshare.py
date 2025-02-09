#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @StartTime: 2025/2/4 17:11
# @EndTime  :
# @Author   : EvlAng
# @Site     : 
# @Project  : Quantitative
# @File     : akshare.py
# @Software : PyCharm
# @Purpose  :
# @Link     :
# @Question :

import akshare as ak

# 日线/周线/月线
# aks.stock_zh_a_hist(symbol="000001",
#                     start_date="20200101",
#                     end_date="20241201",
#                     period="daily",  # daily/weekly/monthly
#                     adjust="qfq")  # qfq-前复权/hfq-后复权/默认不复权
# # 日线
# aks.stock_zh_a_daily(symbol="sz000001",
#                      start_date="20200101",
#                      end_date="20241201",
#                      adjust="qfq")
# # 分钟线
# aks.stock_zh_a_minute(symbol="sz000001",
#                       period="1",  # 1-1分钟/5-5分钟/15-15分钟/30-30分钟/60-1小时
#                       adjust="qfq")

get_roll_yield_bar_df = ak.get_roll_yield_bar(type_method="date ", var="RB", start_day="20180618", end_day="20180718")
print(get_roll_yield_bar_df)
