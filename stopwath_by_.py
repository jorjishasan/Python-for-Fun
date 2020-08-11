
import time as t

print("press ENTER to start the stopwatch \nand, press CTRL + C to stop the stopwatch ")

while True:
    try:
        input()
        start_ =t.time()
        print('stopwatch started..')

    except KeyboardInterrupt:
        print('Stopwatch stopped..')
        end_time =t.time()
        print("The total time: ", round(end_time-start_ , 2), "seconds")
        break
