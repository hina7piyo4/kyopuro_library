#インデックス(1始まり)と一緒にソート(デフォルトは大きい順)、a:リスト
def with_index_sort(a):
    sort_a = []
    for i in range(len(a)):
        sort_a.append((a[i],i+1))
    sort_a.sort(key=lambda x:(-x[0],x[1]))#大きい順
    #sort_a.sort(key=lambda x:(x[0],x[1]))#小さい順
    return sort_a #(要素、インデックス)のリストで返す