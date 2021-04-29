import random
import string

letters = "Mynameis"
result_str = ''.join(random.choice(letters) for i in range(3))
print(result_str)
