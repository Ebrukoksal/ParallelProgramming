import sys

custom_power = lambda x=0, /, e=1: x ** e

def custom_equation(x: float = 0, y: float = 0, /, a: float = 1, b: float = 1, *, c: float = 1) -> float:
    """
    Computes a custom equation.

    :param x: positional-only, default 0
    :param y: positional-only, default 0
    :param a: positional or keyword, default 1
    :param b: positional or keyword, default 1
    :param c: keyword-only, default 1
    :return: result of (x**a + y**b) / c
    """
    return (x ** a + y ** b) / c

def fn_w_counter():
    if not hasattr(fn_w_counter, "count"):
        fn_w_counter.count = 0
        fn_w_counter.callers = {}
    
    fn_w_counter.count += 1
    caller = sys._getframe(1).f_globals.get('__name__', 'unknown')
    fn_w_counter.callers[caller] = fn_w_counter.callers.get(caller, 0) + 1
    
    return fn_w_counter.count, fn_w_counter.callers
