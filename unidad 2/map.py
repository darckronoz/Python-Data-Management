#apply 25% increase to this prices, using map
#the price can't be increased if it surpass 270.000 with the increase

prices = [275.000 , 125.990 , 76.400, 110.900, 68.990, 185.900, 56.850, 352.950, 456.990,
30.990, 69.990, 206.350]

print(list(map(lambda x: x+(x*0.25) if x+(x*0.25)<270.000 else x, prices)))