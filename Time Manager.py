from datetime import datetime
import os


def EventInput():
    f = open('Time Manager.txt','a')
    input_event = input('enter an event you\'re about to do\n')

    current_time = datetime.now()
    f.write(input_event+'\n')
    f.write(current_time.strftime("%Y-%m-%d %H:%M:%S")+'\n')
    f.close()

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

        f = open('Time Manager.txt','a')
        f.write('LastEventDuration is '+str(newtime-oldtime)+'\n\n')
        f.close()

def Update():
    current_time = datetime.now()
    f = open('Update.txt','w')
    f.write(current_time.strftime("%Y-%m-%d %H:%M:%S"))
    f.close()

if __name__ == '__main__':
    EventInput()
    TimeCalc()
    Update()
    
