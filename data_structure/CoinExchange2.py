def countCoinExchange(coins, numDiffCoins, change):
    N = [[-1] * (change+1)] * (numDiffCoins+1)

    # base case
    for i in range(numDiffCoins+1):
        N[i][0] = 1
    for i in range(1, change+1):
        N[0][i] = 0

    # for n in range(1, numDiffCoins+1):
    #     for k in range(1, change+1):
    #         if k-coins[n] < 0:
    #             numComb = 0
    #         else:
    #             numComb = N[n][k-coins[n]]
    #         N[n][k] = N[n-1][k] + numComb
    # print(N[numDiffCoins][change])
    print(N)

coins = [1, 5, 10, 21, 25]
change = 7
countCoinExchange(coins, len(coins), change)