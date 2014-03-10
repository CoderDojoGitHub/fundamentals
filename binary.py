num = 1          # Backing binary is 00000001
print num

# Shift num 1 bit to the left using <<
num = num << 1   # Backing binary is now 00000010
print num

# Keep shifting...
num = num << 1   # Backing binary is now 00000100
print num

num = num << 1   # Backing binary is now 00001000
print num

num = num << 1   # Backing binary is now 00010000
print num

num = num << 1   # Backing binary is now 00100000
print num

num = num << 1   # Backing binary is now 01000000
print num

num = num << 1   # Backing binary is now 10000000
print num
