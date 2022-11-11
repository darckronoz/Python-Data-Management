import numpy as np

#create an array numpy 2D 6x6 with borders of 1 and 0 inside.
#111111
#100001
#100001
#100001
#100001
#111111

base = np.arange(36)
i = 0
while i <= 35:
    if i == 0 or i == 30:
        base[i:i+6]=1
        i+=6
    else:
        base[i] = 1
        base[i+1:i+5] = 0
        base[i+5]=1
        i+=6

base.shape=(6,6)
print(base)