def binary_search(list, target):
    start = 0
    end = len(list)
    middle = 0
    step= 1


    while (start <= end):
        print(f"Steps {step} : {str(list[start:end+1])}")
        step+=1
        middle = (start + end) // 2

        if target == list[middle]:
            return middle
        
        elif target < list[middle]:
            end = middle - 1

        else:
            start = middle + 1

    return -1


ordered_list = [1,2,3,4,5,6,7]
binary_search(ordered_list, 2)