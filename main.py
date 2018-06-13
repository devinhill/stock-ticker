import urllib2

contents = urllib2.urlopen("https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=TSLA&interval=1min&datatype=csv&apikey=FJ7RN88ULNU2K7TQ").read()
lines = contents.split("\r\n")
most_recent = lines[1]
items = most_recent.split(",")
close_price = items[4]

print(close_price)
