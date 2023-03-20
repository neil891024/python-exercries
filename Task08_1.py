#Task #08 作業 01【實作題】階乘總和
x = input() # 4 輸入值
sum = 1
val = 0

if not x.isdigit():
    print("是一個不合法的輸入，無法運算")
else:
    x=int(x)

for f in range(1,x+1): #因為不包含x所以寫x+1
    sum *= f #算出輸入的階層 4!
    val += sum #算出階層的總合

print(val)