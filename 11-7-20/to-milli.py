function to_milli(h, m, s){
  var total = 0
  total = total + ((h * 60) * 60) * 1000
  total = total + (m * 60) * 1000
  total = total + s * 1000
  return total
}