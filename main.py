
def eq(a: list, b: list, point: int=1):
# We'll be using the coordinates of the A point to find the equation
  if point == 1:
    y = a[1]
    m = (b[1] - a[1]) / (b[0] - a[0])
    mx = m*a[0]
    n = y - mx

  # Printing the found numbers and equation 
    print(f'm = {int(m)}')
    print(f'm*x = {int(mx)}')
    print(f'n = {int(n)}')
    print(f'y = {int(m)}x {int(n)}\n')

# We'll be using the coordinates of the B point to find the equation
  if point == 2:
    y = b[1]
    m = (b[1] - a[1]) / (b[0] - a[0])
    mx = m*b[0]
    n = y - mx

  # Printing the found numbers and equation 
    print(f'm = {m}')
    print(f'mx = {mx}')
    print(f'n = {n}')
    print(f'y = {int(m)}x {int(n)}\n')


eq([3, 2], [5, 4])
eq([3, 2], [5, 4], 2)

eq([5, -2], [4, 2])
eq([5, -2], [4, 2], 2)


# ax + by + c = 0

def eqg(a: list, b: list):
  eq = a[0] + b[1] + c 


