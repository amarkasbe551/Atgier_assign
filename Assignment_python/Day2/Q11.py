# 11. Given sample integers below:
# 12345
# 90213
# 123456
# WAP such that the code produces below output :
# (Print 1st digit + last digit + 2nd digit + 2nd last digit + …so on)
# 15243
# 93012
# 162534

# Given sample integers
integers = [12345, 90213, 123456]

# Iterate over the integers
for i, num in enumerate(integers):
    num_str = str(num)
    rearranged_num = ''
    for j in range(len(num_str) // 2):
        rearranged_num += num_str[j] + num_str[-(j + 1)]
    # If the number has an odd number of digits, add the middle digit
    if len(num_str) % 2 == 1:
        rearranged_num += num_str[len(num_str) // 2]
    print(f"{chr(97+i)}. {rearranged_num}")



