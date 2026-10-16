from atcoder.segtree import SegTree
A = [1,2,3,4,5]

#SegTree(関数、単位元(初期化する値)、元となるリスト)
#最大値
st = SegTree(max,-float('inf'),A) #負の値が出てくるときは-float('inf')で初期化。それ以外は0でもよい。

#最小値
#st = SegTree(min,float('inf'),A)

st.set(0,4)#st.set(p,x) -> p番目の要素をxに置き換える
st.get(1)#st.get(p) -> p番目の要素を取得する(O(1))
st.prod(1,3)#st.prod(l,r) -> 半開区間[l,r)の(指定した)演算結果を求める

#和の時はop↓を記述
def op(x,y):
	return x+y
#和
st2 = SegTree(op,0,A)
#和の時のみ使える
# 合計が 10 以下なら True、10 を超えたら False
f = lambda v: v <= 10
#st2.max_right(l,f) #lから右に伸ばしていったとき、どのあたりまで条件fを満たすのか(0~lまで)
#st2.min_left(r,f) #rから左に伸ばしていったとき、どのあたりまで条件fを満たすのか(r~Nまで)