#再帰上限を増やす(*必須*)
import sys
sys.setrecursionlimit(1000000) #中の数字は頂点数よりは多くすること。

#頂点数N、辺情報E、始点S
N = int(input())
E = [[] for _ in range(N)]
s = int(input())

#N個のFalseで初期化した配列visitedを用意
visited = []
for i in range(N):
	visited.append(False)

#再帰関数dfsを定義
def dfs(i):
	visited[i] = True
	for j in E[i]:
		if not visited[j]:
			dfs(j)

#始点から呼び出す
dfs(s)