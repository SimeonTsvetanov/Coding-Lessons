import math

monthly_budget = float(input())
number_concurrent_clients = int(input())
gigabytes_data = int(input())
number_hosts = int(input())
expected_uptime_percent = float(input())

servers_needed = math.ceil(number_concurrent_clients / 50)
storage_needed = gigabytes_data / 0.5

servers_storage_cost = (((2 * servers_needed) + (0.5 * storage_needed)) * 24) * 30
hosts_cost = number_hosts * 10

total = (servers_storage_cost + hosts_cost) * (expected_uptime_percent * 0.01)


if monthly_budget >= total:
    print(f"Clouds Ahoy! Monthly cost: ${total:.2f} (${(monthly_budget - total):.2f} leftover)")
else:
    print(f"Stay Grounded! Monthly cost: ${total:.2f} (Need ${(total - monthly_budget):.2f} more)")
