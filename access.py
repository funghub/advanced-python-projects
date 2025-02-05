'''
demonstrates a generator yielding the number of accesses 
made in each hour, from the beginning of /etc/httpd/logs/access_log
'''

'''file looks like:
66.102.7.103 - - [03/Aug/2023:11:06:26 -0700] "HEAD /~dputnam/blog/atom.xml HTTP/1.1" 302 - "-" "FeedBurner/1.0 (http://www.FeedBurner.com)"
162.222.203.162 - - [03/Aug/2023:11:31:22 -0700] "GET /.env HTTP/1.1" 302 211 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0"
18.203.145.25 - - [03/Aug/2023:11:36:47 -0700] "GET /robots.txt HTTP/1.0" 302 217 "http://hills.ccsf.edu/~lug/index.html" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko)$
140.228.21.43 - - [03/Aug/2023:11:38:34 -0700] "GET /wp-login.php HTTP/1.1" 302 219 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
69.171.231.10 - - [03/Aug/2023:11:57:27 -0700] "GET / HTTP/1.1" 302 207 "-" "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
69.171.231.119 - - [03/Aug/2023:11:57:27 -0700] "GET / HTTP/1.1" 302 207 "-" "facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)"
66.102.7.104 - - [03/Aug/2023:11:58:53 -0700] "HEAD /~dputnam/blog/atom.xml HTTP/1.1" 302 - "-" "FeedBurner/1.0 (http://www.FeedBurner.com)"
57.128.68.71 - - [03/Aug/2023:12:02:13 -0700] "GET /~cholder/mmsp120/index.html HTTP/1.1" 302 234 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/5$67.164.53.77 - - [03/Aug/2023:12:32:57 -0700] "GET /mail HTTP/1.1" 302 211 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko)"
67.164.53.77 - - [03/Aug/2023:12:32:57 -0700] "GET /mail HTTP/1.1" 302 211 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 16_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.4 Mobile/15E148 Safari$
66.102.7.105 - - [03/Aug/2023:12:48:56 -0700] "HEAD /~dputnam/blog/atom.xml HTTP/1.1" 302 - "-" "FeedBurner/1.0 (http://www.FeedBurner.com)"                                                                      96.18.24.38 - - [03/Aug/2023:12:57:53 -0700] "GET / HTTP/1.1" 302 207 "-" "Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.$74.125.214.43 - - [03/Aug/2023:13:28:20 -0700] "HEAD /~dputnam/blog/atom.xml HTTP/1.1" 302 - "-" "FeedBurner/1.0 (http://www.FeedBurner.com)"                                                                     47.128.31.49 - - [03/Aug/2023:14:15:08 -0700] "GET /robots.txt HTTP/1.1" 302 217 "-" "Mozilla/5.0 (Linux; Android 5.0) AppleWebKit/537.36 (KHTML, like Gecko) Mobile Safari/537.36 (compatible; Bytespider; spide$74.125.214.43 - - [03/Aug/2023:14:27:04 -0700] "HEAD /~dputnam/blog/atom.xml HTTP/1.1" 302 - "-" "FeedBurner/1.0 (http://www.FeedBurner.com)"
60.217.75.70 - - [03/Aug/2023:14:30:32 -0700] "GET / HTTP/1.1" 302 207 "-" "Mozilla/5.0"                                                                                                                          122.58.150.172 - - [03/Aug/2023:14:38:46 -0700] "GET /robots.txt HTTP/1.1" 302 217 "-" "Mozilla/5.0 (Linux; Android 8.0; Pixel 2 Build/OPD3.170816.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.7986.1$60.217.75.70 - - [03/Aug/2023:14:42:38 -0700] "GET / HTTP/1.1" 302 207 "-" "Mozilla/5.0"                                                                                                                          13.57.37.146 - - [03/Aug/2023:14:45:35 -0700] "GET / HTTP/1.1" 302 207 "-" "\\\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15\\\""
13.57.37.146 - - [03/Aug/2023:14:46:24 -0700] "GET / HTTP/1.1" 302 207 "-" "\\\"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15\\\""
199.47.82.21 - - [03/Aug/2023:15:23:36 -0700] "GET /robots.txt HTTP/1.1" 302 217 "-" "Turnitin (https://bit.ly/2UvnfoQ)"
199.47.82.21 - - [03/Aug/2023:15:23:36 -0700] "GET /~cfan02/135b/hw02.html HTTP/1.1" 302 229 "-" "Turnitin (https://bit.ly/2UvnfoQ)"                                                                              199.47.82.21 - - [03/Aug/2023:15:23:36 -0700] "GET /~cfan02/135b/hw10.shtml HTTP/1.1" 302 230 "-" "Turnitin (https://bit.ly/2UvnfoQ)"                                                                             199.47.82.21 - - [03/Aug/2023:15:23:37 -0700] "GET /~dbong01/hw2.html HTTP/1.1" 302 224 "-" "Turnitin (https://bit.ly/2UvnfoQ)"
199.47.82.21 - - [03/Aug/2023:15:23:37 -0700] "GET /~ddenni01/hw2.html HTTP/1.1" 302 225 "-" "Turnitin (https://bit.ly/2UvnfoQ)"
'''

path = '/etc/httpd/logs/access_log'
import re
import itertools

# open the file in read mode and enter the lines into a list
with open(path, 'r') as reader:
    log = list(map(lambda x: x.strip(), reader.readlines())) # place the logs in the lines into a list stored as log

# find the timestamps in each line and place them into a list
timestamp = list(itertools.chain(*[re.findall('\[\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2}', item) for item in log]))
    # example use re. to match '[02/Sep/2023:13:44:26'

from datetime import datetime

# create a generator that will extract the timestamps into the ISO datetime format
    # example 2023-08-03 11:06:26
def access_log(timestamp):
    for stamp in timestamp:
        time = datetime.strptime(stamp, '[%d/%b/%Y:%H:%M:%S')
        yield time

generator = access_log(timestamp) # instantiate the generator
dic_logs = {}  # {date: {time: number of logs, time: number of logs}}

for x in range(len(timestamp)):  # iterate the entire length of the number of accesses
        iter_stamp = next(generator)
        date = iter_stamp.date().strftime('%d-%b-%Y')  # set the date for the dictionary
        hour = iter_stamp.hour  # set the hour for the dictionary

        # if the date is not already in the dictionary, it will be created
        if date not in dic_logs:
            dic_logs[date] = {}

        # if the hour is not already under the date, it will be created and count the log as 1
        if hour not in dic_logs[date]:
            dic_logs[date][hour] = 1
        else:
            dic_logs[date][hour] += 1  
            # add one to the count if there is already the date and hour in the dictionary

print(dic_logs) # print the dictionary of the number of accesses made in each hour
# index: {'date': {hour: number of logs, ...}}
