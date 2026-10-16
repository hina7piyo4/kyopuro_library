#約数を求めるプログラム
def yakusuu(a): #a:整数
    x = set()
    for i in range(1,int(a**(1/2))+1):
        if a % i == 0:
            x.add(i)
            x.add(a//i)
    x = sorted(x)
    return x #リストで返される