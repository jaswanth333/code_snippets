import threading
import time

start = time.perf_counter()

def do_something(secs):
    print(f"Sleeping {secs} second(s)...")
    time.sleep(secs)
    print('Done Sleeping..')
    
threads = []
# Create 10 threads

for _ in range(10):
    t = threading.Thread(target=do_something, args=[1.65])
    t.start()
    threads.append(t)

for thread in threads:
    thread.join()
# wait for the threads to finish

end=time.perf_counter()

print(f'Finished in {round(end-start, 2)} second(s)')