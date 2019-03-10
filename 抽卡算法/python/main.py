import random
# 解决抽够所有胎五需要多少抽的问题


i = 10000  # 迭代次数
n = 2  # 胎五总数量
p = 100  #胎五顶峰数量
file_handle = open("1.txt",mode="w")
for n in range(2,p+1):
    m = 0  # 总实验数量
    s = set()
    for i in range(i):
        for j in range(n):
            s.add(j)
        while True:
            k = random.randint(0, n-1)
            if k in s:
                s.remove(k)
            m = m + 1
            if not s:
                break

    print(n,"final answer wa",m/i)
    file_handle.write(str(n))
    file_handle.write("\t")
    file_handle.write(str(m/i))
    file_handle.write("\n")