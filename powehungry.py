import numpy as np

array = [-2,-3,4,-5]

def solution(xs):
    #limpieza
    matrix = np.array(xs)
    new_matrix = np.delete(matrix, np.where(matrix == 0)) #delete zeroes to keep product from being 0
    product = np.prod(new_matrix)
    
    negatives = len([x for x in xs if x<0])
    positives = len([x for x in xs if x>0])
    
    return(f"{product}")
    



print(solution(array))