import bisect

a = [1,3,3,5,7]
a.sort() #ソート済みリストでなければいけない

print(bisect.bisect_left(a,3))  #1 (3が現れる最初の位置)
print(bisect.bisect_right(a,3)) #3 (3が現れる最後の位置の「次」)
print(bisect.bisect(a,3))       #3 (bisect_rightと同じ)
print(bisect.bisect(a,3,lo=1,hi=3)) #3 lo(最小位置),hi(最大位置)で探索範囲を指定できる