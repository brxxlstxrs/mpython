import random

n = int(input())
nums = random.sample(range(*map(int, input().split())), n)
names = random.sample(input().split('; '), n)
profit_rng =

