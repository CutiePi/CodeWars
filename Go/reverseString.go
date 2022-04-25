package kata
func Solution(word string) string {
  var reversed = "";
  for _,value := range word {
    reversed = string(value) + reversed;
  }
  return reversed; 
}