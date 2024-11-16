import time


def main():
    program_types=['clock','timedown']
    print("the program types are : \n")
    for i in program_types:
            print(f"- {i}\n")
    while True:
        program_type = input('what program type do you want ? ')
        print()
        if program_type.lower() == 'clock':
            while True:
                print('\n'*30)
                current_clock = time.localtime()
                time_by_min = f'0{current_clock.tm_min}'
                if current_clock.tm_hour == 0 :
                   current_clock.tm_hour = current_clock.tm_hour + 12 
                print(f"The current clock is {current_clock.tm_hour-12}:{current_clock.tm_min}:{current_clock.tm_sec}")
                print(f"The current date is {current_clock.tm_year}:{current_clock.tm_mon}:{current_clock.tm_mday}")
                time.sleep(1)
        elif program_type.lower()== 'timedown':
            while True: 
                try:
                    stop_watch_time = int(input('how much time do you want to add ( with secconds ): '))
                    while True:
                        if stop_watch_time == 0:
                            print('\nDone!\n')
                            break
                        print('\n'*50)
                        stop_watch_time = stop_watch_time - 1
                        print(stop_watch_time)
                        time.sleep(1)
                        
                except:
                    print("input error , please write only numbers")
        else :
            print('incorrect choice , please choose between :\n')
            for i in program_types:
                print(f"- {i}\n")

main()