# Color List
color_list = ["Red", "Green", "White", "Black", "brown", "red"]

# Finding the indices of the middle two elements
middle_index1 = len(color_list) // 2 - 1
middle_index2 = middle_index1 + 1

# Extracting the middle two colors
middle_colors = color_list[middle_index1:middle_index2 + 1]

# Displaying the middle two colors
print("Middle two colors:", middle_colors)
