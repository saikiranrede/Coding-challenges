"""Given an array of integers, find all pairs whose sum is a given value.
Input: Array of Integers, Integer
Output: Array of pairs. """



def pairs(seq, value):
    final_list = []
    for item1 in seq:
        for item2 in seq:
            if item1 + item2 == value:
                final_list.append((item1, item2))
    #return [(x, y) for x in seq for y in seq if x+y == value ]     #Can also use list Comps for single line execution
    return final_list


print(pairs([8, 7, 2, 5, 3, 1], 10))
