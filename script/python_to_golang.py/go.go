package main

import (
	"time"
	"C"
	"fmt"
)

//递归实现斐波那契
func Fibonacci(i int) int {
    if i < 1 {
        return 0
    }
    if i == 1 || i == 2 {
        return 1
    }
    return Fibonacci(i-1) + Fibonacci(i-2)
}

// func main(){
// 	now:=time.Now()
// 	fmt.Println(fibonacci(30))
// 	fmt.Printf("%f s\n", time.Since(now).Seconds())
// }

// 832040
// 0.003725 s


func Count_time() *C.char {
	start := time.Now()
    Fibonacci(30)
    total_time := time.Since(start).String()
    return C.CString(total_time)
}

func main(){
	fmt.Println(*Count_time())
}
 