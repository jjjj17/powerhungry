array = [2,3,-2,-4,0,5,-9,-5,-2,32,32,1001,0,0,0,0,0,0,-4,-4,-4,-74,-4,-4,-4,-4,-4,-4,4,-2,-2]

def solution(xs):
    prod = 1
    if 0 < len(xs) < 50:
        arr_list = sorted([x for x in xs if x != 0 or abs(x) > 1000])
        print(arr_list)
        negatives = [x for x in xs if x<0]
        print(len(negatives))
        rep = []
        if len(negatives)%2 != 0:
            neg_delete = (min(map(abs, negatives)))*-1
            print(neg_delete)
            amount = arr_list.count(neg_delete)
            print(amount)
            if amount > 1:
                arr_list.remove(neg_delete)
                rep += (amount-1) * [neg_delete]
                print(rep)
                final_list = arr_list + rep
                print(final_list)
                for x in arr_list:
                    prod = prod * x
                return("%s"%prod)
            else:
                pass
                arr_list.remove(neg_delete)
                final_list = arr_list + rep
                for x in arr_list:
                    prod = prod * x
                return("%s"%prod)
        else:
            for x in arr_list:
                prod = prod * x
            return("%s"%prod)


print(solution(array))