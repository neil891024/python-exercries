#Task #07 作業 03【實作題】奇偶數分堆
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
even = [] #偶數
odd = [] #奇數

for x in L:
    if x%2 != 0: #判斷餘數是否為0
        even.append(x)
    else:
        odd.append(x)

L=even+odd
print(L) # [1, 3, 5, 7, 9, 0, 2, 4, 6, 8]