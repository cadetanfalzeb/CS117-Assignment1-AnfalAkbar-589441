A = int(input("Enter A: "))
B = int(input("Enter B: "))

if (A != 0 and A != 1) or (B != 0 and B != 1):
    print("Bits must be 0 or 1")
else:
    and_out = 1 if (A == 1 and B == 1) else 0
    or_out = 1 if (A == 1 or B == 1) else 0
    xor_out = 1 if (A != B) else 0

    print(f"AND = {and_out}")
    print(f"OR = {or_out}")
    print(f"XOR = {xor_out}")
