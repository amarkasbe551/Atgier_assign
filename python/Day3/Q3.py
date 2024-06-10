# . Write a Python program that prints each item and its corresponding type from the following list.
#  Sample List : datalist = [1452, 11.23, 1+2j, True, 'Atgeir', (0, -1), [5, 12], {"class":'V', "section":'A'}]

datalist = [1452, 11.23, 1+2j, True, 'Atgeir', (0, -1), [5, 12], {"class":'V', "section":'A'}]
 
result_list = [(item, type(item)) for item in datalist]

# Printing the result list
print(result_list)
