def targetscore(x):
    points = 0
    if x == 1:
        points += 50
        return points
    elif x == 2:
        points += 40
        return points
    elif x == 3:
        points += 30
        return points
    elif x == 4:
        points += 20
        return points
    elif x == 5:
        points += 10
        return points
    else:
        return points


point = int(input("what row u hit??? 1, 3, 3, 4, or 5: "))
print(targetscore(point))
