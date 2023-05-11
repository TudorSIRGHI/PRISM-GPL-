package main

import (
	"fmt"
	repl "gpl-main/ReplaytoFile"
	"os"
	"os/user"
)

func main() {
	if len(os.Args) > 2 {
		path := os.Args[1]
		repl.PrintAst(path, os.Stdout)
		return
	}
	if len(os.Args) > 1 {
		path := os.Args[1]
		repl.ExecuteFile(path, os.Stdout)
		return
	}
	user, err := user.Current()
	if err != nil {
		panic(err)
	}
	fmt.Printf("Hello %s!\n",
		user.Username)
	fmt.Printf("Feel free to type in commands:\n")
	repl.Start(os.Stdin, os.Stdout)
}
