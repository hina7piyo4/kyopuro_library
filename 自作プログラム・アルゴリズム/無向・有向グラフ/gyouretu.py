#N個の頂点、M本の無向(有向)辺
N,M = map(int,input().split(" "))

#初期化
graph = []
for i in range(N):
	row = []
	for j in range(N):
		row.append(False)
	graph.append(row)

#辺の情報を書き込み
for i in range(M):
	u,v = map(int,input().split(" "))
	graph[u-1][v-1] = True
	#(無向グラフのときのみ)
	#graph[v-1][u-1] = True