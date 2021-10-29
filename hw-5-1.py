# Author Ypngdong Xi (Oct 22 2021)

import random
# Question 1
print(random.randrange(30, 50, 1))

# Question 2
print(random.randrange(2, 75, 2))

# Question 3
print(random.randint(20, 30))

# Question 4
print(random.randint(1, 8))

# Question 5
print(random.randint(1, 20))

# Question 6
seq = 'cat', 'dog', 'sheep', 'cow', 'chicken', 'pig'
print(random.choice(seq))

# Question 7
population = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(random.choices(population, k=4))

# Question 8
population2 = [1, 2, 3, 4, 5]
print(random.sample(population2, k=5))

# Question 9
cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
card = random.choice(cards)
print("the card you drawed was", card)

# Question 10
random.seed(1942)
print(random.randint(1, 1000))
