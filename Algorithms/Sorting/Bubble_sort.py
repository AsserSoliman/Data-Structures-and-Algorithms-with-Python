# Bubble sort
# Complexity O(n^2)

for i in range(len(x)-1):
  for j in range(len(x)-1-i):
      if x[j] > x[j+1]:
        temp = x[j+1]
        x[j+1] = x[j]
        x[j] = temp
