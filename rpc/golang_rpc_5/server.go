package main

import (
        "fmt"
	"net"
	"net/rpc"
	"net/rpc/jsonrpc"
)

type Student struct {
        FirstName, LastName string
}

// rpc func
func (p *Student) Say(payload Student, reply *Student) error {
    fmt.Println("hello: " + payload.FirstName + " " + payload.LastName)
    *reply = payload
    return nil
}


func main() {

	// create a `*Student` object
	mit := new(Student)

	// create a custom RPC server
	server := rpc.NewServer()

	// register `mit` object with `server`
	server.Register(mit)

	// create a TCP listener at address : 127.0.0.1:9002
	// https://golang.org/pkg/net/#Listener
	listener, _ := net.Listen("tcp", "127.0.0.1:9002")

	for {

		// get connection from the listener when client connects
		conn, _ := listener.Accept() // Accept blocks until next connection is received

		// serve connection in a separate goroutine using JSON codec
		go server.ServeCodec(jsonrpc.NewServerCodec(conn))
	}

}
