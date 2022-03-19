my_array = [1, 4, 10, 6, 8, 3, 9, 5, 12]
target = 13


def find_summators(array, target):
    for i in range(len(array) - 1):
        index_1 = 0
        index_2 = len(array) - 1
        couple = array[index_1] + array[len(array)-1]

        if couple < target:
            index_1 += 1
        elif couple > target:
            index_2 -= 1
        elif couple == target:
            summators = [array[index_1], array[index_2]]
        else:
            summators = []
            break
    
    return summators


print(find_summators(my_array, 13))
