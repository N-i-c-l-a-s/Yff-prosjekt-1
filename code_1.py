import random


n = random.choices(range(1, 50), k=50)

print(n)


average = sum(n) / len(n)
print("Average of list: ", round(average, 3))

