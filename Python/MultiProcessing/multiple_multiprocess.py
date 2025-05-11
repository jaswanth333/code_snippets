import multiprocessing
import time
import concurrent.futures

def do_something(secs):
    print(f"Sleeping {secs} second(s)...")
    time.sleep(secs)
    return f'Done Sleeping {secs}..'
    
if __name__ ==  '__main__':
    
    start = time.perf_counter()
    
    # secs=[5,4,3,2,1]
    
    # processes=[multiprocessing.Process(target=do_something, args=[sec]) for sec in secs]

    # for process in processes:
    #     process.start()
    #     process.join()
        
    with concurrent.futures.ProcessPoolExecutor() as executor:
        secs=[5,4,3,2,1]
        results=executor.map(do_something, secs)
        for result in results:
            print(result)  

        


    end=time.perf_counter()

    print(f'Finished in {round(end-start, 2)} second(s)')