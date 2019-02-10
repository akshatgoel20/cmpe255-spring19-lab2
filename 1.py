def mean_num_friends(x):
    # TODO
    sum = 0
    for (y) in num_friends:
        sum = sum + y

    return sum / len(num_friends)


def median_num_friends(x):
    # TODO
    num_friends.sort()
    lenSize = len(num_friends)
    if (lenSize % 2 != 0):
        m = int((lenSize - 1) / 2)
        return num_friends[m]
    else:
        m = int((lenSize / 2) - 1)
        n = int(lenSize / 2)
        evenSum = (num_friends[m] + num_friends[n]) / 2
        return evenSum


num_friends = [100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("mean=", mean_num_friends(num_friends))
print("median", median_num_friends(num_friends))
