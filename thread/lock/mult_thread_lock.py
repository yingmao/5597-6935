import threading

# global variable
VALUE = 0

# 1.def a lock：
mutex = threading.Lock()


# define the adder
def add_value():
    global VALUE
    # 2. add lock
    mutex.acquire()
    for x in range(1000000):
        VALUE += 1
    # 3. release lock
    mutex.release()
    print('value = ', VALUE)


# two threads for the adder
def add_thread_main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()


if __name__ == '__main__':
    add_thread_main()
