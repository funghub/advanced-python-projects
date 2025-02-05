'''
Program that expects as argument the path to a 
greyscale ASCII PGM file, and prints out a sixteeen-bucket 
histogram counting the pixels at each level of grey
'''

import sys, re

with open(sys.argv[1]) as content:
    # split at white spaces into list, then recognize comments and replace with newline
    parts = re.split(r'\s+',re.sub(r'#.*',r'\n',content.read()))
    x_dim, y_dim, depth = int(parts[1]), int(parts[2]), int(parts[3])  # put dimensions and grayscale depth
    pixels = [int(n) for n in parts[4:] if n] # filter out FALSE evaluated strings with if n
    try:
        assert len(pixels) == x_dim * y_dim  # make sure dimentions match to the expected number of pixels
    except AssertionError:
        print('Number of pixels does not match the expected dimensions')

# create the buckets
bucket = depth / 16
bucs = [round(bucket*x,1) for x in range(17)]  # list of intervals for 16 buckets
# print(bucs)

# create the ranges for the buckets
buckets = [f'{bucs[x]} - <{bucs[x+1]}' for x in range(len(bucs)-2)]
buckets.append(f'{bucs[len(bucs) - 2]} - {bucs[len(bucs) - 1]}')  # add in the range for the last bucket
# print(buckets)

buckets_dict = dict.fromkeys(buckets, 0)  # create dictionary with the intervals
# print(buckets_dict)

for gray in pixels:
    for i in range(len(bucs) - 1):  # len is 17 and - 1 is 16, so only evaluate 0-15
        if gray >= bucs[i] and gray < bucs[i+1]:
            buckets_dict[buckets[i]] += 1
        elif gray >= bucs[i] and gray <= bucs[i+1] and i == (len(bucs)-2):  # for the last range of the 16 buckets
            buckets_dict[buckets[i]] += 1

# print(buckets_dict)  # this prints the results of counting the pixels at each level of grey


buckets_dict_max = max(buckets_dict.values())  # find the max count inside the dictionary
# print(buckets_dict_max)

# create the histogram
for key, value in buckets_dict.items():
    print(f'{key:16}' + ':', '=' * int(60*(value/buckets_dict_max)))
