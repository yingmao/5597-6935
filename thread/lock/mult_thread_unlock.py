import threading

# 定义全局变量VALUE
VALUE = 0


# 定义加法线程函数
def add_value():
    global VALUE
    for x in range(1000000):
        VALUE += 1
    print('value = ', VALUE)


# 定义两个线程并发执行加法操作
def add_thread_main():
    for x in range(2):
        t = threading.Thread(target=add_value)
        t.start()


if __name__ == '__main__':
    add_thread_main()
