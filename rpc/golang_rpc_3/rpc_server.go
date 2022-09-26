package main

import (
        "log"
	"net"
        "net/rpc"
)

type HelloService struct {}

// rpc func
func (p *HelloService) Hello(request string, reply *string) error {
    *reply = "Hello from Server:" + request
    return nil
}


func main() {
    rpc.RegisterName("HelloService", new(HelloService))

    listener, err := net.Listen("tcp", ":1234")
    if err != nil {
        log.Fatal("ListenTCP error:", err)
    }

    conn, err := listener.Accept()
    if err != nil {
        log.Fatal("Accept error:", err)
    }

    rpc.ServeConn(conn)
}
