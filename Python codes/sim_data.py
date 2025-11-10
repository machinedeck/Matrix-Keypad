import numpy as np

dat = np.loadtxt("Matrix-Keyboard.txt", skiprows = 1)
x = dat[:, 0]
y = dat[:, 17]

num_raw = y[y>0.5][1:]
start = 0
vals = []
for i in range(16):
    vals.append(num_raw[start])
    start += 3
vals1 = np.array(vals)
index = np.argsort(vals1)
# vals1.resize((4, 4))
# index.resize((4, 4))
# vals = np.sort(vals1) * 1000 # in mV
vals = vals1 * 1000 # in mV

# Arduino digitization
bits = 10
step = 5000 / (2**10 - 1) # in mV

# factors = vals / step

low_lim = np.int64(vals - step)
up_lim = np.int64(vals + step)