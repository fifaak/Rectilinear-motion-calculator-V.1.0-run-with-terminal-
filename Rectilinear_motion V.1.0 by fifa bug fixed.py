from sympy import symbols, Eq, solve
from math import *
from datetime import datetime

def Main ():
    print("input  v  u  a  t  s")
    find =  str(input("find: "))
    if find == "u" or find == "U":
        print("input y for existent variable or n for  nonexistent variable")
        a_check = str(input("--> A  : "))
        t_check = str(input("--> T : "))
        s_check = str(input("--> S : "))
        v_check = str(input("--> V : "))
        if a_check == "y" and t_check == "y" and s_check =="y" and (v_check =="n" or v_check =="y"):
            u,a,t,s = symbols('u,a,t,s')
            a = float(input("input A : "))
            t = float(input("input T : "))
            s = float(input("input S : "))         
            eq1u = Eq((u*t)+((a*(t**2))/2),s)    
            answer = ((solve((eq1u),(u))))
            print("U =",answer)
        elif a_check == "y" and t_check == "y" and s_check =="n"  and v_check =="y":
            u,a,t,v = symbols('u,a,t,v')
            a = float(input("input A : "))
            t = float(input("input T : "))
            v = float(input("input V: "))
            eq2u = Eq((u+(a*t)),v)
            answer = ((solve(eq2u),(u)))
            print("U =",answer)
        elif a_check == "n" and t_check == "y" and s_check =="y" and v_check =="y":
            t,s,v,u = symbols('t,s,v,u')
            t = float(input("input T : "))
            s = float(input("input S : "))
            v = float(input("input V: "))
            eq3u = Eq((((u+v)/2)*t),s)
            answer = (solve(eq3u,u))
            print("U =",answer)
        elif a_check == "y" and t_check == "n" and s_check =="y" and v_check =="y":
            u,a,s,v =symbols('u,a,s,v')
            a = float(input("input A : "))
            s = float(input("input S : "))
            v = float(input("input V: "))
            eq4u = Eq((((u**2)+(2*a*s))),(v**2))
            answer = solve((eq4u),u)
            print("U =",answer)
        else:
            print("Not enough information")
    elif find == "a" or find == "A":
        print("input y for existent variable or n for  nonexistent variable")
        u_check = str(input("--> U : "))
        t_check = str(input("--> T : "))
        s_check = str(input("--> S : "))
        v_check = str(input("--> V : "))
        if u_check == "y" and t_check =="y" and s_check =="y" and (v_check =="n" or  v_check =="y"):
            u,t,s,a = symbols('u,t,s,a')
            u = float(input("input U : "))
            t = float(input("input T : "))
            s = float(input("input S : "))
            eq1a = Eq((u*t)+((a*(t**2))/2),s)    
            answer = ((solve((eq1a),(a))))
            print("A =",answer)
        elif u_check == "y" and t_check =="y" and s_check =="n"  and v_check =="y":
            v,u,t,a = symbols('v,u,t,a')
            v = float(input("input V: "))
            u = float(input("input U : "))
            t = float(input("input T : "))
            eq2a = Eq((u+(a*t)),v)
            answer = ((solve(eq2a),(a)))
            print("A =",answer)
        elif u_check == "n" and t_check =="y" and s_check =="y" and v_check =="y":
            s,v,t,a = symbols('s,v,t,a')
            s = float(input("input S : "))
            v = float(input("input V: "))
            t = float(input("input T : "))
            eq3a = Eq(((v*t)-(a*(t**2)/2)),s)
            answer = (solve((eq3a),a))
            print("A =",answer)
        elif u_check == "y" and t_check =="n"  and s_check =="y" and v_check =="y":
            u,s,v,a,t = symbols('u,s,v,a,t')
            u = float(input("input U : "))
            s = float(input("input S : "))
            v = float(input("input V: "))
            eq4a = Eq((((u**2)+(2*a*s))),(v**2))
            answer = solve((eq4a),a)
            print("A =",answer)
        else:
            print("Not enough information")
    elif find == "t" or find == "T":
        print("input y for existent variable or n for  nonexistent variable")
        a_check = str(input("--> A : "))
        u_check = str(input("--> U : "))
        s_check = str(input("--> S : "))
        v_check = str(input("--> V : "))
        if u_check == "y" and a_check =="y" and s_check =="y" and (v_check =="n" or v_check =="y"):
            u,s,v,a,t = symbols('u,s,v,a,t')
            u = float(input("input U : "))
            a = float(input("input A : "))
            s = float(input("input S : "))
            eq1t = Eq((u*t)+((a*(t**2))/2),s)    
            answer = ((solve((eq1t),(t))))
            print("T =",answer)
        elif u_check == "y" and a_check =="y" and s_check =="n"and v_check =="y":
            u,s,v,a,t = symbols('u,s,v,a,t')
            v = float(input("input V : "))
            u = float(input("input U : "))
            a = float(input("input A : "))
            eq2t = Eq((u+(a*t)),v)
            answer = ((solve(eq2t),(t)))
            print("T =",answer)
        elif u_check == "n" and a_check =="y" and s_check =="y" and v_check =="y":
            u,s,v,a,t = symbols('u,s,v,a,t')
            v = float(input("input V : "))
            s = float(input("input S : "))
            a = float(input("input A : "))
            eq3t = Eq(((v*t)-(a*(t**2)/2)),s)
            answer = (solve((eq3t),t))
            print("T =",answer)
        elif u_check == "y" and a_check =="n" and s_check =="y" and v_check =="y":
            u,s,v,a,t = symbols('u,s,v,a,t')
            v = float(input("input V : "))
            s = float(input("input S : "))
            u = float(input("input U : "))
            
            eq4t = Eq((((u+v)/2)*t),s)
            answer = (solve(eq4t,t))
            print("T =",answer)
        else:
            print("Not enough information")
    elif find == "s" or find == "S":
        print("input y for existent variable or n for  nonexistent variable")
        a_check = str(input("--> A : "))
        u_check = str(input("--> U : "))
        v_check = str(input("--> V : "))
        t_check = str(input("--> T : "))
        if u_check == "y" and t_check =="y" and a_check =="y" and (v_check =="n" or v_check =="y"):
            u,s,v,a,t = symbols('u,s,v,a,t')
            u = float(input("input U : "))
            t = float(input("input T : "))
            a = float(input("input A : "))
            eq1s = Eq((u*t)+((a*(t**2))/2),s)    
            answer = ((solve((eq1s),(s))))
            print("S =",answer)
        elif u_check == "n" and t_check =="y" and a_check =="y" and v_check =="y":
            u,s,v,a,t = symbols('u,s,v,a,t')
            v = float(input("input V : "))
            t = float(input("input T : "))
            a = float(input("input A : "))
            eq2s = Eq(((v*t)-(a*(t**2)/2)),s)
            answer = (solve((eq2s),s))
            print("S =",answer)
        elif u_check == "y" and t_check =="y" and a_check =="n" and v_check =="y":
            u,s,v,a,t = symbols('u,s,v,a,t')
            u = float(input("input U : "))
            t = float(input("input T : "))
            v = float(input("input V : "))
            eq3s = Eq((((u+v)/2)*t),s)
            answer = (solve(eq3s,s))
            print("S =",answer)
        elif u_check == "y" and t_check =="n" and a_check =="y" and v_check =="y":
            u,s,v,a,t = symbols('u,s,v,a,t')
            u = float(input("input U : "))
            v = float(input("input V : "))
            a = float(input("input A : "))
            eq4s = Eq((((u**2)+(2*a*s))),(v**2))
            answer = solve((eq4s),s)
            print("S =",answer)
        else:
            print("Not enough information")
    elif find =="v" or find == "V":
        print("input y for existent variable or n for  nonexistent variable")
        a_check = str(input("--> A : "))
        u_check = str(input("--> U : "))
        s_check = str(input("--> S : "))
        t_check = str(input("--> T : "))
        if u_check == "y" and t_check =="y" and (s_check =="n" or s_check =="y") and a_check =="y":
            u,s,v,a,t = symbols('u,s,v,a,t')
            u = float(input("input U : "))
            t = float(input("input T : "))
            a = float(input("input A : "))
            eq1v = Eq((u+(a*t)),v)
            answer = ((solve(eq1v),(v)))
            print("V =",answer)
        elif u_check == "y" and (t_check =="y" or t_check =="n") and s_check =="y" and a_check =="y":
            u,s,v,a,t = symbols('u,s,v,a,t')
            u = float(input("input U : "))
            s = float(input("input S : "))
            a = float(input("input A : "))
            eq4v = Eq((((u**2)+(2*a*s))),(v**2))
            answer = solve((eq4v),v)
            print("V =",answer)
        elif u_check == "n"  and t_check =="y" and s_check =="y" and a_check =="y":
            u,s,v,a,t = symbols('u,s,v,a,t')
            a = float(input("input A : "))
            t = float(input("input T : "))
            s = float(input("input S : "))
            eq2v = Eq(((v*t)-(a*(t**2)/2)),s)
            answer = (solve((eq2v),v))
            print("V =",answer)
        elif u_check == "y" and t_check =="y" and s_check =="y" and a_check =="n" :
            u,s,v,a,t = symbols('u,s,v,a,t')
            u = float(input("input U : "))
            t = float(input("input T : "))
            s = float(input("input S : "))
            eq3v = Eq((((u+v)/2)*t),s)
            answer = (solve(eq3v,v))
            print("V =",answer)
        else:
            print("Not enough information")
    else:
        print("Wrong, Do it again")
        Main()
    while True:
        print("-----finished-----")
        print("wanna restart the program y/n")
        repeat = str(input(": "))
        if repeat =="y":
            Main()
        else:
            break
    print("******The Program has stopped.******")
    exit()
def check ():
  
    roundd = 3
    while True:
        today = datetime.now().date().strftime('%d')
        today = int(today)
        encrypt = today*112-57
        encrypt = str(encrypt)
        passwordd = str(input("Password: "))
        if passwordd != encrypt:          
            roundd = int(roundd)
            roundd = roundd-1
            print("Incorrect password, you can try only "+str(roundd)+" time/s")
            if roundd == 0:
               
       
          
                break
        if passwordd == encrypt:
            print("----------Pass----------")
            print("-----Rectilinear motion V.1.2-----")
            print("License & Coding by fifa , bug-tester: tord")
            Main()
check()