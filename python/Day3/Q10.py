# 10. Given a list with multiple sub list inside it. Convert it into flat list.
# Ex:
# x=[[1,2,3],[10,[4,6,7]],8]
# Output:
# [1,2,3,10,4,6,7,8]

x = [[1, 2, 3], [10, [4, 6, 7]], 8]

def flatten_list(lst):
    flat_list = []
    for item in lst:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list

op = flatten_list(x)
print("Answer:", op)
