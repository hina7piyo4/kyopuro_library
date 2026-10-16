#遅延セグメント木
from atcoder.lazysegtree import LazySegTree

A = [] #初期リスト
INF = float('inf')

#1.区間加算・区間最小値取得
def mapping(x, y):
    return x + y
def composition(x, y):
    return x + y

e = INF
id_ = 0
seg = LazySegTree(min, e, mapping, composition, id_, A)

#2.区間加算・区間最大値取得
def mapping(x, y):
    return x + y
def composition(x, y):
    return x + y

e = -INF
id_ = 0

seg = LazySegTree(max, e, mapping, composition, id_, A)

#3.区間加算・区間和取得
def op(x, y):
    return x + y
def mapping(x, y):
    return x + y
def composition(x, y):
    return x + y

e = 0
id_ = 0

seg = LazySegTree(op, e, mapping, composition, id_, A)

#4.区間変更・区間最小値取得
ID = INF
def mapping(x, y):
    if x == ID:
        return y
    else:
        return x
def composition(x, y):
    if x == ID:
        return y
    else:
        return x
e = INF
id_ = ID

seg = LazySegTree(min, e, mapping, composition, id_, A)

#5.区間変更・区間最大値取得
ID = INF
def mapping(x, y):
    if x == ID:
        return y
    else:
        return x
def composition(x, y):
    if x == ID:
        return y
    else:
        return x
e = -INF
id_ = ID

seg = LazySegTree(max, e, mapping, composition, id_, A)

#6.区間変更・区間和取得
ID = INF
def op(x, y):
    return x + y
def mapping(x, y):
    if x == ID:
        return y
    else:
        return x
def composition(x, y):
    if x == ID:
        return y
    else:
        return x
e = 0
id_ = ID

seg = LazySegTree(op, e, mapping, composition, id_, A)

#メソッド集
#seg.apply(l,r,x) #半開区間[l,r)の要素に対して、区間加算(変更)をする
#seg.prod(l,r) #半開区間[l,r)の要素すべてについて、最大値(最小値、総和)を取得
#seg.get(p) #A[p]の値を取得する
#seg.set(p,x) #A[p]にxを代入する