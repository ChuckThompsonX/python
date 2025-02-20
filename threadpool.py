import concurrent.futures

# thread pool to run two worker tasks concurrently
# main thread waits for the worker threads to finish via shutdown call 

def worker_thread():
    print("This is a worker thread.")

# set up thread pool
thread_pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

thread_pool.submit(worker_thread)
thread_pool.submit(worker_thread)

# shutdown thead pool
thread_pool.shutdown(wait=True)

print("Main thread continues to run.")
