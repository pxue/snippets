package main

import "fmt"

type P struct {
	X int
	Y int
}

func Pascal(x int, y int, cache *map[P]int) (ret int) {

	if x == 0 || x == y {
		return 1
	}

	ret = 0
	if y%2 == 0 && x == y/2 {
		if val, ok := (*cache)[P{x - 1, y - 1}]; ok {
			return val * 2
		}
	}

	// we can mirrow it
	new_x := x
	if x >= y/2+1 {
		new_x = y - x
	}

	for i := new_x - 1; i <= new_x; i++ {
		if val, ok := (*cache)[P{i, y - 1}]; ok {
			ret += val
		} else {
			ret += Pascal(i, y-1, cache)
		}
	}
	(*cache)[P{new_x, y}] = ret
	fmt.Println(*cache)

	return
}

func NewPascal(x int, y int) (ret int) {
    if x > y+1 {
        return 0
    }
    if x == 0 || x == y {
        return 1
    }

    line := []int{1}
    for i := 0; i <= y; i++ {
        if i == x || i == (y-x) {
            break
        }
        line = append(line, line[i] * (y-i) / (i+1) )
    }
    fmt.Println(line)
    if x > (y-x) {
        return line[(y-x)]
    }
    return line[x]
}

func main() {
	/*p := map[P]int{}*/
	/*fmt.Println(Pascal(2, 5, &p))*/
    fmt.Println(NewPascal(2, 7))
}
