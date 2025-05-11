import threading
import time

start = time.perf_counter()

def do_something():
    print("Sleeping 2 second(s)...")
    time.sleep(2)
    print('Done Sleeping..')

t1= threading.Thread(target=do_something)
t2= threading.Thread(target=do_something)

t1.start()
t2.start()

#thread went to sleep and moved into the next step to calculate the time

t1.join()
t2.join()
# wait for the threads to finish
end=time.perf_counter()

print(f'Finished in {round(end-start, 2)} second(s)')