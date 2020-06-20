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

def KnuthSequence(array_size: int)-> list:
    if array_size <= 1:
        return [1]
    else:
        cur_elem = 1
        knuth_seq = [cur_elem]
        next_elem = 3 * cur_elem + 1
        if next_elem > array_size:
            pass
        else:
            while not next_elem > array_size:
                knuth_seq.insert(0, next_elem)
                cur_elem = next_elem
                next_elem = 3 * cur_elem + 1
        return knuth_seq

def ArrayChunk(array: list, pivot_i=None, i1=None)-> int:
    if len(array) == 0:
        return None
    elif len(array) == 1:
        return 0
    elif len(array) == 2:
        if array[0] > array[1]:
            lower = array[1]
            array[1] = array[0]
            array[0] = lower
        else:
            pass
        return 0
    else:
        if pivot_i is None:
            pivot_i = int(len(array)/2)
            i1 = 0
        else:
            pass
        pivot_v = array[pivot_i]
        i2 = len(array)-1

        while array[i1] < pivot_v:
            i1 += 1
        while array[i2] > pivot_v:
            i2 -= 1

        if array[i1] > array[i2]:
            if i1 == pivot_i:
                pivot_i = i2
            elif i2 == pivot_i:
                pivot_i = i1
            exch = array[i1]
            array[i1] = array[i2]
            array[i2] = exch
            ArrayChunk(array, pivot_i, i1)

        if i1 == i2-1 and array[i1] > array[i2]:
            exch = array[i1]
            array[i1] = array[i2]
            array[i2] = exch
            ArrayChunk(array, pivot_i, i1)
        elif i1 == i2 or (i1 == i2-1 and array[i1] < array[i2]):
            if array[i1] >= pivot_v and array[i2] <= pivot_v:
                exch = array[i1]
                array[i1] = array[i2]
                array[i2] = exch
                pivot_i -= 1
                return pivot_i
            else:
                return pivot_i
        else:
            return pivot_i
