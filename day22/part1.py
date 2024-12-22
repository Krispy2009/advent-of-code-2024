with open('input.txt') as f:
    secrets = [int(i) for i in f.read().splitlines()]

# print(secrets)



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


total = 0
for idx, secret in enumerate(secrets):
    for _ in range(2000):
        secret = get_next_number(secret)
    total += secret
    # print(secrets[idx], secret)


print("Total:", total)

