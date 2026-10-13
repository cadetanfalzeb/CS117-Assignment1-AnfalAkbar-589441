def ohms_current(v, r):
    return v / r

def power_dissipated(i, r):
    return (i ** 2) * r

v_val = 12
r_val = 6
current_result = ohms_current(v_val, r_val)
power_result = power_dissipated(current_result, r_val)

print(f"Current = {current_result:.1f} A")
print(f"Power = {power_result:.1f} W")
