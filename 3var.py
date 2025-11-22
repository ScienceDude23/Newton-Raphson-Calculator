import sympy

x1, x2, x3 = sympy.symbols('x1 x2 x3')

f1 = sympy.sympify(input('Define function f1: '))
f2 = sympy.sympify(input('Define function f2: '))
f3 = sympy.sympify(input('Define function f3: '))

x1ev = input('Input starting value of x1: ')
x2ev = input('Input starting value of x2: ')
x3ev = input('Input starting value of x3: ')
stop = input('Define error bound: ')

dx1 = 1
dx2 = 1
dx3 = 1

while abs(dx1) >= stop and abs(dx2) >= stop and abs(dx3) >= stop:
    F = sympy.Matrix([f1, f2, f3])
    x = [x1, x2, x3]
    J = F.jacobian(x)

    evF = F.subs({x1:x1ev,x2:x2ev,x3:x3ev})
    nF = -1*evF
    evJ = J.subs({x1:x1ev,x2:x2ev,x3:x3ev})

    Jaug = evJ.col_insert(3,nF)
    rref = Jaug.rref()

    dx1 = rref[0][0,3]
    dx2 = rref[0][1,3]
    dx3 = rref[0][2,3]

    x1ev = dx1 + float(x1ev)
    x2ev = dx2 + float(x2ev)
    x3ev = dx3 + float(x3ev)
ans = sympy.Matrix([x1ev,x2ev,x3ev])
sympy.pprint(ans)