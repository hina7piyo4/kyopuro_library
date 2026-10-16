from collections import deque

R,C = map(int,input().split(" ")) #R行C列
sy,sx = map(int,input().split(" ")) #スタート地点の座標
gy,gx = map(int,input().split(" ")) #ゴール地点の座標

S = [] #2次元のグリッド
for i in range(R):
  s = input()
  S.append(s)

sy -= 1
sx -= 1
gy -= 1
gx -= 1

#始点からの最小移動回数を管理する2次元配列。-1なら未訪問
dist = []
for i in range(R):
  dist.append([-1]*C)

#キューを用意して、始点を入れる
Q = deque()
Q.append([sy,sx])
dist[sy][sx] = 0

edge = [[0,1],[0,-1],[1,0],[-1,0]]

#キューから取り出しながら探索
while len(Q) > 0:
  i,j = Q.popleft() #poprightにすると、深さ優先になる
  #4つの隣マスを確認する
  for x,y in edge:
    i2,j2 = i+x,j+y
    #もし盤面の範囲内でなければ無視する
    if not (0 <= i2 < R and 0 <= j2 < C):
      continue
    #もし壁マスであれば無視する
    if S[i2][j2] == "#":
      continue
    #もし未訪問(dist[i2][j2]が-1)であれば、距離を更新してキューに入れる
    if dist[i2][j2] == -1:
      dist[i2][j2] = dist[i][j] + 1
      Q.append([i2,j2])

#始点から終点までの最小移動回数を出力
print(dist[gy][gx])