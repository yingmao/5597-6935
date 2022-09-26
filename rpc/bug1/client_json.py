import json

class RPCProxy:
    def __init__(self, connection):
        # 需要与server建立连接
        self._connection = connection
    def __getattr__(self, name):
        # 连接server，发送client调用的func name
        def do_rpc(*args, **kwargs):
            self._connection.send(json.dumps((name, args, kwargs)))
            result = json.loads(self._connection.recv())
            return result
        return do_rpc

from multiprocessing.connection import Client
c = Client(('localhost', 17000), authkey=b'peekaboo')
proxy = RPCProxy(c)
print(proxy.add(2, 3))
print(proxy.sub(2, 3))
# bug : 在server端注册过的func才能调用
# print(proxy.add1(4, 5))
