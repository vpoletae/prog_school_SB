import math

def GenerateBBSTArray(a):
    depth = int(math.log((len(a) + 1), 2) - 1)
    if len(a) == 0:
        return []
    elif len(a) == 1:
        return a
    else:
        ordered_array = order_array(sorted(a))
        return(ordered_array)
        # if len(ordered_array) <= 3:
        #     return ordered_array
        # else:
        #     reordered = reorder(ordered_array, depth)
        #     return reordered

# def reorder(ordered_array, depth):
#     to_reorder = ordered_array[1:]
#     mid_index = int(len(to_reorder) / 2 - 1)
#     left_subtree = to_reorder[:(mid_index + 1)]
#     right_subtree = to_reorder[(mid_index + 1):]
#     reordered = ordered_array[:1]
#     for level in range(depth):
#         nodes_on_lvl = 2 ** level
#         for i in range(nodes_on_lvl):
#             to_add = left_subtree.pop(0)
#             reordered += [to_add]
#         for i in range(nodes_on_lvl):
#             to_add = right_subtree.pop(0)
#             reordered += [to_add]
#     return reordered


def order_array(sorted_array):
    if len(sorted_array) <= 2:
        return sorted_array
    index = int()
    if len(sorted_array) % 2 == 0:
        index = (len(sorted_array) // 2) - 1
    else:
        index = (len(sorted_array) // 2 + 1) - 1
    return [sorted_array[index]] + order_array(sorted_array[:index]) + order_array(sorted_array[(index + 1):])
