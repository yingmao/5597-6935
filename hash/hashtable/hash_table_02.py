

class StorageNode:
    def __init__(self, name=None, host=None):
        self.name = name
        self.host = host

    def fetch_file(self, path):
        print(f'get {path} from {self.name}:{self.host} storage node')

    def put_file(self, path):
        print(f'put {path} in {self.name}:{self.host} storage node')


# storage_nodes holding instances of actual storage node objects
storage_nodes = [
    StorageNode(name='A', host='239.67.52.72'),
    StorageNode(name='B', host='137.70.131.229'),
    StorageNode(name='C', host='98.5.87.182'),
    StorageNode(name='D', host='11.225.158.95'),
    StorageNode(name='E', host='203.187.116.210'),
]


def hash_fn(key):
    """The function sums the bytes present in the `key` and then
    take a mod with 5. This hash function thus generates output
    in the range [0, 4].
    """
    # if nodes change 7, 5 -> 7
    return sum(bytearray(key.encode('utf-8'))) % 5


def upload(path):
    # we use the hash function to get the index of the storage node
    # that would hold the file
    index = hash_fn(path)

    # we get the StorageNode instance
    node = storage_nodes[index]

    # we put the file on the node and return
    return node.put_file(path)


def fetch(path):
    # we use the hash function to get the index of the storage node
    # that would hold the file
    index = hash_fn(path)

    # we get the StorageNode instance
    node = storage_nodes[index]

    # we fetch the file from the node and return
    return node.fetch_file(path)


# for file in ['f1.txt', 'f2.txt', 'f3.txt', 'f4.txt', 'f5.txt']:
#     print(f"file {file} resides on node {storage_nodes[hash_fn(file)].name}")
#
# fetch('f1.txt')

# add another 2 nodes, what will happen???
# node1 = StorageNode(name='F', host='107.117.238.203')
# node2 = StorageNode(name='G', host='27.161.219.131')
# storage_nodes.append(node1)
# storage_nodes.append(node2)
# # bug : hash_fn should change 7
# for file in ['f1.txt', 'f2.txt', 'f3.txt', 'f4.txt', 'f5.txt']:
#     print(f"file {file} resides on node {storage_nodes[hash_fn(file)].name}")
#
# fetch('f1.txt')
