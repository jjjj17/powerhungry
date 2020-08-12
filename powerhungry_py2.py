def solution(xs):
    if 0 < len(xs) < 50:
        negatives = [x for x in xs if x<0]
        positives = [x for x in xs if x>0]
        if len(negatives)%2 != 0:
            negatives.sort()
            negatives.pop()
        values = negatives + positives
        if values:
            prod = 1
            for value in values:
                print(value)
                prod = prod * value
            return("%s"%prod)
        else:
            return("0")
    else:
        return("0")


array = [-4,-2,-4]
print(solution(array))