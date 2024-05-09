inp = open('input4.txt', 'r')
out = open('output4.txt', 'w')

n, amount = map(int, inp.readline().split())
coins = list(map(int, inp.readline().split()))


def mini_num_coins(coins, amount):
    queue = [(0, 0)]
    visited = set()

    while queue:
        sum_amount, num_coin = queue.pop(0)
        if sum_amount == amount:
            return num_coin
        for i in coins:
            next_amount = sum_amount + i
            if next_amount <= amount and next_amount not in visited:
                queue.append((next_amount, num_coin + 1))
                visited.add(next_amount)
    return -1


out.write(str(mini_num_coins(coins, amount)))

inp.close()
out.close()


'''
To solve this problem, i Have used a queue.
in this q the sum total of coins value and the 
required number of coins stored. in while loop all the possible sum total
append in the queue and it check wheather the amount is equal to
the given total amount. if it exceed the value it print -1, otherwse it print
the minimum coin required for making the required amount. thus it
it give the minimum required number of coins.
'''
