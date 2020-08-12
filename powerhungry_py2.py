def solution(xs):
    if 0 < len(xs) < 51:
        negatives = [x for x in xs if -1001<x<0]
        positives = [x for x in xs if 1001>x>0]
        if (len(negatives)%2 != 0 and len(xs)>1):
          negatives.sort()
          negatives.pop()
        values = negatives + positives
        if values:
            prod = long(1)
            for value in values:
                prod = prod * value
            return("%s"%prod)
        else:
            return("0")
    else:
        return("0")


arrays = [[-4,0], [-4]]

for x in arrays:
    print(solution(x))