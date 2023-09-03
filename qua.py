def detect_vibration(price, m, n):
    vibrations = []
    start_idx = None
    end_idx = None
    
    for i in range(1, len(price)):
        price_change = abs(price[i] - price[i - 1])
        
        if price_change > m:
            # 涨跌幅大于m，可能横盘区间的结束
            if start_idx is not None and end_idx is None:
                end_idx = i - 1
                if end_idx - start_idx >= 10:  # 横盘区间持续时间超过10分钟
                    vibrations.append((start_idx, end_idx))
            start_idx = None
            end_idx = None
        elif start_idx is not None and price_change <= n:
            # 在横盘区间内，涨跌幅小于等于n
            end_idx = i
        elif start_idx is None and price_change <= n:
            # 横盘区间的开始
            start_idx = i - 1

    # 检查最后一个可能的横盘区间
    if start_idx is not None and end_idx is None:
        end_idx = len(price) - 1
        if end_idx - start_idx >= 10:
            vibrations.append((start_idx, end_idx))

    return vibrations

# 示例用法
price_sequence = [100, 102, 103, 105, 105, 105, 104, 104, 103, 103, 103, 102, 102, 102, 101, 100]
m_threshold = 2
n_threshold = 1
vibration_intervals = detect_vibration(price_sequence, m_threshold, n_threshold)
print(vibration_intervals)


def backtest(price, signal, buy_threshold, sell_threshold):
    position = 0  # 当前持仓数量
    pnl = 0.0  # 累计收益
    max_pnl = 0.0  # 最大累计收益
    buy_price = 0.0  # 买入价格

    for i in range(len(price)):
        sig_value = signal[i]

        if position < 3 and sig_value > buy_threshold:
            # 信号大于买入阈值且持仓未达到上限，买入1手
            position += 1
            buy_price = price[i]

        elif position > 0 and sig_value < sell_threshold:
            # 信号小于卖出阈值且持仓大于0，卖出1手
            position -= 1
            pnl += (price[i] - buy_price)

        max_pnl = max(max_pnl, pnl)

    return max_pnl

# 示例用法
import pandas as pd

# 从data.csv读取数据，假设该CSV文件包含price和sig_1到sig_8等字段
data = pd.read_csv("data.csv")
price_sequence = data["price"].tolist()
signal_1 = data["sig_1"].tolist()
signal_2 = data["sig_2"].tolist()
# 依此类推，处理其他信号

buy_threshold = 99  # 买入阈值，可以根据信号分位点来设置
sell_threshold = 1  # 卖出阈值，可以根据信号分位点来设置

pnl_1 = backtest(price_sequence, signal_1, buy_threshold, sell_threshold)
pnl_2 = backtest(price_sequence, signal_2, buy_threshold, sell_threshold)
# 依此类推，计算其他信号的累计收益

print("PnL for signal 1:", pnl_1)
print("PnL for signal 2:", pnl_2)
# 依此类推，输出其他信号的累计收益
