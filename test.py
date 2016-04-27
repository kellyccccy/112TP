import random

def getNextElevator():
    bound1 = random.randint(100, 360)
    bound2 = random.randint(100, 360)
    y = random.randint(100, 360)
    lowerBound = min(bound1, bound2)
    upperBound = max(bound1, bound2)
    legal1 = False # check whether the y is within bound
    while not legal1:
        if isLegalElevator(lowerBound, upperBound, y):
            legal1 = True
        else:
            y = random.randint(100, 360)
    print(lowerBound, y, upperBound)


def isLegalElevator(lower, upper, y):
    if lower <= y and upper >= y and lower < upper:
        return True
    else: return False