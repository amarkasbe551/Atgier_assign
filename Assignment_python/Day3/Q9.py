# 9.Input : test_list = [(25, 6), (34, 7), (214, 235), (12, 45), (78, ),(111,22),[356,729]]
# Output : [(214, 235)] 
# Explanation : Extract tuples having 3 digit elements.

test_list = [(25, 6), (34, 7), (214, 235), (12, 45), (78,), (111, 22), [356, 729]]

result_list = []

for tup in test_list:
    if all(isinstance(item, int) and 100 <= item < 1000 for item in tup):
        result_list.append(tup)

# Output
print("Output:", result_list)

