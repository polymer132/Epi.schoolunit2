import math
def solve_quadratic(a,b,c):
  det = b**2 - 4*a*c
  if det < 0:
    return None
  if det == 0: 
    return (-b+math.sqrt(det))/(2*a)
  if det > 0:
    return (-b+math.sqrt(det))/(2*a), (-b-math.sqrt(det))/(2*a)