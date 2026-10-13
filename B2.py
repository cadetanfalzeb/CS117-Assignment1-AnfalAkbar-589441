num_resistors = int(input("How many resistors? "))
total_resistance = 0.0

for i in range(1, num_resistors + 1):
    r_val = float(input(f"Enter R{i}: "))
    total_resistance += r_val

print(f"Total resistance = {total_resistance} ohm")
