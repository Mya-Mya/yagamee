from typing import Callable,Tuple
import sigfig
import re

Format = Callable[[float | int], str]

exp_regex: re.Pattern = re.compile(r".*[eE]([+-]?)(\d+)")

def parse_exp_expr(x:str)->Tuple[str, int]:
    match = exp_regex.match(x)
    if match:
        sign: str = match.group(1)
        exponent: str = match.group(2)
        exp_expr_len: int = len(exponent)+len(sign)+1
        return x[:-exp_expr_len], int(exponent)*(-1 if sign == "-" else 1)
    else:
        return x, 0

def latexify_exp_expr(x: str) -> str:
    mantissa, exponent = parse_exp_expr(x)
    if exponent == 0:
        return mantissa
    else:
        return mantissa + r"\\times 10^{" + str(exponent) + "}"


def create_f_format(digits: str) -> Format:
    return lambda x: ("{:."+str(digits)+"f}").format(x)


def create_g_format(digits: str) -> Format:
    return lambda x: ("{:."+str(digits)+"g}").format(x)


def create_e_format(digits: str) -> Format:
    return lambda x: ("{:."+str(digits)+"e}").format(x)


def create_sigfig_format(digits: str) -> Format:
    return lambda x: sigfig.round(str(x), sigfigs=int(digits))


def create_latexified_e_format(digits: str) -> Format:
    e_format: Format = create_e_format(digits)

    def format(x):
        e_formatted: str = e_format(x)
        latexified: str = latexify_exp_expr(e_formatted)
        return latexified

    return format

def create_latexified_g_format(digits: str) -> Format:
    g_format: Format = create_g_format(digits)

    def format(x):
        g_formatted: str = g_format(x)
        latexified: str = latexify_exp_expr(g_formatted)
        return latexified

    return format