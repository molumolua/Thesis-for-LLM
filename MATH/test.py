def solution():
    computers_initial = 9
    computers_per_day = 5
    num_days = 4  # 4 days between Monday and Thursday
    daily_increase_rate = computers_per_day / computers_initial  # Daily rate of increase relative to initial stock
    cumulative_increase = sum([computers_initial * (1 + daily_increase_rate) ** day for day in range(1, num_days + 1)])
    computers_total = computers_initial + cumulative_increase
    result = round(computers_total)  # Ensure the result is an integer value, as the total count of computers is discrete
    return result


print(solution())