#Task #09 作業 02【實作題】定義函式
NUMBER_PRIME=2
NMUBER_COMPOSITE=1
NMUBER_NONE=0

def number(n):
    """判斷是否為質數"""
    if n<=1: 
        return NMUBER_NONE
    flag=0
    for i in range(1,n+1):
        if n%i == 0:
            flag+=1
    if flag > 2: 
        return NMUBER_COMPOSITE
    else:
        return NUMBER_PRIME
    
def primes(n):
    """列出小於n的質數"""
    prime = []
    for i in range(1,n+1):
        if number(i)==NUMBER_PRIME:
            prime.append(i)
    return prime
    
n = int(input("請輸入一個數字:"))
print(primes(n))