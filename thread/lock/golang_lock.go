package main

import (
	"fmt"
	"sync"
	"time"
)

var a = 0
// def lock
var lock sync.Mutex

func work1(count int) {
        // add lock
	lock.Lock()
        // when the func end, unlock
	defer lock.Unlock()
	for i := 0; i < 1000000; i++ {
		a += 1
	}
	fmt.Printf("a is %d\n", a)
}

func work2(count int) {
        // add lock
	lock.Lock()
        // when the func end, unlock
	defer lock.Unlock()
	for i := 0; i < 1000000; i++ {
		a += 1
	}
	fmt.Printf("a is %d\n", a)
}

func main() {
	go work1(a)
	go work2(a)
	time.Sleep(time.Second * 2)
}
