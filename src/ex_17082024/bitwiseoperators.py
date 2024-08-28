# Bitwise operators
# ----And operator
a = 5  # 101---binary
b = 4  # 100 ---- binary
print(a & b)  # 100------------ and operator

# -------Or Operator
a = 5  # 101---binary
b = 4  # 100 ---- binary
print(a | b)  # 101------------ Or operator

# ----Not Operator
a = 4  # 100 ---binary
print(~a)  # Invert all bits and add one due to 2's complement >>011 >>100-----Not Operator

# a=-11
# print(bin(a))

# ------------Xor Operator
a = 10  # 1010
b = 4  # 0100
print(a ^ b)  # ---------a xor b>> 1110==8+4+2+0= 14

# ----------Right Shift operator
a = 10  # 1010
print(a >> 1)  # ---     0101

# ----------Left Shift operator
a = 10  # 1010
print(a << 1)  # ---     10100
