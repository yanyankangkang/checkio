from copy import deepcopy


def count_gold(pyramid):
    result = []
    for i in pyramid[::-1]:
        tempResult = deepcopy(list(i))
        if not result:
            result = deepcopy(tempResult)
            continue
        for j in range(len(tempResult)):
            tempResult[j] = tempResult[j] + max(result[j], result[j + 1])
        result = deepcopy(tempResult)
    return max(result)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for
    # auto-testing
    assert count_gold((
        (1,),
        (2, 3),
        (3, 3, 1),
        (3, 1, 5, 4),
        (3, 1, 3, 1, 3),
        (2, 2, 2, 2, 2, 2),
        (5, 6, 4, 5, 6, 4, 3)
    )) == 23, "First example"
    assert count_gold((
        (1,),
        (2, 1),
        (1, 2, 1),
        (1, 2, 1, 1),
        (1, 2, 1, 1, 1),
        (1, 2, 1, 1, 1, 1),
        (1, 2, 1, 1, 1, 1, 9)
    )) == 15, "Second example"
    assert count_gold((
        (9,),
        (2, 2),
        (3, 3, 3),
        (4, 4, 4, 4)
    )) == 18, "Third example"
