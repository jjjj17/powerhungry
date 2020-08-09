import numpy as np

array = [-5,0,38,-9]

def solution(xs):
    matrix = np.array(xs)
    new_matrix = np.sort(np.delete(matrix, np.where(matrix == 0))) #delete zeroes to keep product from being 0)
    negatives = [x for x in xs if x<0]
    if len(negatives)%2 != 0:
        neg_delete = (min(map(abs, negatives)))*-1
        final_matrix = np.delete(new_matrix, np.where(new_matrix == neg_delete))
        return(f"{np.prod(final_matrix)}")
    else:
        return(f"{np.prod(new_matrix)}")

    
print(solution(array))