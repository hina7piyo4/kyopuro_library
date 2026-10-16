import heapq

N,M = map(int,input().split(" "))

#グラフは隣接リストとして保持する
G = []
for i in range(N):
    G.append([])

#グラフの辺を受け取る
for i in range(M):
    ai,bi = map(int,input().split(" "))
    #頂点番号は-1して0から始まるようにする
    ai = -1
    bi = -1
    #aiとbiの間に辺を張る
    G[ai].append(bi)
    G[bi].append(ai)

#グラフ上でダイクストラ法を実行し、頂点0から各頂点への距離を求める

#頂点0から各頂点への最短距離を保持する配列
#N個の-1で満たしておく(-1の場合は未訪問であることを表す)
dist = []
for i in range(N):
    dist.append(-1)

#ダイクストラ法で使うヒープ
Q = []

#始点となる頂点0をヒープに追加しておく
#(距離、頂点)として追加する
heapq.heappush(Q,(0,0))

#始点となる頂点0への最短距離は0とする
dist[0] = 0

#ヒープから取り出したことがあるかを保存する配列
#最初はN個のFalseで埋めておく
done = []
for i in range(N):
    done.append(False)

#ダイクストラ法で各頂点への最短距離を求める
while len(Q) > 0:
    #ヒープの先頭の頂点を取り出してiとする
    d,i2 = heapq.heappop(Q)

    #もし前にヒープから取り出したことがあれば、
    #隣接する頂点を調べることをスキップする
    if done[i2]:
        continue

    #ヒープから頂点iを取り出したことを記録しておく
    done[i2] = True

    #頂点iに隣接する頂点を順番に見る
    #見ている頂点をjとする
    for j in G[i2]:
        #この問題では、辺の重みは常に1
        x = 1

        #jが未訪問だったとき、あるいはjへの最短距離が更新可能だったとき、
        #jへの最短距離を更新して、ヒープの末尾に追加する
        if dist[j] == -1 or dist[j] > dist[i2] + x:
            dist[j] = dist[i2] + x
            heapq.heappush(Q,(dist[j],j))

if dist[N-1] == 2:
    print("POSSIBLE")
else:
    print("IMPOSSIBLE")