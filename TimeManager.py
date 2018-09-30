# READ ME #

# 1. enter anything you want to record your events #

# 2. ensure all the same events have a same name, or their time cannot be added #

# 3. enter "sleep" to record your sleep time #

# 4. the end of event "sleep" is the start of a new day #

# 5. enter "summary" to check all things you've recorded #

# 6. enter "summarytoday" to check all things you've recorded today #


from datetime import datetime
import os
import time
import math

def EventInput():
    current_time = datetime.now()
    f.write(input_event+', >> ')
    f.write(current_time.strftime("%Y-%m-%d %H:%M:%S")+' >> ')
    f.close()
    
def EventInputToday():
    if input_event == 'sleep':
        g.seek(0)
        g.truncate()
    else:
        current_time = datetime.now()
        g.write(input_event+', >> ')
        g.write(current_time.strftime("%Y-%m-%d %H:%M:%S")+' >> ')
    g.close()


def TimeCalc():
    if os.path.isfile('Update.txt'):
        current_time = datetime.now()
        f = open('Update.txt','r')
        oldtime_str = f.read()
        newtime = datetime.strptime(current_time.strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")
        oldtime = datetime.strptime(oldtime_str,"%Y-%m-%d %H:%M:%S")   
        print('last event duration is: ')
        print(newtime-oldtime)
        f.close()

        f = open('DataBase.txt','a')
        f.write(str(newtime-oldtime)+','+' >> ')
        f.close()
    f = open('DataBase.txt','a')
    f.write('\n')
    f.close()

def TimeCalcToday():
    if input_event == 'sleep':
        g = open('DataBaseToday.txt','a')
        g.seek(0)
        g.truncate()
    else:
        if os.path.isfile('UpdateToday.txt'):
            current_time = datetime.now()
            f = open('UpdateToday.txt','r')
            oldtime_str = f.read()
            newtime = datetime.strptime(current_time.strftime("%Y-%m-%d %H:%M:%S"),"%Y-%m-%d %H:%M:%S")
            oldtime = datetime.strptime(oldtime_str,"%Y-%m-%d %H:%M:%S")   
            f.close()

            f = open('DataBaseToday.txt','a')
            f.write(str(newtime-oldtime)+','+' >> ')
            f.close()
        f = open('DataBaseToday.txt','a')
        f.write('\n')
        f.close()
    

def Update():
    current_time = datetime.now()
    f = open('Update.txt','w')
    f.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))
    f.close()

def UpdateToday():
    current_time = datetime.now()
    f = open('UpdateToday.txt','w')
    f.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))
    f.close()

def AddTimeUp():
    with open((os.path.join('DataBase.txt')), 'r') as f:
        lines = f.readlines() 
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


    # turn list into dictionary

    keyslist_in_dictionary = []
    i=0
    for list_right_combination_elements in list_right_combination:
        if i%2 ==0:
            keyslist_in_dictionary.append(list_right_combination[i])
            i=i+2
        if i > len(list_right_combination)-1:
            break

    valueslist_in_dictionary = []
    i=1
    for list_right_combination_elements in list_right_combination:
        if i%2 !=0:
            valueslist_in_dictionary.append(list_right_combination[i])
            i=i+2
        if i > len(list_right_combination):
            break

    dictionary_list = []
    for sequential_number in range(len(keyslist_in_dictionary)):
        keys = keyslist_in_dictionary[sequential_number]
        values = valueslist_in_dictionary[sequential_number]
        dictionary_list.append(dict(zip([keys],[values])))

    final_dictionary = {}
    from collections import Counter
    for dicts in dictionary_list:
        final_dictionary = dict(Counter(final_dictionary)+Counter(dicts))
    return final_dictionary


def AddTimeUpToday():
    with open((os.path.join('DataBaseToday.txt')), 'r') as g:
        lines = g.readlines() 
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




    # turn list into dictionary

    keyslist_in_dictionary = []
    i=0
    for list_right_combination_elements in list_right_combination:
        if i%2 ==0:
            keyslist_in_dictionary.append(list_right_combination[i])
            i=i+2
        if i > len(list_right_combination)-1:
            break

    valueslist_in_dictionary = []
    i=1
    for list_right_combination_elements in list_right_combination:
        if i%2 !=0:
            valueslist_in_dictionary.append(list_right_combination[i])
            i=i+2
        if i > len(list_right_combination):
            break

    dictionary_list = []
    for sequential_number in range(len(keyslist_in_dictionary)):
        keys = keyslist_in_dictionary[sequential_number]
        values = valueslist_in_dictionary[sequential_number]
        dictionary_list.append(dict(zip([keys],[values])))

    final_dictionary = {}
    from collections import Counter
    for dicts in dictionary_list:
        final_dictionary = dict(Counter(final_dictionary)+Counter(dicts))
    return final_dictionary



def changeTime(allTime):
    day = 24*60*60
    hour = 60*60
    min = 60
    if allTime <60:        
        return  "%d sec"%math.ceil(allTime)
    elif  allTime > day:
        days = divmod(allTime,day) 
        return "%d days, %s"%(int(days[0]),changeTime(days[1]))
    elif allTime > hour:
        hours = divmod(allTime,hour)
        return '%d hours, %s'%(int(hours[0]),changeTime(hours[1]))
    else:
        mins = divmod(allTime,min)
        return "%d mins, %d sec"%(int(mins[0]),math.ceil(mins[1]))
 
 


    
if __name__ == '__main__':
    f = open('DataBase.txt','a')
    input_event = input('enter an event you\'re about to do\n')

    g = open('DataBaseToday.txt','a')


    if input_event == 'summary':
        add_time_up = AddTimeUp()
        final_events_list = list(add_time_up.keys())
        final_time_list = list(add_time_up.values())
        for i in range(len(final_time_list)):
            final_time_list[i] = changeTime(final_time_list[i])
     
        for i in range(len(final_time_list)):
            print(final_events_list[i]+':')
            print(final_time_list[i])

            
    elif input_event == 'summarytoday':
        add_time_up = AddTimeUpToday()
        final_events_list = list(add_time_up.keys())
        final_time_list = list(add_time_up.values())
        for i in range(len(final_time_list)):
            final_time_list[i] = changeTime(final_time_list[i])
     
        for i in range(len(final_time_list)):
            print(final_events_list[i]+':')
            print(final_time_list[i])
            

    elif input_event.find('>>') ==1:
        print ('input error, string\">>\"cannot be included')
        
    else:
        EventInput()
        EventInputToday()
        TimeCalc()
        TimeCalcToday()
        Update()
        UpdateToday()
    

