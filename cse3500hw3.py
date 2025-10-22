def maxTriangle(triArr):
    #base case triangle only has one number
    if len(triArr) == 1:
        return triArr[0][0]
    #start at second to last row
    print(triArr[-2])



triArr = [[7], [3,8], [8,1,0], 
          [2,7,4,4], [4,5,2,6,5]]
baseCase = [[4]]

print(maxTriangle(baseCase))