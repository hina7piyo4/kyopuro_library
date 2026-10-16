import heapq
N, M = list(map(int, input().split()))
ABC = [list(map(int, input().split())) for in range(M)]

# ネットワークの作成
adj = [[] for in range(N + 1)]
for a, b, c in ABC:
    adj[a].append((b, c))
    adj[b].append((a, c))

dist = [-1] * (N + 1)     # dist[v]: 点vまでの最短距離．1-index
q = [(0, 1)]              # (vまでの距離（最短とは限らない）, v)
while q:
    d, v = heapq.heappop(q)     # 距離最短の点 vを獲得
    if dist[v] >= 0:    # 決定済みの点はスキップ
        continue
    dist[v] = d     # 点vまでの最短距離確定
    for u, c in adj[v]:
        if dist[u] == -1:   # 点vと隣接する点uが最短距離未決定の場合
            heapq.heappush(q, (d + c, u))
print(*dist[1:])  # 各点への最短距離を表示．1-index