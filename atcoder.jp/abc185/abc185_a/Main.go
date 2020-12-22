package main

import "fmt"
import "math"

func main() {
	var a, b, c, d float64
	fmt.Scan(&a, &b, &c, &d)
	fmt.Print(math.Min(a, math.Min(b, math.Min(c, d))))
}