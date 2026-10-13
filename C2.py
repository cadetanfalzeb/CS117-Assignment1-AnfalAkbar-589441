def parallel_resistance(resistors):
    inv_sum = 0.0
    for r in resistors:
        inv_sum += 1.0 / r
    return 1.0 / inv_sum

print(f"parallel_resistance ([10, 10]) -> {parallel_resistance([10, 10]):.1f}")
print(f"parallel_resistance([100, 200, 300]) -> {parallel_resistance([100, 200, 300]):.2f}")
