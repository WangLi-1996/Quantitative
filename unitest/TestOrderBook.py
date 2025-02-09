#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @StartTime: 2025/2/9 22:42
# @EndTime  :
# @Author   : EvlAng
# @Site     : 
# @Project  : Quantitative
# @File     : TestOrderBook.py
# @Software : PyCharm
# @Purpose  :
# @Link     :
# @Question :
import pandas as pd

from OrderBook import OrderBook


class OrderBook_test:
    def testOrderBook(self):
        """
        测试用例
        :return:
        """
        # 初始化订单簿
        ob = OrderBook()

        # 添加限价单
        ob.add_order(True, 100.0, 500)  # 买方 100元 500股
        ob.add_order(True, 99.5, 300)  # 买方 99.5元 300股
        ob.add_order(False, 101.0, 800)  # 卖方 101元 800股
        ob.add_order(False, 101.5, 400)  # 卖方 101.5元 400股

        print("最优报价:", ob.get_bbo())  # 输出：(100.0, 101.0)
        print("市场深度:", ob.get_depth(2))

        # 模拟市价卖出订单（卖出600股）
        avg_price = ob.match_market_order(False, 600)
        print(f"市价卖出均价: {avg_price:.2f}")  # 计算：(100*500 + 99.5*100)/600 = 99.92

    def testOrderBook_2(self):
        """
        滑点模拟
        :return:
        """
        def simulate_slippage(ob: OrderBook, order_qty: int, is_buy: bool):
            """模拟不同订单量下的滑点"""
            initial_bbo = ob.get_bbo()
            expected_price = initial_bbo[0] if is_buy else initial_bbo[1]
            executed_price = ob.match_market_order(is_buy, order_qty)

            slippage = (executed_price - expected_price) / expected_price * 10000  # 单位：bps
            return slippage

        # 测试不同订单量的滑点
        for qty in [200, 600, 1000]:
            ob_test = OrderBook()
            ob_test.add_order(False, 101.0, 500)
            ob_test.add_order(False, 101.5, 500)
            slippage = simulate_slippage(ob_test, qty, True)
            print(f"订单量{qty}的滑点: {slippage:.1f} bps")

    def testOrderBook_3(self):
        """
        订单流分析
        :return:
        """
        # 生成模拟订单流数据
        orders = pd.DataFrame([
            {'time': '09:30:01', 'price': 100.0, 'qty': 200, 'direction': 'buy'},
            {'time': '09:30:03', 'price': 101.0, 'qty': 300, 'direction': 'sell'},
            {'time': '09:30:05', 'price': 100.5, 'qty': 500, 'direction': 'buy'},
            {'time': '09:30:07', 'price': 101.0, 'qty': 400, 'direction': 'sell'},
        ])

        # 分析买卖压力
        buy_pressure = orders[orders['direction'] == 'buy']['qty'].sum()
        sell_pressure = orders[orders['direction'] == 'sell']['qty'].sum()
        print(f"买压/卖压比率: {buy_pressure / sell_pressure:.2%}")

        # 订单流可视化
        import plotly.express as px
        fig = px.scatter(orders, x='time', y='price', size='qty', color='direction',
                         title="订单流分布图")
        fig.show()


if __name__ == '__main__':
    ob_test = OrderBook_test()
    ob_test.testOrderBook()