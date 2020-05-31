def SelectionSortStep(array: list, index: int)-> list:
    if index > len(array)-1:
        return None
    elif index == len(array)-1:
        return array

    prev = array[:index]
    val = array[index]
    post = array[index+1:]
    min_val = min(post)
    if min_val < val:
        min_index = post.index(min_val)
        post[min_index] = val
        return prev + [min_val] + post
    else:
        return array

def BubbleSortStep(array: list)-> bool:
    if len(array) <= 1:
        return True
    changes = 0
    offset = 1
    for i in range(len(array)):
        if array[i] > array[offset]:
            min_val = array[offset]
            array[offset] = array[i]
            array[i] = min_val
            changes += 1
        else:
            pass
        if offset == len(array)-1:
            pass
        else:
            offset += 1
    if changes == 0:
        return True
    else:
        return False
