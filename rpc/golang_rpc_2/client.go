package main

import (
	"log"
	"net/rpc"
)

func main() {
	client, err := rpc.Dial("tcp", "localhost:42586")
	if err != nil {
		log.Fatal(err)
	}


        var reply bool
        err = client.Call("Listener.GetLine", "line", &reply)
        if err != nil {
            log.Fatal(err)
        }
}
