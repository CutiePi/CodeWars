package kata

func RowSumOddNumbers(n int) int {
    // your code here
  maxNum := n * (n + 1);
  startRow := n*(n-1)
  sum := 0;
  for i := startRow; i < maxNum; i++ {
      if(i%2!=0){
        sum+=i;
      }
    }
    return sum;
  }