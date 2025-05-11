import concurrent.futures
import time

start = time.perf_counter()


def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    return f'Done Sleeping...{seconds}'

# Method 1: Using ThreadPoolExecutor

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     t1=executor.submit(do_something, 1)
#     t2=executor.submit(do_something, 1)
    
#     t1.result()
#     t2.result()



# with concurrent.futures.ThreadPoolExecutor() as executor:
    
#     secs = [5, 4, 3, 2, 1]

#     results=[executor.submit(do_something, sec) for sec in secs]
    
#     for result in concurrent.futures.as_completed(results):
#         print(result.result())

# Method 2: Using map


with concurrent.futures.ThreadPoolExecutor() as executor:

    secs = [5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)

    for result in results:
        print(result)


finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} second(s)')
