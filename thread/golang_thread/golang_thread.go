package main

import (
        "fmt"
        "time"
	    "strconv"
)

func do_waiting(arg int) {
	fmt.Println(strconv.Itoa(arg) + " start waiting.")
    time.Sleep(300 * time.Millisecond)
    fmt.Println(strconv.Itoa(arg) + " stop waiting.")
}

func main() {
    fmt.Println("main thread start...")
    for i:=0; i<10; i++ {
        go do_waiting(i)
    }
    // bug ： main thread has to wait until the end of child thread
    // if main thread exit, child thread will automatically exit.

}
