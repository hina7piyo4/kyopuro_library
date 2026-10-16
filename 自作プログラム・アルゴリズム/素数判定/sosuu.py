def eratosthenes(_,n):
# _以上n以下の整数をTrueで初期化
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False # 0と1は素数ではない

    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:# iの倍数をFalseに設定
            for j in range(i * i, n + 1, i):
                is_prime[j] = False

    # 素数のみをリストとして返す
    return [i for i in range(max(2, _), n + 1) if is_prime[i]]

# 使用例
s = 11
n = 50
primes = eratosthenes(s,n)
print(f"{s}以上{n}以下の素数: {primes}")