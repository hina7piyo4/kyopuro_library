import heapq

a = [1, 6, 8, 0, -1]
heapq.heapify(a) #リストaを優先度付きキューに変換
print(a) # [-1, 0, 8, 1, 6]

x = heapq.heappop(a) #最小値の取り出し(最大値順にしたい時はすべての要素に-1を掛ける)
print(x) # -1
print(a) # [0, 1, 8, 6]

heapq.heappush(a,-2) #要素の挿入
print(a) # [-2, 0, 1, 8, 6]