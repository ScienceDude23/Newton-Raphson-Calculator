import sympy
import time
import sys

n = input('How many variables? ')

if n == '3':
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

elif n == '2':
    x1, x2 = sympy.symbols('x1 x2')

    f1 = sympy.sympify(input('Define function f1: '))
    f2 = sympy.sympify(input('Define function f2: '))

    x1ev = input('Input starting value of x1: ')
    x2ev = input('Input starting value of x2: ')
    stop = float(input('Define error bound: '))

    dx1 = 1
    dx2 = 1

    while abs(dx1) >= stop and abs(dx2) >= stop:
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

        x1ev = dx1 + float(x1ev)
        x2ev = dx2 + float(x2ev)
    ans = sympy.Matrix([x1ev,x2ev])
    sympy.pprint(ans)

elif n=='4':
    x1, x2, x3, x4 = sympy.symbols('x1 x2 x3 x4')

    f1 = sympy.sympify(input('Define function f1: '))
    f2 = sympy.sympify(input('Define function f2: '))
    f3 = sympy.sympify(input('Define function f3: '))
    f4= sympy.sympify(input('Define function f3: '))


    x1ev = input('Input starting value of x1: ')
    x2ev = input('Input starting value of x2: ')
    x3ev = input('Input starting value of x3: ')
    x4ev = input('Input starting value of x4: ')
    stop = float(input('Define error bound: '))

    dx1 = 1
    dx2 = 1
    dx3 = 1
    dx4 = 1

    while abs(dx1) >= stop and abs(dx2) >= stop and abs(dx3) >= stop and abs(dx4) >= stop:
        F = sympy.Matrix([f1, f2, f3, f4])
        x = [x1, x2, x3, x4]
        J = F.jacobian(x)

        evF = F.subs({x1:x1ev,x2:x2ev,x3:x3ev,x4:x4ev})
        nF = -1*evF
        evJ = J.subs({x1:x1ev,x2:x2ev,x3:x3ev,x4:x4ev})

        Jaug = evJ.col_insert(3,nF)
        rref = Jaug.rref()

        dx1 = rref[0][0,4]
        dx2 = rref[0][1,4]
        dx3 = rref[0][2,4]
        dx3 = rref[0][3,4]

        x1ev = dx1 + float(x1ev)
        x2ev = dx2 + float(x2ev)
        x3ev = dx3 + float(x3ev)
        x4ev = dx4 + float(x4ev)
    ans = sympy.Matrix([x1ev,x2ev,x3ev, x4ev])
    sympy.pprint(ans)


else:
    def delay_print(s):
        for c in s:
            sys.stdout.write(c)
            sys.stdout.flush()
            time.sleep(0.05)

    delay_print("You fucked up. ")
    time.sleep(.25)
    delay_print("My retarded ass can't code for n variables, so pick 2, 3, or 4. ")
    time.sleep(.5)
    delay_print("Actually, go fuck yourself. ")
    time.sleep(.25)
    delay_print("Goodbye.")