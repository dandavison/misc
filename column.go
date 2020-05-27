// For a proper solution see [xsv](https://github.com/BurntSushi/xsv).

// By default `column` squashes adjacent delimiters, which is very misleading:

// ```sh
// $ echo "a,b,c\n1,,3" | column -t -s,
// a  b  c
// 1  3
// ```

// The debian version provides `-n` which fixes this problem. But the BSD
// version on OS X does not. The version of `column` here exists to provide
// behavior like the `-n` flag on OS X.

// ```sh
// $ echo "a,b,c\n1,,3" | column -t -s=, -w=3
// a  b  c
// 1     3
// ```

package main

import (
	"bufio"
	"flag"
	"fmt"
	"io"
	"os"
	"strings"
)

func main() {

	var width int
	var sep string
	flag.IntVar(&width, "w", 25, "Field width in formatted output")
	flag.StringVar(&sep, "s", "\t", "String delimiting fields in input")
	flag.Bool("t", false, "[Ignored. For compatibility with unix column]")
	flag.Parse()

	field_fmt := fmt.Sprintf("%%-%ds", width)

	rdr := bufio.NewReader(os.Stdin)

	for {
		switch line, err := rdr.ReadString('\n'); err {

		case nil:
			line = strings.TrimRight(line, "\n")
			fields := strings.Split(line, sep)
			for _, field := range fields {
				fmt.Printf(field_fmt, field)
			}
			fmt.Print("\n")

		case io.EOF:
			os.Exit(0)
		}
	}
}
