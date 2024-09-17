import csv
import datetime as dt

with open('hacker_news.csv', 'r') as read_obj: # read the file as a list of lists
    csv_reader = csv.reader(read_obj) # pass the file object to reader to get the reader object
    hn_list = list(csv_reader) # pass reader object to list() to get a list of lists

headers = [hn_list[0]] #creating new headers list
hn_list.pop(0) # removing headers from original list

ask_posts = []
show_posts = []
other_posts = []

for row in hn_list:
    title = row[1] #setting title to a variable to separate posts into 3 categories
    if title.lower().startswith('ask hn'):
        ask_posts.append(row)
    elif title.lower().startswith('show hn'):
        show_posts.append(row)
    else:
        other_posts.append(row)

total_ask_comments = 0

for row in ask_posts:
    total_ask_comments = total_ask_comments + int(row[4])

avg_ask_comments = total_ask_comments / int(len(ask_posts))

total_show_comments = 0

for row in show_posts:
    total_show_comments = total_show_comments + int(row[4])

avg_show_comments = total_show_comments / int(len(show_posts))

#Calculate the number of ask posts created in each hour of the day, along with the number of comments received.
#Calculate the average number of comments ask posts receive by hour created.

result_list = []

for row in ask_posts:
    result = [row[6], str(row[4])]
    result_list.append(result)

counts_by_hour = {}
comments_by_hour = {}

print(result_list)
for row in result_list:
    date = dt.datetime.strptime(str(row[0]), "%m/%d/%Y %H:%M")
    hour = dt.datetime.strftime(date, "%H")

    if hour not in counts_by_hour:
        counts_by_hour[hour] = 1
        comments_by_hour[hour] = int(row[1])
    else:
        counts_by_hour[hour] += 1
        comments_by_hour[hour] += int(row[1])

print(counts_by_hour.items())
avg_by_hour = []

for comment in comments_by_hour:
    avg_by_hour.append([comment, comments_by_hour[comment]/ counts_by_hour[comment]])

swap_avg_by_hour = []

for row in avg_by_hour:
    temp = [row[1], row[0]]
    swap_avg_by_hour.append(temp)

sorted_swap = sorted(swap_avg_by_hour, reverse=True)

print("Top 5 Hours for Ask Posts Comments")

for row in sorted_swap[:5]:
    hour = dt.datetime.strptime(row[1], "%H")
    hour = hour.strftime("%H:%M")
    avg = "{:.2f}".format(row[0])
    print(hour + ": " + avg + " average comments per post")


