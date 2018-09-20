import random


def fluky(good_val, bad_val, gen_bad, p):
    if not gen_bad:
        return good_val
    r = random.random()
    if r <= p:
        return bad_val
    else:
        return good_val
