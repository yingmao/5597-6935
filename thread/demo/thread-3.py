import time
import threading


def do_waiting(arg):
    print(str(arg) + ' start waiting.')
    time.sleep(3)
    print(str(arg) + ' stop waiting.')


if __name__ == '__main__':
    print('main thread start...')
    for i in range(10):
        # instance Thread
        t = threading.Thread(target=do_waiting, args=(i,))
        t.start()
