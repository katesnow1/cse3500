def maxTriangle(triArr):
    #base case triangle only has one number
    if len(triArr) == 1:
        return triArr[0][0]
    #start at second to last row
    for row in range(len(triArr) - 2, -1, -1):
        for num in range(len(triArr[row])):
            if triArr[row+1][num] > triArr[row+1][num+1]:
                triArr[row][num] = triArr[row][num] + triArr[row+1][num]
            else:
                triArr[row][num] = triArr[row][num] + triArr[row+1][num+1]
        triArr.pop()
    return triArr[0][0]

triangle = [
    [7],
    [3, 8],
    [8, 1, 0],
    [2, 7, 4, 4],
    [4, 5, 2, 6, 5]
]

print(maxTriangle(triangle))


def coinCombos(coins):
    combos = {0}
    for num in coins:
        newCombos = set()
        for combo in combos:
            newCombos.add(num+combo)
        combos = combos | newCombos
    combos.pop()
    return combos


k = [2,4,7]

print(coinCombos(k))

