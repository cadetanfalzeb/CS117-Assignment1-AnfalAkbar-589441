count_1_percent = 0
count_5_percent = 0
count_rejected = 0

while True:
    val = float(input("Enter measured resistance value (0 to stop): "))
    if val == 0:
        break
    
    if 99.0 <= val <= 101.0:
        count_1_percent += 1
    elif 95.0 <= val <= 105.0:
        count_5_percent += 1
    else:
        count_rejected += 1

print(f"1% tolerance count: {count_1_percent}")
print(f"5% tolerance count: {count_5_percent}")
print(f"Reject count: {count_rejected}")
