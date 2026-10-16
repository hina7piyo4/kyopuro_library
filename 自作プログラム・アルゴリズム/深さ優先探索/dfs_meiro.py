#スタートからゴールに辿り着けるか判定 実装例(ATC001 深さ優先探索)
#再帰上限を増やす
import sys
sys.setrecursionlimit(1000000)

H,W = map(int,input().split(" "))
S = []
for i in range(H):
  s = input()
  S.append(s)

#始点と終点の座標を探す
for i in range(H):
  for j in range(W):
    if S[i][j] == "s":
      si,sj = i,j
    if S[i][j] == "g":
      gi,gj = i,j

#N個のFalseで初期化した配列visitedを用意
visited = []
for i in range(H):
	visited.append([False]*W)

#再帰関数dfsを定義
def dfs(i,j):
	visited[i][j] = True
	#4方向の隣マスを探索
	for i2,j2 in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
	  #もし盤面の範囲内でなければ無視
	  if not (0 <= i2 < H and 0 <= j2 < W):
	    continue
	  #もし壁マスであれば無視
	  if S[i2][j2] == "#":
	    continue
	  #もし未訪問なら再帰的に呼び出し
	  if not visited[i2][j2]:
	    dfs(i2,j2)

#始点から呼び出す
dfs(si,sj)

#終点が訪問済みかどうかに応じてYesまたはNoを出力
if visited[gi][gj]:
  print("Yes")
else:
  print("No")