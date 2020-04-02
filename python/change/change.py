def find_fewest_coins(coins, target, check=None):
    if target < 0:
        raise ValueError('no exact change')
    elif target == 0:
        return []
    temp = target
    change = []
    for coin in coins[::-1]:
        if temp < min(coins):
            return [min(coins)] + find_fewest_coins(coins, target - min(coins))
        elif temp // coin > 0:
            change += [coin for i in range(temp // coin)]
            temp %= coin
        if temp == 0:
            while len(coins) > 1:
                coins = coins[:-1]
                alternate = find_fewest_coins(coins, target, True)
                if alternate and len(alternate) < len(change):
                    change = alternate
            return sorted(change)
    if check:
        return
    else:
        raise ValueError('no exact change')
