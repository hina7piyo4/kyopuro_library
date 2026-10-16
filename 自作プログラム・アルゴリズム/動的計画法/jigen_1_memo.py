#Frog1(AtCoder Educational DP Contest A問題)
#別解 メモ化再帰を用いる方法
import sys
sys.setrecursionlimit(1000000) #再帰上限を増やす
N = int(input())
h = list(map(int,input().split(" ")))

cost = [0]*N
#cost[i]が計算済みであることを示すフラグ
done = [False]*N

def rec(i):
    #計算済みであれば、即座に値を返す(ここがメモ化再帰)
    if done[i]:
        return cost[i]
    #そうでなければ値を計算
    if i == 0:
        cost[i] = 0
    elif i == 1:
        cost[i] = rec(0) + abs(h[0]-h[1])
    else:
        cost[i] = min(rec(i-1) + abs(h[i-1]-h[i]), rec(i-2) + abs(h[i-2]-h[i]))
    #計算済みフラグを立てて値を返す
    done[i] = True
    return cost[i]
#答えは最後の足場までの最小コスト
print(rec(N-1))

#メモ化再帰は、インデックス順に値を求めていけないときに用いるとよい。