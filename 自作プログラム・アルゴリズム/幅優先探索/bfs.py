from collections import deque

#頂点数N,辺情報E,始点s
N = int(input())
s = int(input())
#N個のFalseで初期化した配列visitedを用意
visited = []
for i in range(N):
	visited.append(False)

#キューを用意
Q = deque()
Q.append(s)
visited[s] = True

#キューから取り出しながら探索
while len(Q) > 0:
	i = Q.popleft() #poprightにすると、深さ優先になる
	for j in E[i]:
		if not visited[j]:
			visited[j] = True
			Q.append(j)