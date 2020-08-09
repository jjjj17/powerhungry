import numpy as np

array = [2,0,2,2,0,2,0,2,2,0,2,0,2,2,0,2,0,2,2,0,2,0,2,2,0,2,0,2,2,0,2,0,2,2,0,2,0,2,2,0,2,0,2,2,0,2,0,2]

def solution(xs):
    matrix = np.array(xs)
    negatives = len([x for x in xs if x<0])
    positives = len([x for x in xs if x>0])
    zeros = len([x for x in xs if x == 0])
    #return negatives, positives, zeros
    return(matrix)



a,b,c = solution(array)

print(f"numero de negativos: {a}")
print(f"numero de positivos: {b}")
print(f"numero de ceros: {c}")