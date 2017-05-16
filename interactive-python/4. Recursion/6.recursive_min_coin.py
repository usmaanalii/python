def min_coin(coin_value_list, change):
    min_coins = change
    if change in coin_value_list:
        return 1
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + min_coin(coin_value_list, change - i)
            if num_coins < min_coins:
                min_coins = num_coins

    return min_coins

#  print(min_coin([1, 5, 10, 25], 63))


def min_coin_table(coin_value_list, change, known_results):
    min_coins = change
    if change in coin_value_list:
        known_results[change] = 1
        return 1
    elif known_results[change] > 0:
        return known_results[change]
    else:
        for i in [c for c in coin_value_list if c <= change]:
            num_coins = 1 + \
                min_coin_table(coin_value_list, change - i, known_results)
            if num_coins < min_coins:
                min_coins = num_coins
                known_results[change] = min_coins

    return min_coins


print(min_coin_table([1, 5, 10, 25], 63, [0] * 64))
