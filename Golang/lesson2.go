package main

import "fmt"

func main() {
	var i int = 1
	var f64 float64 = 1.2
	var s string = "test"
	var t bool = true
	var f bool = false
	//varを一気に宣言したい場合、impotのパッケージと同じように()でまとめて出来る

	fmt.Println(i, f64, s, t, f)

	xi := 1
	xf64 := 1.2
	xs := "test"
	xt, xf := true, false
	fmt.Println(xi, xf64, xs, xt, xf)
	fmt.Printf("%T", xf64)
	// := で定義したものは関数内でのみ有効なプライベート変数。varで定義した関数はグローバル変数
	// var [name] [type] = [variable]で定義
	//fmt.Printf()は改行を「\n」で手動入力しなければ改行されない
}
