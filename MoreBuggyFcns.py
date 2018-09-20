from phi import *
import numpy as np
import random
import numbers
import pandas as pd
import math
from inspect import signature


def fluky(good_val, bad_val, gen_bad, p):
    if not gen_bad:
        return good_val
    r = random.random()
    if r <= p:
        return bad_val
    else:
        return good_val

def sumOdds(n):
    sum = 0;
    while n >= 1:
        if n % 2 == 1:
            sum += n
        n -= 1
    return sum


def bad_sumOdds(n):
    gen_bad = random.random() > 0.5;  # Indicates when fluky should generate a bad value.
    n_0 = n;
    sum_0 = None;
    sum_3 = None;
    sum_1 = None;
    sum_2 = None;
    sum_4 = None;
    n_2 = None;
    n_1 = None;
    n_3 = None;

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
    record_locals(lo, test_counter)
    return sum_4


def sum_divs_and_rems(n):
    sum = 0;
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
    n_0 = n;
    r_1 = None;
    r_0 = None;
    r_2 = None;
    d_1 = None;
    d_0 = None;
    d_2 = None;
    sum_0 = None;
    sum_4 = None;
    sum_1 = None;
    sum_2 = None;
    sum_3 = None;
    sum_5 = None;
    n_2 = None;
    n_1 = None;
    n_3 = None;
    out_1 = None;
    out_0 = None;
    out_2 = None;

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
    record_locals(lo, test_counter)
    return out_2


# generate python causal map
# causal_map = {'n_2': ['n_0', 'n_1'], 'n_1': ['n_2'], 'r_0': ['n_2'], 'n_3': ['n_0', 'n_1'], 'r_2': ['r_0'],
#               'r_1': ['r_0'], 'sum_5': ['sum_0', 'sum_3'], 'sum_4': ['sum_0', 'sum_3'], 'out_0': ['sum_3'],
#               'out_2': ['out_0'], 'out_1': ['out_0'], 'd_0': ['n_2'], 'sum_3': ['sum_1', 'sum_2', 'r_0'],
#               'sum_2': ['sum_4', 'r_0'], 'sum_1': ['sum_4', 'd_0'], 'd_2': ['d_0'], 'sum_0': [], 'd_1': ['d_0'], }
#
# added phi names
# phi_names_set = {'r_1', 'd_1', 'sum_4', 'n_2', 'out_1', 'sum_3', 'r_2', 'd_2', 'sum_5', 'n_3', 'out_2', }

def right_to_left_exp(x, n): # Basic Algorithms in Number Theory by Buhler & Wagon, 2008.
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
    x_0 = x;
    n_0 = n;
    p_1 = None;
    p_0 = None;
    p_2 = None;
    r_1 = None;
    r_0 = None;
    r_2 = None;
    x_2 = None;
    x_1 = None;
    x_3 = None;
    y_0 = None;
    y_3 = None;
    y_1 = None;
    y_2 = None;
    y_4 = None;
    n_2 = None;
    n_1 = None;
    n_3 = None;

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
    record_locals(lo, test_counter)
    return y_4


# generate python causal map
causal_map = {'n_2': ['n_0', 'n_1', 'n_0', 'n_1'], 'p_0': ['r_0'], 'n_1': ['n_2'], 'r_0': ['n_2'],
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

#this function merge local variables and its covariates into global_value_dict
def record_locals(lo, i):
    for name in lo:
        # if this postfix is in the name of the variable, skip it
        if '_IV' in name:
            continue
        # if the variable is a number and in the causal map
        if isinstance(lo[name], numbers.Number) and name in causal_map:
            if name not in global_value_dict:
                columns = causal_map[name].copy()
                columns.insert(0, name)
                global_value_dict[name] = pd.DataFrame(columns=columns)
            new_row = [np.float64(lo[name])]

            for pa in causal_map[name]:
                if isinstance(lo[pa], numbers.Number):
                    new_row.append(np.float64(lo[pa]))
                else:
                    new_row.append(lo[pa])
            global_value_dict[name].loc[i] = new_row

good_dict = {}
#bad_dict and global_value_dict are imported by the localizer
bad_dict = {}
global_value_dict = {}
#test cases
# args = np.arange(1, 1000)

test_counter = 0
fails = 0

#running the test set
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
    print("------- Test of Function", bad_func.__name__, "-------")
    sig = signature(good_func)
    args_length = len(sig.parameters)
    for _ in range(n_tests):
        args = [random.randint(arg_min, arg_max) for arg in range(args_length)]
        good_dict[test_counter] = good_func(*args)
        bad_dict[test_counter] = bad_func(*args)
        if abs(bad_dict[test_counter] - good_dict[test_counter]) > 0:
            fails = fails + 1
        test_counter += 1

test_function(right_to_left_exp, bad_right_to_left_exp, 5000)

print("Failures: {0:10d}".format(fails))