package main

import "fmt"

func main() {
	/*
		//int型：環境依存で32bitか64bitに変化する。int8などで指定も可能
		//uint型：int型とは違い負の値は使えない
		//complex型：複素数を扱える
		var (
			u8  uint8     = 255
			i8  int8      = 127
			f32 float32   = 0.2
			c64 complex64 = -5 + 12i
			//Goではイコールを揃える書き方が推奨されている（見易さの問題）
		)
		fmt.Println(u8, i8, f32, c64)
		fmt.Printf("Type=%T value=%v", u8, u8)
		//%Tで型が分かるだけでなく、%vで数値が分かる。他にもあるがdocを参照
	*/
	/*
		fmt.Println("1 + 1 = ", 1+1)
		//計算でint型同士なら解もint型になるが、一方でもfloat型の場合は解がfloat型になる
	*/

	/*
		x := 0
		fmt.Println(x)
		x++
		fmt.Println(x)
		x--
		fmt.Println(x)
	*/

	//ビット演算（x << nで2進数のxをnbit左に、x >> nで2進数のxをnbit右にシフトする）
	fmt.Println(1 << 0) // 0001 0001
	fmt.Println(1 << 1) // 0001 0010
	fmt.Println(1 << 2) // 0001 0100
	fmt.Println(1 << 3) // 0001 1000
}
