#Knapsack1(AtCoder Educational DP Contest D問題)
#PyPyで提出
N,W = map(int,input().split(" "))
#1始まりにするため、先頭にダミーを入れる
ws = [0]
vs = [0]
for i in range(N):
    w,v = map(int,input().split(" "))
    ws.append(w)
    vs.append(v)

#value[i][j]:品物iまで見て重さjであるときの価値の総和の最大値
#非常に小さい値で初期化しておく
value = []
for i in range(N+1):
    value.append([-10**18]*(W+1))

#初期条件
value[0][0] = 0

#iが小さい順に求めていく
for i in range(1,N+1):
    for j in range(W+1):
        #品物iを使わない場合
        value[i][j] = max(value[i][j],value[i-1][j])
        #品物iを使う場合
        if j-ws[i] >= 0:
            value[i][j] = max(value[i][j],value[i-1][j-ws[i]]+vs[i])

#value[N][0],...,value[N][W]の中で一番価値の総和が大きいものを答えとする
ans = max(value[N])
print(ans)