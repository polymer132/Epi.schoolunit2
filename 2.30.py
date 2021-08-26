def fizz_buzz():
  n=1
  while (n<=1000):
    if (n % 15) == 0:
      print ("fizzbuzz")
    elif (n % 3) == 0: 
      print ("fizz")
    elif (n % 5) == 0:
      print ("buzz")
    else: print(n)
    n = n + 1

fizz_buzz()
