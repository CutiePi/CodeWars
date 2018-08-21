function array_diff(a, b) {
  let diff  = a.filter(x => !b.includes(x));
  return diff;
}
