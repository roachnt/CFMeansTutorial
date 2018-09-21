from phi import *
import numpy as np
import random
import numbers
import pandas as pd
import math
from inspect import signature
from fluky import fluky

# Python Program to print kth prime factor
import math
def kPrimeFactor(n, k):

    while (n % 2 == 0):
        k = k - 1
        n = n / 2
        if (k == 0):
            return 2

    i = 3
    while i <= math.sqrt(n):

        while (n % i == 0):
            if (k == 1):
                return i

            k = k - 1
            n = n / i

        i = i + 2

    if (n > 2 and k == 1):
        return n

    return -1


import math
def bad_kPrimeFactor(n,k):
    gen_bad = random.random() > 0.5
    n_0 = n;k_0 = k;
    i_0=None;i_2=None;i_1=None;i_3=None;k_2=None;k_1=None;k_3=None;k_7=None;k_5=None;k_4=None;k_6=None;k_8=None;n_2=None;n_1=None;n_3=None;n_7=None;n_5=None;n_4=None;n_6=None;n_8=None;

    phi0 = Phi()
    while (phi0.phiLoopTest(n_0,n_1)%2==0):
        phi0.set()
        k_2 = phi0.phiEntry(k_0,k_1)
        n_2 = phi0.phiEntry(n_0,n_1)

        k_1=k_2-1 
        n_1=fluky(n_2/2, n_2*2, gen_bad, 0.9)
        
        if (k_1==0):
            lo = locals()
            record_locals(lo, bad_kPrimeFactor_causal_map)
            return 2
    k_3 = phi0.phiExit(k_0,k_1)
    n_3 = phi0.phiExit(n_0,n_1)
    i_0=3 
    phi0 = Phi()
    while phi0.phiLoopTest(i_0,i_1)<=math.sqrt(phi0.phiLoopTest(n_3,n_6)):
        phi0.set()
        i_2 = phi0.phiEntry(i_0,i_1)
        k_7 = phi0.phiEntry(k_3,k_6)
        n_7 = phi0.phiEntry(n_3,n_6)

        phi1 = Phi()
        while (phi1.phiLoopTest(n_7,n_4)%i_2==0):
            phi1.set()
            k_5 = phi1.phiEntry(k_7,k_4)
            n_5 = phi1.phiEntry(n_7,n_4)

            if (k_5==1):
                lo = locals()
                record_locals(lo, bad_kPrimeFactor_causal_map)
                return i_2
            k_4=k_5 - 1
            n_4=n_5/i_2
        k_6 = phi1.phiExit(k_7,k_4)
        n_6 = phi1.phiExit(n_7,n_4)
        i_1= i_2+2
    i_3 = phi0.phiExit(i_0,i_1)
    k_8 = phi0.phiExit(k_3,k_6)
    n_8 = phi0.phiExit(n_3,n_6)
    if (n_8>2 and k_8==1):
        lo = locals()
        record_locals(lo, bad_kPrimeFactor_causal_map)
        return n_8
    return -1



#generate python causal map
bad_kPrimeFactor_causal_map = {'n_2':['n_0','n_1','n_1','n_0'],'k_5':['k_7','k_4','n_4','n_7','i_2'],'n_1':['n_2'],'k_4':['k_5'],'k_7':['k_3','k_6','n_3','n_6','i_1','i_0'],'n_4':['n_5','i_2'],'n_3':['n_0','n_1','n_1','n_0'],'k_6':['k_7','k_4','n_4','n_7','i_2'],'n_6':['n_7','n_4','n_4','n_7','i_2'],'n_5':['n_7','n_4','n_4','n_7','i_2'],'k_8':['k_3','k_6','n_3','n_6','i_1','i_0'],'n_8':['n_3','n_6','n_3','n_6','i_1','i_0'],'n_7':['n_3','n_6','n_3','n_6','i_1','i_0'],'i_1':['i_2'],'i_0':[],'k_1':['k_2'],'i_3':['i_0','i_1','n_3','n_6','i_1','i_0'],'i_2':['i_0','i_1','n_3','n_6','i_1','i_0'],'k_3':['k_0','k_1','n_1','n_0'],'k_2':['k_0','k_1','n_1','n_0'],}

#added phi names
bad_kPrimeFactor_phi_names_set = {'k_2','n_2','k_3','n_3','i_2','k_7','n_7','k_5','n_5','k_6','n_6','i_3','k_8','n_8',}


def lcm(num1, num2):

    if(num1 > num2):
        num = num1
        den = num2

    else:
        num = num2
        den = num1
    rem = num % den

    while(rem != 0):
        num = den
        den = rem
        rem = num % den

    gcd = den
    lcm = int(int(num1 * num2)/int(gcd))

    return lcm


def bad_lcm(num1,num2):
    gen_bad = random.random() > 0.5

    num1_0 = num1;num2_0 = num2;
    num_0=None;num_1=None;num_2=None;num_4=None;num_3=None;num_5=None;lcm_0=None;gcd_0=None;rem_0=None;rem_2=None;rem_1=None;rem_3=None;den_0=None;den_1=None;den_2=None;den_4=None;den_3=None;den_5=None;

    if (num1_0>num2_0):
        num_0=num1_0 
        den_0=num2_0 
    else:
        num_1=num2_0 
        den_1=num1_0 
    phiPreds = [(num1_0>num2_0)]
    phiNames = [num_0,num_1]
    num_2= phiIf(phiPreds, phiNames)
    phiPreds = [(num1_0>num2_0)]
    phiNames = [den_0,den_1]
    den_2= phiIf(phiPreds, phiNames)
    rem_0=num_2%den_2 
    phi0 = Phi()
    while (phi0.phiLoopTest(rem_0,rem_1)!=0):
        phi0.set()
        num_4 = phi0.phiEntry(num_2,num_3)
        rem_2 = phi0.phiEntry(rem_0,rem_1)
        den_4 = phi0.phiEntry(den_2,den_3)

        num_3=den_4
        den_3=rem_2 
        rem_1=num_3%den_3
    num_5 = phi0.phiExit(num_2,num_3)
    rem_3 = phi0.phiExit(rem_0,rem_1)
    den_5 = phi0.phiExit(den_2,den_3)
    gcd_0=fluky(den_5, den_5 + 5, gen_bad, 0.9)
    lcm_0=int(int(num1_0*num2_0)/int(gcd_0)) 
    lo = locals()
    record_locals(lo, bad_lcm_causal_map)
    return lcm_0



#generate python causal map
bad_lcm_causal_map = {'gcd_0':['den_5'],'lcm_0':['num1_0','num2_0','gcd_0'],'den_0':['num2_0'],'den_1':['num1_0'],'den_2':['den_0','den_1','num1_0','num2_0'],'den_3':['rem_2'],'den_4':['den_2','den_3','rem_1','rem_0'],'num_0':['num1_0'],'den_5':['den_2','den_3','rem_1','rem_0'],'num_5':['num_2','num_3','rem_1','rem_0'],'rem_3':['rem_0','rem_1','rem_1','rem_0'],'rem_1':['num_3','den_3'],'rem_2':['rem_0','rem_1','rem_1','rem_0'],'num_1':['num2_0'],'num_2':['num_0','num_1','num1_0','num2_0'],'rem_0':['num_2','den_2'],'num_3':['den_4'],'num_4':['num_2','num_3','rem_1','rem_0'],}

#added phi names
bad_lcm_phi_names_set = {'num_2','den_2','num_4','rem_2','den_4','num_5','rem_3','den_5',}

def steins_algorithm(a, b):

    if (a == 0):
        return b
    if (b == 0):
        return a
    k = 0
    while(((a | b) & 1) == 0):
        a = a >> 1
        b = b >> 1
        k = k + 1
    while ((a & 1) == 0):
        a = a >> 1
    while(b != 0):
        while ((b & 1) == 0):
            b = b >> 1
        if (a > b):
            temp = a
            a = b
            b = temp
        b = (b - a)
    return (a << k)

def bad_steins_algorithm(a,b):
    gen_bad = random.random() > 0.5

    a_0 = a;b_0 = b;
    a_2=None;a_1=None;a_3=None;a_5=None;a_4=None;a_6=None;a_9=None;a_7=None;a_8=None;a_10=None;b_2=None;b_1=None;b_3=None;b_10=None;b_5=None;b_4=None;b_6=None;b_7=None;b_8=None;b_9=None;b_11=None;temp_2=None;temp_0=None;temp_1=None;temp_3=None;k_0=None;k_2=None;k_1=None;k_3=None;

    lo = locals()
    record_locals(lo, bad_steins_algorithm_causal_map)
    if (a_0==0):
        return b_0
    if (b_0==0):
        return a_0
    k_0=0 
    phi0 = Phi()
    while (((phi0.phiLoopTest(a_0,a_1)|phi0.phiLoopTest(b_0,b_1))&1)==0):
        phi0.set()
        a_2 = phi0.phiEntry(a_0,a_1)
        b_2 = phi0.phiEntry(b_0,b_1)
        k_2 = phi0.phiEntry(k_0,k_1)

        a_1=a_2>>1 
        b_1=b_2>>1 
        k_1=fluky(k_2+1, k_2+3, gen_bad, 0.9)
    a_3 = phi0.phiExit(a_0,a_1)
    b_3 = phi0.phiExit(b_0,b_1)
    k_3 = phi0.phiExit(k_0,k_1)
    phi0 = Phi()
    while ((phi0.phiLoopTest(a_3,a_4)&1)==0):
        phi0.set()
        a_5 = phi0.phiEntry(a_3,a_4)

        a_4=a_5>>1 
    a_6 = phi0.phiExit(a_3,a_4)
    phi0 = Phi()
    while (phi0.phiLoopTest(b_3,b_9)!=0):
        phi0.set()
        a_9 = phi0.phiEntry(a_6,a_8)
        b_10 = phi0.phiEntry(b_3,b_9)
        temp_2 = phi0.phiEntry(None,temp_1)

        phi1 = Phi()
        while ((phi1.phiLoopTest(b_10,b_4)&1)==0):
            phi1.set()
            b_5 = phi1.phiEntry(b_10,b_4)

            b_4=b_5>>1 
        b_6 = phi1.phiExit(b_10,b_4)
        if (a_9>b_6):
            temp_0=a_9 
            a_7=b_6 
            b_7=temp_0 
        phiPreds = [(a_9>b_6)]
        phiNames = [a_7,a_9]
        a_8= phiIf(phiPreds, phiNames)
        phiPreds = [(a_9>b_6)]
        phiNames = [temp_0,temp_2]
        temp_1= phiIf(phiPreds, phiNames)
        phiPreds = [(a_9>b_6)]
        phiNames = [b_7,b_6]
        b_8= phiIf(phiPreds, phiNames)
        b_9=(b_8-a_8) 
    a_10 = phi0.phiExit(a_6,a_8)
    b_11 = phi0.phiExit(b_3,b_9)
    temp_3 = phi0.phiExit(None,temp_1)
    lo = locals()
    record_locals(lo, bad_steins_algorithm_causal_map)
    return (a_10<<k_3)



#generate python causal map
bad_steins_algorithm_causal_map = {'a_10':['a_6','a_8','b_3','b_9'],'a_1':['a_2'],'b_2':['b_0','b_1','a_1','b_0','a_0','b_1'],'a_3':['a_0','a_1','a_1','b_0','a_0','b_1'],'a_2':['a_0','a_1','a_1','b_0','a_0','b_1'],'b_1':['b_2'],'a_5':['a_3','a_4','a_3','a_4'],'b_4':['b_5'],'b_3':['b_0','b_1','a_1','b_0','a_0','b_1'],'a_4':['a_5'],'b_6':['b_10','b_4','b_10','b_4'],'a_7':['b_6'],'a_6':['a_3','a_4','a_3','a_4'],'b_5':['b_10','b_4','b_10','b_4'],'a_9':['a_6','a_8','b_3','b_9'],'b_8':['b_7','b_6','b_6','a_9'],'b_7':['temp_0'],'a_8':['a_7','a_9','b_6','a_9'],'k_1':['k_2'],'k_0':[],'b_9':['b_8','a_8'],'k_3':['k_0','k_1','a_1','b_0','a_0','b_1'],'k_2':['k_0','k_1','a_1','b_0','a_0','b_1'],'b_11':['b_3','b_9','b_3','b_9'],'b_10':['b_3','b_9','b_3','b_9'],'temp_0':['a_9'],'temp_1':['temp_0','temp_2','b_6','a_9'],'temp_2':['temp_1','b_3','b_9'],'temp_3':['temp_1','b_3','b_9'],}

#added phi names
bad_steins_algorithm_phi_names_set = {'a_2','b_2','k_2','a_3','b_3','k_3','a_5','a_6','a_9','b_10','temp_2','b_5','b_6','a_8','temp_1','b_8','a_10','b_11','temp_3',}


def xgcd(a, b):

    x, y, lastx, lasty = 0, 1, 1, 0

    while b != 0:
        q = a // b
        r = a % b
        a = b
        b = r
        temp = x
        x = lastx - q * x
        if x > 50:
            b = 6
        else:
            while a > 0:
                a -= 5
        lastx = temp
        temp = y
        y = lasty - q * y
        lasty = temp
    return a

def bad_xgcd(a,b):
    gen_bad = random.random() > 0.5
    a_0 = a;b_0 = b;
    a_6=None;a_1=None;a_3=None;a_2=None;a_4=None;a_5=None;a_7=None;q_1=None;q_0=None;q_2=None;b_4=None;b_1=None;b_2=None;b_3=None;b_5=None;r_1=None;r_0=None;r_2=None;temp_2=None;temp_0=None;temp_1=None;temp_3=None;x_0=None;x_2=None;x_1=None;x_3=None;y_0=None;y_2=None;y_1=None;y_3=None;lasty_0=None;lasty_2=None;lasty_1=None;lasty_3=None;lastx_0=None;lastx_2=None;lastx_1=None;lastx_3=None;

    x_0,y_0,lastx_0,lasty_0=0,1,1,0 
    phi0 = Phi()
    while phi0.phiLoopTest(b_0,b_3)!=0:
        phi0.set()
        q_1 = phi0.phiEntry(None,q_0)
        a_6 = phi0.phiEntry(a_0,a_5)
        r_1 = phi0.phiEntry(None,r_0)
        b_4 = phi0.phiEntry(b_0,b_3)
        temp_2 = phi0.phiEntry(None,temp_1)
        x_2 = phi0.phiEntry(x_0,x_1)
        y_2 = phi0.phiEntry(y_0,y_1)
        lasty_2 = phi0.phiEntry(lasty_0,lasty_1)
        lastx_2 = phi0.phiEntry(lastx_0,lastx_1)

        q_0=a_6//b_4 
        r_0=a_6%b_4 
        a_1=b_4 
        b_1=r_0 
        temp_0=x_2 
        x_1=lastx_2-q_0*x_2 
        if x_1>50:
            b_2=6 
        else:
            phi1 = Phi()
            while phi1.phiLoopTest(a_1,a_2)>0:
                phi1.set()
                a_3 = phi1.phiEntry(a_1,a_2)
                a_2 = fluky(a_3-5, a_3-9, gen_bad, 0.9)
            a_4 = phi1.phiExit(a_1,a_2)
        phiPreds = [x_1>50]
        phiNames = [a_1,a_4]
        a_5= phiIf(phiPreds, phiNames)
        phiPreds = [x_1>50]
        phiNames = [b_2,b_1]
        b_3= phiIf(phiPreds, phiNames)
        lastx_1=temp_0 
        temp_1=y_2 
        y_1=lasty_2-q_0*y_2 
        lasty_1=temp_1 
    q_2 = phi0.phiExit(None,q_0)
    a_7 = phi0.phiExit(a_0,a_5)
    r_2 = phi0.phiExit(None,r_0)
    b_5 = phi0.phiExit(b_0,b_3)
    temp_3 = phi0.phiExit(None,temp_1)
    x_3 = phi0.phiExit(x_0,x_1)
    y_3 = phi0.phiExit(y_0,y_1)
    lasty_3 = phi0.phiExit(lasty_0,lasty_1)
    lastx_3 = phi0.phiExit(lastx_0,lastx_1)
    lo = locals()
    record_locals(lo, bad_xgcd_causal_map)
    return a_7



#generate python causal map
bad_xgcd_causal_map = {'a_1':['b_4'],'b_2':[],'a_3':['a_1','a_2','a_1','a_2'],'b_1':['r_0'],'a_2':['a_3'],'b_4':['b_0','b_3','b_0','b_3'],'a_5':['a_1','a_4','x_1'],'a_4':['a_1','a_2','a_1','a_2'],'b_3':['b_2','b_1','x_1'],'a_7':['a_0','a_5','b_0','b_3'],'a_6':['a_0','a_5','b_0','b_3'],'b_5':['b_0','b_3','b_0','b_3'],'lastx_0':[],'q_1':['q_0','b_0','b_3'],'r_0':['a_6','b_4'],'q_0':['a_6','b_4'],'lasty_2':['lasty_0','lasty_1','b_0','b_3'],'r_2':['r_0','b_0','b_3'],'lastx_3':['lastx_0','lastx_1','b_0','b_3'],'r_1':['r_0','b_0','b_3'],'q_2':['q_0','b_0','b_3'],'lasty_3':['lasty_0','lasty_1','b_0','b_3'],'lasty_0':[],'lastx_1':['temp_0'],'lastx_2':['lastx_0','lastx_1','b_0','b_3'],'lasty_1':['temp_1'],'x_0':[],'x_2':['x_0','x_1','b_0','b_3'],'y_1':['lasty_2','q_0','y_2'],'y_0':[],'x_1':['lastx_2','q_0','x_2'],'y_3':['y_0','y_1','b_0','b_3'],'y_2':['y_0','y_1','b_0','b_3'],'x_3':['x_0','x_1','b_0','b_3'],'temp_0':['x_2'],'temp_1':['y_2'],'temp_2':['temp_1','b_0','b_3'],'temp_3':['temp_1','b_0','b_3'],}

#added phi names
bad_xgcd_phi_names_set = {'q_1','a_6','r_1','b_4','temp_2','x_2','y_2','lasty_2','lastx_2','a_3','a_4','a_5','b_3','q_2','a_7','r_2','b_5','temp_3','x_3','y_3','lasty_3','lastx_3',}

def sumOdds(n):
    sum = 0
    while n >= 1:
        if n % 2 == 1:
            sum += n
        n -= 1
    return sum


def bad_sumOdds(n):
    # Indicates when fluky should generate a bad value.
    gen_bad = random.random() > 0.5
    n_0 = n
    sum_0 = None
    sum_3 = None
    sum_1 = None
    sum_2 = None
    sum_4 = None
    n_2 = None
    n_1 = None
    n_3 = None

    sum_0 = 0
    phi0 = Phi()
    while phi0.phiLoopTest(n_0, n_1) >= 1:
        phi0.set()
        sum_3 = phi0.phiEntry(sum_0, sum_2)
        n_2 = phi0.phiEntry(n_0, n_1)

        if n_2 % 2 == 1:
            sum_1 = sum_3 + n_2
        phiPreds = [n_2 % 2 == 1]
        phiNames = [sum_1, sum_3]
        sum_2 = phiIf(phiPreds, phiNames)
        n_1 = fluky(n_2 - 1, n_2 - 3, gen_bad, 0.9)
    sum_4 = phi0.phiExit(sum_0, sum_2)
    n_3 = phi0.phiExit(n_0, n_1)
    lo = locals()
    record_locals(lo, bad_sumOdds_causal_map)
    return sum_4

#generate python causal map
bad_sumOdds_causal_map = {'n_2':['n_0','n_1','n_1','n_0'],'n_1':['n_2'],'n_3':['n_0','n_1','n_1','n_0'],'sum_3':['sum_0','sum_2','n_1','n_0'],'sum_2':['sum_1','sum_3','n_2'],'sum_1':['sum_3','n_2'],'sum_0':[],'sum_4':['sum_0','sum_2','n_1','n_0'],}

#added phi names
bad_sumOdds_phi_names_set = {'sum_3','n_2','sum_2','sum_4','n_3',}

def sum_divs_and_rems(n):
    sum = 0
    while n >= 1:
        d = n // 2
        r = n % 2
        if r == 1:
            sum += d
        else:
            sum += r
        out = sum
        n -= 1
    return out


def bad_sum_divs_and_rems(n):
    gen_bad = random.random() > 0.5
    n_0 = n
    r_1 = None
    r_0 = None
    r_2 = None
    d_1 = None
    d_0 = None
    d_2 = None
    sum_0 = None
    sum_4 = None
    sum_1 = None
    sum_2 = None
    sum_3 = None
    sum_5 = None
    n_2 = None
    n_1 = None
    n_3 = None
    out_1 = None
    out_0 = None
    out_2 = None

    sum_0 = 0
    phi0 = Phi()
    while phi0.phiLoopTest(n_0, n_1) >= 1:
        phi0.set()
        r_1 = phi0.phiEntry(None, r_0)
        d_1 = phi0.phiEntry(None, d_0)
        sum_4 = phi0.phiEntry(sum_0, sum_3)
        n_2 = phi0.phiEntry(n_0, n_1)
        out_1 = phi0.phiEntry(None, out_0)

        d_0 = n_2 // 2
        r_0 = n_2 % 2
        if r_0 == 1:
            sum_1 = fluky(sum_4 + d_0, random.random(), gen_bad, 0.9)
        else:
            sum_2 = sum_4 + r_0
        phiPreds = [r_0 == 1]
        phiNames = [sum_1, sum_2]
        sum_3 = phiIf(phiPreds, phiNames)
        out_0 = sum_3
        n_1 = n_2 - 1
    r_2 = phi0.phiExit(None, r_0)
    d_2 = phi0.phiExit(None, d_0)
    sum_5 = phi0.phiExit(sum_0, sum_3)
    n_3 = phi0.phiExit(n_0, n_1)
    out_2 = phi0.phiExit(None, out_0)
    lo = locals()
    record_locals(lo, bad_sum_divs_and_rems_causal_map)
    return out_2


# generate python causal map
bad_sum_divs_and_rems_causal_map = {'n_2': ['n_0', 'n_1'], 'n_1': ['n_2'], 'r_0': ['n_2'], 'n_3': ['n_0', 'n_1'], 'r_2': ['r_0'],
              'r_1': ['r_0'], 'sum_5': ['sum_0', 'sum_3'], 'sum_4': ['sum_0', 'sum_3'], 'out_0': ['sum_3'],
              'out_2': ['out_0'], 'out_1': ['out_0'], 'd_0': ['n_2'], 'sum_3': ['sum_1', 'sum_2', 'r_0'],
              'sum_2': ['sum_4', 'r_0'], 'sum_1': ['sum_4', 'd_0'], 'd_2': ['d_0'], 'sum_0': [], 'd_1': ['d_0'], }

# added phi names
bad_sum_divs_and_rems_phi_names_set = {'r_1', 'd_1', 'sum_4', 'n_2', 'out_1',
                 'sum_3', 'r_2', 'd_2', 'sum_5', 'n_3', 'out_2', }


# Basic Algorithms in Number Theory by Buhler & Wagon, 2008.
def right_to_left_exp(x, n):
    y = 1
    while n > 0:
        r = n % 2
        p = r == 1
        if p:
            y = x * y
        x = x * x
        n = math.floor(n/2)
    return y


def bad_right_to_left_exp(x, n):
    gen_bad = random.random() > 0.5
    x_0 = x
    n_0 = n
    p_1 = None
    p_0 = None
    p_2 = None
    r_1 = None
    r_0 = None
    r_2 = None
    x_2 = None
    x_1 = None
    x_3 = None
    y_0 = None
    y_3 = None
    y_1 = None
    y_2 = None
    y_4 = None
    n_2 = None
    n_1 = None
    n_3 = None

    y_0 = 1
    phi0 = Phi()
    while phi0.phiLoopTest(n_0, n_1) > 0:
        phi0.set()
        p_1 = phi0.phiEntry(None, p_0)
        r_1 = phi0.phiEntry(None, r_0)
        x_2 = phi0.phiEntry(x_0, x_1)
        y_3 = phi0.phiEntry(y_0, y_2)
        n_2 = phi0.phiEntry(n_0, n_1)

        r_0 = n_2 % 2
        p_0 = r_0 == 1
        if p_0:
            y_1 = fluky(x_2 * y_3, x_2 * y_3 * random.random(), gen_bad, 1)
        phiPreds = [p_0]
        phiNames = [y_1, y_3]
        y_2 = phiIf(phiPreds, phiNames)
        x_1 = x_2 * x_2
        n_1 = math.floor(n_2 / 2)
    p_2 = phi0.phiExit(None, p_0)
    r_2 = phi0.phiExit(None, r_0)
    x_3 = phi0.phiExit(x_0, x_1)
    y_4 = phi0.phiExit(y_0, y_2)
    n_3 = phi0.phiExit(n_0, n_1)
    lo = locals()
    record_locals(lo, bad_right_to_left_exp_causal_map)
    return y_4


# generate python causal map

bad_right_to_left_exp_causal_map = {'n_2': ['n_0', 'n_1', 'n_0', 'n_1'], 'p_0': ['r_0'], 'n_1': ['n_2'], 'r_0': ['n_2'],
              'p_2': ['p_0', 'n_0', 'n_1'],
              'p_1': ['p_0', 'n_0', 'n_1'],
              'n_3': ['n_0', 'n_1', 'n_0', 'n_1'], 'r_2': ['r_0', 'n_0', 'n_1'], 'r_1': ['r_0', 'n_0', 'n_1'],
              'x_2': ['x_0', 'x_1', 'n_0', 'n_1'],
              'y_1': ['x_2', 'y_3'],
              'y_0': [], 'x_1': ['x_2', 'x_2'], 'y_3': ['y_0', 'y_2', 'n_0', 'n_1'], 'y_2': ['y_1', 'y_3', 'r_0'],
              'x_3': ['x_0', 'x_1', 'n_0', 'n_1'],
              'y_4': ['y_0', 'y_2', 'n_0', 'n_1'], }

#added phi names
phi_names_set = {'p_1','r_1','x_2','y_3','n_2','y_2','p_2','r_2','x_3','y_4','n_3',}


# this function merge local variables and its covariates into global_value_dict


def record_locals(local_vars, causal_map):
    with open("ssa_variables.csv", "a") as f:
        if test_counter == 0:
            column_names = list(local_vars.keys())
            column_names.append("output")
            column_names.append("incorrect")
            f.write(", ".join(column_names) +"\n")
            values = ["\"" + str(value) + "\"" if isinstance(value, list) else str(value) for value in list(local_vars.values())]
            f.write(", ".join(values))
        else:
            values = ["\"" + str(value) + "\"" if isinstance(value, list) else str(value) for value in list(local_vars.values())]
            f.write(", ".join(values))
    for name in local_vars:
        # if this postfix is in the name of the variable, skip it
        if '_IV' in name:
            continue
        # if the variable is a number and in the causal map
        if isinstance(local_vars[name], numbers.Number) and name in causal_map:
            if name not in global_value_dict:
                columns = causal_map[name].copy()
                columns.insert(0, name)
                global_value_dict[name] = pd.DataFrame(columns=columns)
            new_row = [np.float64(local_vars[name])]

            for pa in causal_map[name]:
                if isinstance(local_vars[pa], numbers.Number):
                    new_row.append(np.float64(local_vars[pa]))
                else:
                    new_row.append(local_vars[pa])
            global_value_dict[name].loc[test_counter] = new_row


good_dict = {}
# bad_dict and global_value_dict are imported by the localizer
bad_dict = {}
global_value_dict = {}
# test cases
# args = np.arange(1, 1000)

test_counter = 0
fails = 0

# running the test set
# for arg in args:
#     bad_dict[test_counter] = bad_sum_divs_and_rems(arg)
#     good_dict[test_counter] = sum_divs_and_rems(arg)
#     if abs(bad_dict[test_counter] - good_dict[test_counter]) > 0:
#         fails = fails + 1
#     test_counter += 1
#
# print("\n{0:10d} failures".format(fails))


def test_function(good_func, bad_func, n_tests, arg_min=1, arg_max=10):
    global test_counter
    global fails
    print("\n------- Test of Function", bad_func.__name__, "-------")
    
    # Get function information
    sig = signature(good_func)
    args_length = len(sig.parameters)

    # Erase contents of file for new test
    open('ssa_variables.csv', 'w').close()
    open("result.csv", "w").close()

    for _ in range(n_tests):
        # Get function arguments
        args = [random.randint(arg_min, arg_max) for arg in range(args_length)]

        # Run good and bad function with args
        good_dict[test_counter] = good_func(*args)
        bad_dict[test_counter] = bad_func(*args)

        # Output result of bad function
        with open("ssa_variables.csv", "a") as f:
            f.write(", " + str(bad_dict[test_counter]))

        # Check if bad function was incorrect
        if abs(bad_dict[test_counter] - good_dict[test_counter]) > 0:
            # Write result to file
            with open("ssa_variables.csv", "a") as f:
                f.write(", " + "True" + "\n")
            fails = fails + 1
        else:
            with open("ssa_variables.csv", "a") as f:
                f.write(", " + "False" + "\n")
        test_counter += 1


# change this function to change the function being tested and the number of tests
test_function(kPrimeFactor, bad_kPrimeFactor, 500)

print("Failures: ", fails)
