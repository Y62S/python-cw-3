# write your code here
favorite_animals = ["dog" , "cat" , "monkey" , "rabit"]
print(favorite_animals)
print(favorite_animals[1])
favorite_animals.remove("monkey")
print(favorite_animals)
favorite_animals.append("lion")
print(favorite_animals)

for animal in favorite_animals:
  print(f"i love {animal}")

  numbers = [5 , 4 , 3 , 2 , 1]
  numbers_sum = 0
  for num in numbers:
    numbers_sum+=num
print(numbers_sum)