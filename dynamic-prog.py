
def solution(n, coins):
    # ascendingCoins = sorted(list(coins), reverse=True)
    total = 0
    for coin in coins:
        total += solve(n - coin, coins, coin)
    return total

cache = {}

def solve(n, coins, lastCoin):
    if (n, lastCoin) in cache:
        return cache[(n, lastCoin)]
    if n == 0:
        return 1
    if n < 0:
        return 0
    total = 0
    for coin in coins:
        if coin >= lastCoin:
            total += solve(n - coin, coins, coin)
    cache[(n, lastCoin)] = total
    return total


def solveDfs(target, coins, lastCoin):
    if target == 0:
        return 1
    if target < 0:
        return 0

    total = 0
    for coin in coins:
        if coin >= lastCoin:
            total += solveDfs(target - coin, coins, coin)

    return total

def main():
    myset = {1,5}

    print(solveDfs(15, myset, min(myset)))
    print(solution(15, myset))
main()