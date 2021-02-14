def get_rabbits(months):
    if months <= 2:
        return 1
    return get_rabbits(months - 1) + get_rabbits(months - 2)


for months in range(1, 50 + 1):
    print(months, get_rabbits(months))
