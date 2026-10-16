#N個の頂点、M本の無向(有向)辺
N,M = map(int,input().split(" "))

#初期化
graph = []
for i in range(N):
  row = []
  graph.append(row)

#辺の情報を書き込み
for i in range(M):
  u,v = map(int,input().split(" "))
  graph[u-1].append(v-1)
  #(無向グラフのときのみ)
  #graph[v-1].append(u-1)