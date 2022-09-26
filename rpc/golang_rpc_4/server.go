package main

import "net/rpc"

type PutArgs struct {
Key string
Value string
}

type PutReply struct {
Err Err
}

type KV struct {
mu sync.Mutex
keyvalue map[string]string
}

func (kv *KV) Put(args *PutArgs, reply *PutReply) error {
kv.mu.Lock()
defer kv.mu.Unlock()
kv.keyvalue[args.Key] = args.Value
reply.Err = OK
return nil
}


func startServer() {
rpcs := rpc.NewServer()
kv := KV{keyvalue: make(map[string]string)}
rpcs.Register(&kv)
l, e := net.Listen("tcp", ":8888")
go func() {
for {
conn, err := l.Accept()
if err == nil {
go rpcs.ServeConn(conn)
} else {
break
}
}
l.close()
}()
}

func main() {
startServer()
client := NewKVClient()
client.Put("nyu", "New York University")
client.Put("cmu", "Carnegie Mellon University")
fmt.Printf("Get value=%s\n", client.Get("nyu"))
}
