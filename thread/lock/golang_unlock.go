package main

import (
	"fmt"
	"time"
)

var a = 0

func work1(count int) {
	for i := 0; i < 1000000; i++ {
		a += 1
	}
	fmt.Printf("a is %d\n", a)
}

func work2(count int) {
	for i := 0; i < 1000000; i++ {
		a += 1
	}
	fmt.Printf("a is %d\n", a)
}

func main() {
        // mult thread
	go work1(a)
	go work2(a)
	time.Sleep(time.Second * 2)
}
