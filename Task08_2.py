#Task #08 作業 02【實作題】字串計數
#算出文字在字串中出現的次數
x = input()
dic1= {i: x.count(i) for i in x}
print(dic1)