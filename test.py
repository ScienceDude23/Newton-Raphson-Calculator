import sympy

x1, x2 = sympy.symbols('x1 x2')

f1 = input('Define function f1: ')
f2 = input('Define function f2: ')

x1ev = input('Input starting value of x1: ')
x2ev = input('Input starting value of x2: ')
stop = float(input('Define error bound: '))

dx1 = 1
dx2 = 1

# while abs(dx1) >= stop and abs(dx2) >= stop:
#     F = sympy.Matrix([f1, f2])
#     x = [x1, x2]
#     J = F.jacobian(x)

#     evF = F.subs({x1:x1ev,x2:x2ev})
#     nF = -1*evF
#     evJ = J.subs({x1:x1ev,x2:x2ev})

#     Jaug = evJ.col_insert(2,nF)
#     rref = Jaug.rref()

#     dx1 = rref[0][0,2]
#     dx2 = rref[0][1,2]

#     x1ev = dx1 + float(x1ev)
#     x2ev = dx2 + float(x2ev)
# ans = sympy.Matrix([x1ev,x2ev])
# sympy.pprint(ans)

F = sympy.Matrix([f1, f2])
x = [x1, x2]
J = F.jacobian(x)

evF = F.subs({x1:x1ev,x2:x2ev})
nF = -1*evF
evJ = J.subs({x1:x1ev,x2:x2ev})

Jaug = evJ.col_insert(2,nF)
rref = Jaug.rref()

dx1 = rref[0][0,2]
dx2 = rref[0][1,2]

sympy.pprint(rref)
print(dx1, dx2)