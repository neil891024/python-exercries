#Task #09 作業 03【實作題】計算總和的函數
def f(*args): #可帶入多個參數
    result = 0
    for num in args:
        result += num
    return result

print(f(1, 2, 3)) # 6
print(f(1, 2, 3, 4, 5)) #15