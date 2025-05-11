import multiprocessing
import time

def do_something():
    print("Sleeping 2 second(s)...")
    time.sleep(2)
    print('Done Sleeping..')
    
if __name__ ==  '__main__':
    
    start = time.perf_counter()

    p1= multiprocessing.Process(target=do_something)
    p2= multiprocessing.Process(target=do_something)

    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    # p1.join() waits for p1 to finish before moving on to the next line


    end=time.perf_counter()

    print(f'Finished in {round(end-start, 2)} second(s)')