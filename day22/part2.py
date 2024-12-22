from collections import defaultdict
with open('input.txt') as f:
    secrets = [int(i) for i in f.read().splitlines()]


# secrets = [123]
# print(secrets)

prices = defaultdict(list)
price_changes = defaultdict(list)

def  get_next_number(secret):

    to_mix = secret * 64
    #mix
    secret = to_mix ^ secret
    #prune
    secret %= 16777216

    to_mix = int(secret / 32)
    #mix 
    secret = to_mix ^ secret
    #prune
    secret %= 16777216

    to_mix = int(secret * 2048)
    #mix
    secret = to_mix ^ secret
    #prune
    secret %= 16777216

    return secret


for idx, secret in enumerate(secrets):
    og_sec = secret
    prices[og_sec].append(int(str(secret)[-1]))
    price_changes[og_sec].append(None)
    for i in range(1,2000):
        secret = get_next_number(secret)
        prices[og_sec].append(int(str(secret)[-1]))
        price_changes[og_sec].append(prices[og_sec][i] - prices[og_sec][i-1])
        # print(prices)
        # print(price_changes)


    highest_price = max(prices[og_sec])
    # print(highest_price)
# print(price_changes[og_sec])

all_bids = {}

for og_sec in secrets:
    bids = {}
    for idx, _ in enumerate(price_changes[og_sec][4:]):
        idx = idx+4
        group = (price_changes[og_sec][idx-3], price_changes[og_sec][idx-2], price_changes[og_sec][idx-1], price_changes[og_sec][idx])
        # print(idx+4, group)
        if group not in bids:
            bids[group] = prices[og_sec][idx]
    all_bids[og_sec] = bids




# print(all_bids)

all_possibilities = set([x for i in all_bids.values() for x in i.keys()])

# print(all_possibilities)

bananas = []

for pos in all_possibilities:
    # print("checking ", pos, "in all buyers")
    s = 0
    for og_secret in all_bids:
        if pos in all_bids[og_secret]:
            # print("Buyer:", og_secret, "Adding", all_bids[og_secret][pos], "from", pos)
            s += all_bids[og_secret][pos]
    bananas.append((pos, s))

# print(bananas)

print(max(bananas, key=lambda x: x[1]))
