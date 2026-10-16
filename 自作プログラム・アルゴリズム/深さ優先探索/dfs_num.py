#N以下の、7,5,3が1回以上現れる数字の総数を求める(ABC114 C問題)
#再帰上限を増やす(なくても動いた)
import sys
sys.setrecursionlimit(1000000)

N = int(input())

ans = 0

#数nについて調べ、末尾に数字を追加した数を再帰的に調べる関数
#use3,use5,use7はそれぞれ3,5,7を使ったかというフラグ
def dfs(n,use3,use5,use7):
	global ans #関数の外で宣言された関数を関数の中で変更する場合は宣言が必要。
	#nを超えていたら打ち切って終了する
	if n > N:
		return
	#3種類全てを使っていたら答えに加算する
	if use3 and use5 and use7:
		ans += 1
	#末尾に3,5,7を付けた数を再帰的に調べる
	dfs(10*n+3,True,use5,use7)
	dfs(10*n+5,use3,True,use7)
	dfs(10*n+7,use3,use5,True)

#何もない状態(値としては0)から呼び出す
dfs(0,False,False,False)

print(ans)