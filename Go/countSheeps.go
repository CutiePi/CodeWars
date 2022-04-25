package kata

func CountSheeps(numbers []bool) int {
  var missing int = 0;
  for _, element := range numbers {
   if(element){
    missing+=1;
  }
    }
  return missing // your code here
  
}