package main

import (
	"fmt"
	"log"
	"net/rpc"
)

func main() {
        // connect to the server
	client, err := rpc.Dial("tcp", "localhost:1234")
	if err != nil {
		log.Fatal("dialing:", err)
	}

	var reply string
        // remote Hello function
	err = client.Call("HelloService.Hello", "Jack", &reply)
	if err != nil {
		log.Fatal(err)
	}

	fmt.Println(reply)
}
