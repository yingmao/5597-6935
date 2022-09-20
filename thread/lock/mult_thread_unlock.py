import threading

# global variable
VALUE = 0


# adder
def add_value():
    global VALUE
    for x in range(1000000):
        VALUE += 1
    print('value = ', VALUE)


def add_thread_main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()


if __name__ == '__main__':
    add_thread_main()
