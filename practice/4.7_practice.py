# This is my ninth Python programming practice file.
# Author: Alexey Konovalov
# Date: 05.09.2026


ping = int(input())
if ping >= 0:
    ping_report = "low to average" if ping < 150 else "too high"
    print(f"Ping is {ping_report}")
else: 
    print("Invalid ping value.")

