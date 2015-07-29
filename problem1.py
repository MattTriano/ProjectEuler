
def threeOrFive(n):
    values = []

    for i in range(n):
        if i%3 == 0:
            values.append(i)
        elif i%5 == 0:
            values.append(i)

    return sum(values)

print(threeOrFive(1000))
