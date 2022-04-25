package kata

func Feast(beast string, dish string) bool {
  // your code here
  b := []rune(beast);
  d := []rune(dish);
  return (b[0] == d[0]) && (b[len(b)-1] == d[len(d)-1])
}