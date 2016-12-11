# ASSO = 4
# 32KB
# [4, 16, 32, 64]
# [0.700800, 0.700400, 0.700400, 0.700100]

# 256KB
# [4, 16, 32, 64]
# [0.742300, 0.741900, 0.741800, 0.741600]

# 4MB
# [4, 16, 32, 64]
# [0.972100, 0.971700, 0.971600, 0.971400]



# BLOCK = 16

# 32KB
# [4, 8, 16, 32]
# [0.700400, 0.680600, 0.661400, 0.645800]
# 256KB
# [4, 8, 16, 32]
# [0.741900, 0.713300, 0.700900, 0.649500]

# 4MB
# [4, 8, 16, 32]
# [0.971700, 0.870800, 0.736600, 0.739300]

import matplotlib.pyplot as plt

bx = [4, 8, 16, 32]
by = [0.700400, 0.680600, 0.661400, 0.645800]

gx = [4, 8, 16, 32]
gy = [0.741900, 0.713300, 0.700900, 0.649500]

rx = [4, 8, 16, 32]
ry = [0.971700, 0.870800, 0.736600, 0.739300]

plt.plot(bx, by,label="Cache size = 32KB",color="blue")
plt.plot(gx, gy,label="Cache size = 256KB", color="green")
plt.plot(rx, ry,label="Cache size = 4MB",color="red")

plt.xlabel("Associativity")
plt.ylabel("Miss Rate")
plt.title("Block size = 16")
plt.ylim(0.5,1.0)
plt.legend()
plt.show()
