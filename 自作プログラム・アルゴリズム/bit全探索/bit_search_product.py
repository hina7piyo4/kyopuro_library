#productを用いたコード。3進数以上のときはこっちの方が分かりやすいかも。
#PyPyで提出した方がいい。(CPythonだとN=20でギリギリ)
from itertools import product

for i in product(range(2), repeat=3): #rangeの中は〇進数,repeatはN
    print(list(i)) #iのままだとタプルになる。リストに変換したいときはこのようにする。
# [0, 0, 0]
# [0, 0, 1]
# [0, 1, 0]
# [0, 1, 1]
# [1, 0, 0]
# [1, 0, 1]
# [1, 1, 0]
# [1, 1, 1]