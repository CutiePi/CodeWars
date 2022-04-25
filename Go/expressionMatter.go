package kata

func ExpressionMatter(a int, b int, c int) int {
    // your code here
  pp := a + b +c;
  mm := a * b * c;
  pm := (a + b) * c;
  pm2 := (a * b) + c;
  mp := a * (b + c);
  mp2 := a + (b * c);
  vals := []int{pp,mm,pm,pm2,mp,mp2};
  m := 0;
  for _,value := range vals {
    if(value > m){
      m = value;
    }
  }
  return m;
}