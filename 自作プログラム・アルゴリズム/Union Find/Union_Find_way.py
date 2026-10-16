from atcoder.dsu import DSU
#Union Find
#無向グラフで、2頂点が連結かどうかを調べる。
#辺を追加する、2頂点が連結かどうかの判定をするのが速くできる
N = 5
uf = DSU(N)          #初期化(Nは頂点数)
print(uf.groups())   #各連結成分のリストを返す。[[0], [1], [2], [3], [4]]

uf.merge(0, 1)       #頂点0の連結成分と頂点1の連結成分を結合する。この連結成分の代表元を返す。
print(uf.merge(0,1)) #0
print(uf.groups())   #[[0, 1], [2], [3], [4]]

uf.same(0,1)         #2頂点0,1が同じ連結成分ならTrueを、そうでない場合はFalseを返す。
print(uf.same(0,1))  #True
print(uf.same(1,2))  #False

uf.leader(0)         #頂点0の連結成分の代表元を返す。
print(uf.leader(0))  #0

uf.size(0)           #頂点0の連結成分の頂点数を返す。
print(uf.size(0))    #2
print(uf.size(3))    #1