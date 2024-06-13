# 4. Write a Python program to get a list of locally installed Python modules.

import pkgutil

# Get a list of locally installed Python modules
installed_modules = [module.name for module in pkgutil.iter_modules()]

# Print the list of installed modules
print("List of locally installed Python modules:")
for module in installed_modules:
    print(module)
