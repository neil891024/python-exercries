#Task #07 作業 02【實作題】n! 階乘計算
x = input() # 4
sum = 1
if not x.isdigit(): #isdight 檢測字符串是否只由數字組成，只對0和正數有效。
    print("是一個不合法的輸入，無法運算")

else:
    x=int(x)

for f in range(1,x+1): #算階層
    sum *= f

print(sum)