import numpy as np

array = [4,-5,0,38,-9]

def solution(xs):
    #limpieza
    matrix = np.array(xs)
    new_matrix = np.sort(np.delete(matrix, np.where(matrix == 0))) #delete zeroes to keep product from being 0)

    negatives = [x for x in xs if x<0]

    print(xs)

    if len(negatives)%2 != 0:
        print("not hey")
        min_neg = min(map(abs, negatives))
        neg_delete = min_neg*-1

        final_matrix = np.delete(new_matrix, np.where(new_matrix == neg_delete))
        return(f"{np.prod(final_matrix)}")
    else:
        print("hey")
        return(f"{np.prod(new_matrix)}")

    
print(solution(array))