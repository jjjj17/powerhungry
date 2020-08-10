import numpy as np

array = [2,3,-2,-4,0,5,-9,-5,-2,32,32,1001,0,0,0,0,0,0,-4,-4,-4,-74,-4,-4,-4,-4,-4,-4,4]

def solution(xs):
    if 0 < len(xs) < 50:
        matrix = np.array(xs)
        new_matrix = np.sort(np.delete(matrix, np.where((matrix == 0)|(abs(matrix) > 1000))))
        negatives = [x for x in xs if x<0]
        #print(np.where(new_matrix == -1)[0][0])
        if len(negatives)%2 != 0:
            neg_delete = (min(map(abs, negatives)))*-1
            amount = np.count_nonzero(new_matrix == neg_delete)
            if amount > 1:
                rep = np.repeat(neg_delete, (amount-1))
                final_matrix = np.concatenate((np.delete(new_matrix, np.where(new_matrix == neg_delete)), rep))
                print(final_matrix.dtype)
                return("%s"%(np.prod(final_matrix))) #returns zero due to integer overflow
            else:
                final_matrix = np.delete(new_matrix, np.where(new_matrix == neg_delete))
                return("%s"%(np.prod(final_matrix)))
            
        else:
            return("%s"%np.prod(new_matrix))

    
print(solution(array))