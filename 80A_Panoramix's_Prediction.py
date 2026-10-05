n, m = map(int, input().split())
def is_prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

next_prime = n + 1
while not is_prime(next_prime):
    next_prime += 1
print("YES" if next_prime == m else "NO")