'''
Write a program that uses the ansiplot library to 
display a histogram showing the distribution of 1000 random numbers
'''

import ansiplot
import random

# create 100 random numbers
rand_nums = [random.randint(0,1000) for x in range(1001)]

# round the random numbers so we get 10 categories of step 100
rounded_num = [(num // 100)*100 for num in rand_nums]



# counter_dict = {}
# for unit in range(0,1100,100):
#         counter_dict[unit] = rounded_num.count(unit)




x = list(range(0,1100,100))
y = [rounded_num.count(unit) for unit in range(0,1100,100)]

# print(x)
# print(y)
# print(counter_dict)
canvas = ansiplot.Scaled(40, 10, palette=ansiplot.palette.Pretty)
canvas.plot(x, y, title="count of random number every 100")
canvas.show()

###################################33

import ansiplot
import random

# create 1000 random numbers
rand_nums = [random.randint(0,999) for x in range(1000)]

# floor division the random numbers so we can sort 10 intervals
rounded_num = [(num // 100)*100 for num in rand_nums]

# make a dicitonary of the counts of every 100 intervals
counter_dict = {}
for unit in range(0,1000,100): # get 0-199 intervals with 100 steps
        counter_dict[f'{unit}-{unit+99}'] = rounded_num.count(unit)

# plot the bar graph
canvas = ansiplot.Scaled(40, 10, axis=False)
for pos, (key, value) in enumerate(counter_dict.items()):
    canvas.bar(pos, value, title=key)
canvas.show()