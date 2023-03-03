package main

//パッケージまたはライブラリと呼ばれる関数の塊
import (
	"fmt"
	"os/user" //osパッケージの下にuserパッケージがある
	"time"
)

func main() {
	//Golangのプログラムを成立させるために必ず必要なmain関数。他の関数は例外を除きmainから呼び出して使う。
	//パッケージについて調べたいときは、cmdから"go doc [package] [function]"で調べられる
	fmt.Println("Hello, World", "To be continued")
	fmt.Println(time.Now())
	fmt.Println(user.Current())
}
