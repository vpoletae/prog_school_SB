def SelectionSortStep(array: list, index: int):
    if index >= len(array)-1:
        pass
    else:
        val = array[index]
        post = array[index+1:]
        min_val = min(post)
        if min_val < val:
            min_index = post.index(min_val) - len(post)
            array[min_index] = val
            array[index] = min_val

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

def InsertionSortStep(array: list, step: int, index: int):

    if len(array) <= 1:
        pass
    else:
        next_index = index + step
        if next_index > len(array)-1:
            return array
        else:
            indexes = [index]
            values = [array[index]]
            while not next_index > len(array)-1:
                indexes.append(next_index)
                values.append(array[next_index])
                next_index += step
        index_value = list(zip(indexes, sorted(values)))
        for pair in index_value:
            array[pair[0]] = pair[1]
