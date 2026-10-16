#Frog1(AtCoder Educational DP Contest A問題)
N = int(input())
h = list(map(int,input().split(" ")))

#足場iに辿り着くための最小コスト
cost = [0]*N

cost[0] = 0
#2つめの足場はジャンプ元が1通り
cost[1] = cost[0] + abs(h[0]-h[1])
#それ以降の足場はジャンプ元が2通りあるため、コストが小さいほうを採用
for i in range(2,N):
    cost[i] = min(cost[i-1] + abs(h[i-1]-h[i]), cost[i-2] + abs(h[i-2]-h[i]))

#答えは最後の足場までの最小コスト
print(cost[N-1])