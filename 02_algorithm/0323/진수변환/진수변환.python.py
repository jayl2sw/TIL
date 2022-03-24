num = 10

# 2진법 변환
binary = bin(num)
print(binary[2:])
print(binary.replace('0b', ''))

# 8진법 변환
octal = oct(num)
print(octal.replace('0o', ''))

# 16진법 변환
decimaltohex = hex(num)
print(decimaltohex.replace('0x', ''))

dec = int(binary, base=2)
print(dec)

dec = int(octal, base=8)
print(dec)

dec = int(decimaltohex, base=16)
print(dec)


