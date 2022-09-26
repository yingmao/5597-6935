package main
import "net/rpc"

type KVClient struct {
clt *rpc.Client
}


func NewKVClient() *KVClient {
clt, err := rpc.Dial("tcp", ":8888")
return &KVClient{clt: clt}
}


func (c *KVClient) Put(key string, value string) {
args := &PutArgs{Key: key, Value: val}
reply := PutReply{}
err := c.clt.call("KV.Put", args, &reply)
}


func main() {

client := NewKVClient()
client.Put("nyu", "New York University")
client.Put("cmu", "Carnegie Mellon University")
fmt.Printf("Get value=%s\n", client.Get("nyu"))
}
