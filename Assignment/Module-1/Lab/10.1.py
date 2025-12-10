def sqr_num(i):
    return i * i

num = [1, 2, 3, 4, 5]

sqrt = list(map(sqr_num, num))

print("OG list : ", num)
print("squared list : ", sqrt)