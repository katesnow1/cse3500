import random
#generate array of balls, where each ball is represented by boolean value (False = not radioactive, True = radioactive)
#one index is randomly generated to represent the radioactive ball
n = 100000 #number of balls in problem, can be changed by user
balls = []
for i in range(n):
    balls.append(False)
randomIndex = random.randint(0, n-1)
balls[randomIndex] = True 


def findRadioactive(balls, offset=0):
    #this function returns the index of the radioactive ball in the array
    #offset is to keep track of original index
    if len(balls) == 1:
        return offset
    else:
        middle = len(balls) // 2
        #because we dont have the detection box in this code, i will just check if the random index is in the first half of the array
        if randomIndex < middle + offset:
            return findRadioactive(balls[:middle], offset)
        else:
            return findRadioactive(balls[middle:], offset + middle)

print(findRadioactive(balls))


