def GenerateBBSTArray(a):
    if a == []:
        return []
    a_sorted = sort_array(a)
    empty = create_empty_array(a)
    balanced = fulfill_empty(a_sorted, empty, index=0)
    return balanced

def sort_array(a):
    return sorted(a)

def create_empty_array(a):
    return [None] * len(a)

def fulfill_empty(a, empty, index=0):
    if a == []:
        pass
    else:
        mid_index = int(len(a) / 2)
        empty[index] = a[mid_index]
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        fulfill_empty(a[:mid_index], empty, left_index)
        fulfill_empty(a[mid_index + 1:], empty, right_index)
    return empty
