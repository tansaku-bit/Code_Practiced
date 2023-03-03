package main

import "fmt"

//プログラム内で書き換えることのない定数はconstで定義する。グローバルのため基本的に関数の外側に書くと良い
//constは定義した時点でオーバーフローしても、処理後の値がオーバーフローしなければエラーにならない
const Pi = 3.14
const (
	Username = "default"
	Password = "0000"
)

func main() {
	fmt.Println(Pi, "\n", Username, Password)
}
