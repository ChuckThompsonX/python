import threading
import os, time

# run two tasks concurrently

def task_one():
    id = os.getpid()
    name = threading.current_thread().name
    print("Task one assigned to thread: {}".format(name))
    print("ID for task 1: {}".format(id))
    time.sleep(2)
    print(f"Thread {name}: finishing")

def task_two():
    id = os.getpid()
    name = threading.current_thread().name
    print("Task two assigned to thread: {}".format(name))
    print("ID for task 2: {}".format(id))
    time.sleep(2)
    print(f"Thread {name}: finishing")

if __name__ == "__main__":
    # main thread
    id = os.getpid()
    name = threading.current_thread().name
    print("Main thread name: {}".format(name))
    print("ID for main program: {}".format(id))

    # create two threads
    t1 = threading.Thread(target=task_one, name='t1')
    t2 = threading.Thread(target=task_two, name='t2')

    # start the threads
    t1.start()
    t2.start()

    # end threads
    print("Main thread: waiting for threads to complete")
    t1.join()
    t2.join()
    print("Main thread: all threads completed")
