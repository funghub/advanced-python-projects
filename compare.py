'''
Write a program that indicates how many times out of a thousand the Monte Carlo method is faster 
than the Leibniz formula at converging to pi, plus or minus one one-thousandth.
'''

# the program runs the Leibniz and Monte Carlo methods until they get the right answer and compares the times it takes for them to get the answer

'''
LEIBNIZ
'''
def program_1():

  def leibniz():
    count = 0
    estimate = 0
    while True:  # use while True: for an infinite generator with next()
      iteration = ((-1)**count) / (2*count + 1)
      estimate += iteration
      yield estimate * 4
      '''
      (yield allows the generator to remember this output for the next iteration,
      but not necessarily return it or remember the other previous iterations)
      '''
      count += 1

  def iterate():
      pi_estimation = leibniz()  # instantiate the generator
      '''
      (this creates the generator and must be before the loop or
      else we would make a new generator each loop)
      '''
      estimation = 0  # estmation of pi

      while estimation < 3.140 or estimation > 3.142:  # if the estimation is in range, we will stop the generation
          estimation = next(pi_estimation)   # call generator repeatedly with next()

      return estimation

  numbers_list = iterate()


'''
MONTE CARLO
'''

def program_2():

  import random

  in_circle = 0  # points inside the circle
  total_points = 0  # total points inside the circle and in the square
  estimation = 0  # estimation of pi

  while estimation < 3.140 or estimation > 3.142:
    # x and y pair generated at random between -1 and 1
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    r_squared = x**2 + y**2  # formula to test if point is inside the circle

    if r_squared <= 1:  # if the point is inside the circle
      in_circle += 1

    total_points += 1  # counter for all points 
    estimation = (in_circle/total_points) * 4  # estimation of pi from the Monte Carlo method


'''
TIMER to compare the time performance of the Leibniz formula vs Monte Carlo
'''

def timer():
   
    import time
    start_1 = time.perf_counter()
    program_1()
    end_1 = time.perf_counter()
    duration_1 = end_1 - start_1
    # print(f'Leibniz program time is {end_1 - start_1}')

    start_2 = time.perf_counter()
    program_2()
    end_2 = time.perf_counter()
    duration_2 = end_2 - start_2
    # print(f'Monte Carlo program time is {end_2 - start_2}')

    if duration_1 > duration_2:  # counting the times Monte Carlo is faster
       return 1
    else:
       return 0

# run it a thousand times and count how many times the Monte Carlo is faster than Leibniz
print('The number of times out of a thousand the Monte Carlo method is faster than the Leibniz formula at converging to pi is', sum([timer() for x in range(1000)]), 'out of 1000 times.')