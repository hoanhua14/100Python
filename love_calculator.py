print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
names = name1 + name2
true_set = set("TRUE")
love_set = set("LOVE")
true_count = 0
love_count = 0
for char in names:
  if char.upper() in true_set:
    true_count += 1
  if char.upper() in love_set:
    love_count += 1

count = str(true_count) + str(love_count)
count = int(count)

if count < 10 or count> 90:
  print(f'Your score is {count}, you go together like coke and mentos.')
elif count > 40 and count < 50:
  print(f'Your score is {count}, you are alright together.')
else:
  print(f'Your score is {count}.')
