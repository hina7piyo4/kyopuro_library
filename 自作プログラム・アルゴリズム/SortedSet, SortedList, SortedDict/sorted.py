#必ずPyPyで提出!!!
from sortedcontainers import SortedSet, SortedList, SortedDict

sort_X = SortedList([0])

#追加
sort_X.add(6) #SortedList([0, 6])

#削除
sort_X.discard(0) #SortedList([6])


#二分探索があるらしい