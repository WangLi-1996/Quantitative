#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @StartTime: 2025/2/9 22:37
# @EndTime  :
# @Author   : EvlAng
# @Site     : 
# @Project  : Quantitative
# @File     : OrderBook.py
# @Software : PyCharm
# @Purpose  :
# @Link     :
# @Question : 基础订单簿实现

import pandas as pd
from sortedcontainers import SortedDict


class OrderBook:
    def __init__(self):
        # 使用SortedDict自动按价格排序（买方向降序，卖方向升序）
        self.bids = SortedDict(lambda x: -x)  # 买方队列 {价格: 数量}
        self.asks = SortedDict()  # 卖方队列 {价格: 数量}

    def add_order(self, is_bid: bool, price: float, qty: int):
        """添加限价单"""
        book = self.bids if is_bid else self.asks
        book[price] = book.get(price, 0) + qty

    def match_market_order(self, is_bid: bool, qty: int) -> float:
        """市价单匹配逻辑：返回成交量与成交均价"""
        total_qty = 0
        total_value = 0.0
        book = self.asks if is_bid else self.bids  # 买方市价单匹配卖盘

        for price in book.keys():
            available = book[price]
            if total_qty + available >= qty:
                filled = qty - total_qty
                total_value += filled * price
                total_qty = qty
                book[price] -= filled
                if book[price] == 0:
                    del book[price]
                break
            else:
                total_value += available * price
                total_qty += available
                del book[price]

        return total_value / total_qty if total_qty > 0 else 0.0

    def get_bbo(self) -> tuple:
        """获取最优买卖报价"""
        best_bid = self.bids.peekitem(0)[0] if self.bids else 0
        best_ask = self.asks.peekitem(0)[0] if self.asks else 0
        return (best_bid, best_ask)

    def get_depth(self, levels=5) -> dict:
        """获取市场深度"""
        return {
            'bids': {k: self.bids[k] for k in self.bids.keys()[:levels]},
            'asks': {k: self.asks[k] for k in self.asks.keys()[:levels]}
        }