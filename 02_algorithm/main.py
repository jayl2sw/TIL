p = { hex(i).replace('0x', '').upper() : bin(i).replace('0b','').zfill(4) for i in range(16) }
print(p)