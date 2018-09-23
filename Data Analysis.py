from datetime import datetime
import os

with open((os.path.join('Time Manager.txt')), 'r') as f:
    lines = f.readlines() #lines 是一个list，list的每个元素是f中的一行
line_list = []
for line in lines:
    line_list.append(line.split(" >> "))
i=0
right_combination = []
while i <= len(line_list)-2:
    event_line = line_list[i]
    duration_line = line_list[i+1]
    event_name = event_line[0]
    event_duration = duration_line[2]
    i+=1
    combination_element = event_name+event_duration
    right_combination.append(combination_element)

str_right_combination = "".join(sorted(right_combination))
list_right_combination = str_right_combination.split(',')

# change days into seconds
i=0
keyword = 'day'
for list_right_combination_element in list_right_combination:
    if (keyword in list_right_combination[i]):
        list_right_combination[i] = int(list_right_combination[i].strip(' days'))*24*3600
    if i > len(list_right_combination):
        break
    i=i+1

# change hours into seconds
i=0
keyword = ':'
for list_right_combination_element in list_right_combination:
    if (keyword in str(list_right_combination[i])):
        list_right_combination[i] = list_right_combination[i].split(':')
        hours_into_seconds = int(list_right_combination[i][0])*3600
        minutes_into_seconds = int(list_right_combination[i][1])*60
        seconds_into_seconds = int(list_right_combination[i][2])*1
        list_right_combination[i] = hours_into_seconds+minutes_into_seconds+seconds_into_seconds
    if i > len(list_right_combination):
        break
    i=i+1


# seconds+seconds

for i in range(len(list_right_combination)-1):
    
    if type(list_right_combination[i]) == type(list_right_combination[i+1]):
        list_right_combination[i] = list_right_combination[i+1]+list_right_combination[i]
        list_right_combination[i+1] = ''
    

while '' in list_right_combination:
    list_right_combination.remove('')


    






