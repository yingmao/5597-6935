package main

import (
	"fmt"
	"net/rpc/jsonrpc"
)


type Student struct {
	FirstName, LastName string
}

func main() {

	// get JSON-RPC client by dialing TCP connection
	client, _ := jsonrpc.Dial("tcp", "127.0.0.1:9002")

        var john Student
	// add student by id `1`
	if err := client.Call("Student.Say", Student{
		FirstName: "John",
		LastName:  "Doe",
	}, &john); err != nil {
		fmt.Println("Error: Student.Say()", err)
	} else {
		fmt.Printf("Success: Student '%s' \n", john.FirstName)
	}

}
