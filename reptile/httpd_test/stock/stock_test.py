'''
*************************************: 
FilePath     : \stock\stock_test.py
version      : 
Author       : dof
Date         : 2026-02-13 10:51:27
LastEditors  : dof
LastEditTime : 2026-02-13 14:32:49
Descripttion :  
compile      :  
**************************************: 
'''
# src/main.py
import requests
import pandas as pd
import json
from datetime import datetime, timedelta
import time
import warnings
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
warnings.filterwarnings('ignore')

class StockAnalyzer:
    def __init__(self):
        self.session = requests.Session()
        # 设置请求头，模拟浏览器访问
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
        })
        
    def get_network_communication_stocks(self):
        """
        获取网络通信相关股票列表
        这里使用一个预定义的列表，实际应用中可以使用更复杂的逻辑来获取实时数据
        """
        # A股网络通信相关股票代码列表（部分示例）
        stocks = {
            '000063': '中兴通讯',
            '002230': '科大讯飞',
            '002475': '立讯精密',
            '300033': '同花顺',
            '300433': '蓝思科技',
            '600030': '中信证券',
            '600036': '招商银行',
            '600519': '贵州茅台',
            '601318': '中国平安',
            '601888': '中国中免',
        }
        return stocks
    
    def get_stock_data(self, stock_code):
        """
        获取单个股票的基本信息和历史数据
        """
        try:
            # 使用tushare接口获取数据（需要安装tushare库）
            # 这里使用模拟数据，实际应用中需要使用真实API
            print(f"正在获取 {stock_code} 的数据...")
            
            # 模拟获取股票数据
            stock_info = {
                'code': stock_code,
                'name': self.get_stock_name(stock_code),
                'current_price': round(20 + (int(stock_code) % 100) * 0.5, 2),
                'change_percent': round((int(stock_code) % 20) - 11, 2),
                'volume': int(stock_code) * 10000,
                'amount': int(stock_code) * 1000000,
                'market_cap': int(stock_code) * 100000000,
                'pe_ratio': round(10 + (int(stock_code) % 50), 2)
            }
            
            # 模拟历史数据
            history_data = self.generate_mock_history_data(stock_code)
            
            return {
                'stock_info': stock_info,
                'history_data': history_data
            }
            
        except Exception as e:
            print(f"获取 {stock_code} 数据时出错: {str(e)}")
            return None
    
    def get_stock_name(self, stock_code):
        """
        获取股票名称（模拟）
        """
        stocks = self.get_network_communication_stocks()
        return stocks.get(stock_code, f"未知股票_{stock_code}")
    
    def generate_mock_history_data(self, stock_code):
        """
        生成模拟的历史数据
        """
        # 生成最近30天的数据
        data = []
        base_price = 20 + (int(stock_code) % 100) * 0.5
        current_date = datetime.now()
        
        for i in range(30):
            date = (current_date - timedelta(days=i)).strftime('%Y-%m-%d')
            # 模拟价格波动
            price_change = (int(stock_code) % 20) - 10
            open_price = base_price + (i * 0.1)
            close_price = open_price + (price_change * 0.1)
            high_price = max(open_price, close_price) + (i * 0.05)
            low_price = min(open_price, close_price) - (i * 0.05)
            
            data.append({
                'date': date,
                'open': round(open_price, 2),
                'high': round(high_price, 2),
                'low': round(low_price, 2),
                'close': round(close_price, 2),
                'volume': int(stock_code) * 10000 + i * 1000
            })
            base_price = close_price
        
        return data
    
    def get_stock_news(self, stock_code):
        """
        获取股票相关新闻资讯（模拟）
        """
        news_list = [
            {
                'title': f"{self.get_stock_name(stock_code)}发布最新财报",
                'summary': "公司发布了2023年第三季度财报，营收同比增长15%，净利润增长20%。",
                'time': "2023-10-15 10:30:00",
                'source': "财经网"
            },
            {
                'title': f"{self.get_stock_name(stock_code)}获得重要订单",
                'summary': "公司成功中标某大型通信项目，合同金额达50亿元。",
                'time': "2023-10-10 14:20:00",
                'source': "证券时报"
            },
            {
                'title': f"{self.get_stock_name(stock_code)}与国际厂商合作",
                'summary': "公司宣布与某国际知名通信设备厂商建立战略合作关系。",
                'time': "2023-10-05 09:15:00",
                'source': "新华网"
            }
        ]
        
        return news_list
    
    def analyze_stocks(self):
        """
        分析所有网络通信相关股票
        """
        print("开始分析网络通信相关股票...")
        print("=" * 60)
        
        stocks = self.get_network_communication_stocks()
        results = []
        
        for code, name in stocks.items():
            print(f"\n正在分析 {code} - {name}")
            
            # 获取股票数据
            stock_data = self.get_stock_data(code)
            if stock_data:
                results.append(stock_data)
                
                # 打印基本信息
                info = stock_data['stock_info']
                print(f"  股票名称: {info['name']}")
                print(f"  股票代码: {info['code']}")
                print(f"  当前价格: {info['current_price']}")
                print(f"  涨跌幅: {info['change_percent']}%")
                print(f"  成交量: {info['volume']}")
                print(f"  市值: {info['market_cap']:,}")
                print(f"  市盈率: {info['pe_ratio']}")
                
                # 打印最近5天历史数据
                print("  最近5天历史数据:")
                history = stock_data['history_data'][:5]
                for day in history:
                    print(f"    {day['date']}: 开盘{day['open']}, 收盘{day['close']}")
                
                # 获取相关新闻
                print("  最新资讯:")
                news = self.get_stock_news(code)
                for item in news:
                    print(f"    {item['time']} - {item['title']}")
                    print(f"      摘要: {item['summary']}")
                    print(f"      来源: {item['source']}")
                
                # 绘制股票价格图表
                self.plot_stock_chart(stock_data, code)
                
                print("-" * 40)
            
            # 添加延迟避免请求过于频繁
            time.sleep(0.5)
        
        return results
    
    def plot_stock_chart(self, stock_data, stock_code):
        """
        绘制股票价格图表
        """
        try:
            # 准备数据
            history = stock_data['history_data']
            dates = [datetime.strptime(day['date'], '%Y-%m-%d') for day in history]
            closes = [day['close'] for day in history]
            opens = [day['open'] for day in history]
            highs = [day['high'] for day in history]
            lows = [day['low'] for day in history]
            
            # 创建图表
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})
            
            # 绘制价格走势图
            ax1.plot(dates, closes, label='收盘价', linewidth=2, color='blue')
            ax1.plot(dates, opens, label='开盘价', linewidth=1, color='green')
            ax1.plot(dates, highs, label='最高价', linewidth=1, color='red')
            ax1.plot(dates, lows, label='最低价', linewidth=1, color='orange')
            
            # 设置价格图的格式
            ax1.set_title(f'{stock_data["stock_info"]["name"]} ({stock_code}) 股价走势', fontsize=14, fontweight='bold')
            ax1.set_ylabel('价格 (元)', fontsize=12)
            ax1.legend(loc='upper left')
            ax1.grid(True, alpha=0.3)
            
            # 格式化x轴日期
            ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
            ax1.xaxis.set_major_locator(mdates.DayLocator(interval=5))
            plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45)
            
            # 绘制成交量
            volumes = [day['volume'] for day in history]
            ax2.bar(dates, volumes, alpha=0.7, color='gray')
            ax2.set_title('成交量', fontsize=12)
            ax2.set_ylabel('成交量', fontsize=12)
            ax2.set_xlabel('日期', fontsize=12)
            
            # 格式化成交量图的x轴
            ax2.xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))
            ax2.xaxis.set_major_locator(mdates.DayLocator(interval=5))
            plt.setp(ax2.xaxis.get_majorticklabels(), rotation=45)
            
            # 调整布局并显示图表
            plt.tight_layout()
            plt.show()
            
        except Exception as e:
            print(f"绘制图表时出错: {str(e)}")
    
    def save_results(self, results, filename='stock_analysis_results.json'):
        """
        保存分析结果到文件
        """
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(results, f, ensure_ascii=False, indent=2)
            print(f"\n分析结果已保存到 {filename}")
        except Exception as e:
            print(f"保存文件时出错: {str(e)}")

def main():
    """
    主函数
    """
    print("A股网络通信公司股票走势和资讯分析程序")
    print("=" * 50)
    
    # 创建分析器实例
    analyzer = StockAnalyzer()
    
    try:
        # 分析股票
        results = analyzer.analyze_stocks()
        
        # 保存结果
        analyzer.save_results(results)
        
        print("\n分析完成！")
        print("=" * 50)
        
    except Exception as e:
        print(f"程序执行出错: {str(e)}")

if __name__ == "__main__":
    main()