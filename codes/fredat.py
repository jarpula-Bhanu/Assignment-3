data = [10,20,36,92,95,40,50,56,60,70,92,88,80,70,72,70,36,40,36,40,92,40,50,50,56,60,70,60,60,88]

total = len(data)

data.sort()

print("marks    frequency\n")

frequency = {}

for item in data:
   if item in frequency:
      frequency[item] += 1
   else:
      frequency[item] = 1

for i in frequency:
    print(i,"     ",frequency[i])

print("\nTotal   ",total)