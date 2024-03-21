# Random Module
import random
import my_module

# Random Integer Number (Inclusive - Includes 1 and 10)
random_integer = random.randint(1, 10)
print(random_integer)

# Random Float Number
# 0.00000000... - 0.999999999...
random_float = random.random() * 5
print(random_float)

print(my_module.pi)