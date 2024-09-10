# 请补充你的代码
# 提示用户输入股票的买入价格（每股）
buy_price = float(input("请输入股票的买入价格（每股）："))

# 提示用户输入股票的卖出价格（每股）
sell_price = float(input("请输入股票的卖出价格（每股）："))

# 提示用户输入持有的股票数量
quantity = int(input("请输入持有的股票数量："))

# 计算总收益
total_profit = (sell_price - buy_price) * quantity

# 按格式输出总收益，保留两位小数
print(f"总收益为：{total_profit:.2f} 元")
