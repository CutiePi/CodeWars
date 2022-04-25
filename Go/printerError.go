package kata
import "fmt"
import "strings"


func PrinterError(s string) string {
  length := len(s)
  errors := 0

  invalidChars := "nopqrstuvwxyz"

  for pos, char := range s {
    fmt.Println(string(char) + string(pos))
    if strings.Contains(invalidChars, string(char)) {
      errors += 1
    }
  }

  return fmt.Sprintf("%v", errors) + "/" + fmt.Sprintf("%v", length)

}