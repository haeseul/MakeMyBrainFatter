def coinExchange(coins, numDiffCoins, change, C, L):
    # base case
    C[0], L[0] = 0, 0

    # 거스름돈으로 가능한 경우 = k
    for k in range(1, change+1):
        minCoins = k
        newCoin = 1
        for j in range(numDiffCoins):
            if coins[j] > k: continue
            if C[k-coins[j]] + 1 < minCoins:
                minCoins = C[k-coins[j]] + 1
                newCoin = coins[j]
        C[k] = minCoins
        L[k] = newCoin
    print(C[change])

def reconstruct(change, lastCoin):
    if change > 0:
        reconstruct(change - lastCoin[change], lastCoin)
        print('%d' % lastCoin[change])

coins = [1, 5, 10, 21, 25]
change = 23
C = [0] * (change+1)  # used coin
L = [0] * (change+1)  # last coin
coinExchange(coins, len(coins), change, C, L)
reconstruct(change, L)