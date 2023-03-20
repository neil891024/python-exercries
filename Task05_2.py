#Task #05 作業 03【實作題】去除重複與排序
L = [1, 1, 3, 9, 7, 8, 8, 8]
L = list(set(L)) #創建集合，因為集合會將重複的元素消除
L = sorted(L,reverse=True) #排列 True:大~小 False:小~大

print(L)