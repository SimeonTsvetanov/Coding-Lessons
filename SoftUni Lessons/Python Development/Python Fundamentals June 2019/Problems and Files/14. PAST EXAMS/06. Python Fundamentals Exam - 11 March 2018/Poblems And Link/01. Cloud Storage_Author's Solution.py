import math

budget = float(input())
concurrent_clients = int(input())
gigabytes_to_store = int(input())
hosts_needed = int(input())
expected_uptime = float(input())

servers_needed = math.ceil(concurrent_clients / 50)
storage_units_needed = math.ceil(gigabytes_to_store / 0.5)

hourly_cost = servers_needed * 2 + storage_units_needed * 0.5

daily_cost = hourly_cost * 24
host_cost = hosts_needed * 10

monthly_cost = daily_cost * 30
total_cost = (monthly_cost + host_cost) * expected_uptime / 100

if total_cost <= budget:
	print(f'Clouds Ahoy! Monthly cost: ${total_cost:.2f} (${budget - total_cost:.2f} leftover)')
else:
	print(f'Stay Grounded! Monthly cost: ${total_cost:.2f} (Need ${total_cost - budget:.2f} more)')
