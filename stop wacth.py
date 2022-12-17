import time
while True:
     def time_convert(sec):
       mins = sec // 60
       sec = sec % 60
       hour = mins // 60
       mins = mins % 60
       print("Time Lapsed = hour:{0} min:{1} sec:{2}".format(int(hour),int(mins),sec))

     input("Press Enter to start")
     start_time = time.time()

     input("Press Enter to stop")
     end_time = time.time()

     time_lapsed = end_time - start_time
     time_convert(time_lapsed)