# continue.py
fruits = ["apple", "banana", "cherry"]  
for x in fruits:
  if x == "banana":
    continue
  print(x)

# another example
for i in range(1, 10):
    if i % 2 == 1:  # if the number is odd
        continue
    print(i)