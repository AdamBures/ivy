from typing import Union, Optional, Tuple, List
from numbers import Number
import mxnet as mx

from ivy.utils.exceptions import IvyNotImplementedException


def sinc(
    x: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def fmax(
    x1: Union[(None, mx.ndarray.NDArray)],
    x2: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def fmin(
    x1: Union[(None, mx.ndarray.NDArray)],
    x2: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def trapz(
    y: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    x: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
    dx: float = 1.0,
    axis: int = (-1),
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def float_power(
    x1: Union[(None, mx.ndarray.NDArray, float, list, tuple)],
    x2: Union[(None, mx.ndarray.NDArray, float, list, tuple)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def exp2(
    x: Union[(None, mx.ndarray.NDArray, float, list, tuple)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def copysign(
    x1: Union[(None, mx.ndarray.NDArray, Number)],
    x2: Union[(None, mx.ndarray.NDArray, Number)],
    /,
    *,
    out: Optional[None] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def count_nonzero(
    a: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    axis: Optional[Union[(int, Tuple[(int, ...)])]] = None,
    keepdims: bool = False,
    dtype: Optional[None] = None,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def nansum(
    x: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    axis: Optional[Union[(Tuple[(int, ...)], int)]] = None,
    dtype: Optional[None] = None,
    keepdims: bool = False,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def gcd(
    x1: Union[(None, mx.ndarray.NDArray, int, list, tuple)],
    x2: Union[(None, mx.ndarray.NDArray, float, list, tuple)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def isclose(
    a: Union[(None, mx.ndarray.NDArray)],
    b: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    rtol: float = 1e-05,
    atol: float = 1e-08,
    equal_nan: bool = False,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def nan_to_num(
    x: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    copy: bool = True,
    nan: Union[(float, int)] = 0.0,
    posinf: Optional[Union[(float, int)]] = None,
    neginf: Optional[Union[(float, int)]] = None,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def logaddexp2(
    x1: Union[(None, mx.ndarray.NDArray, float, list, tuple)],
    x2: Union[(None, mx.ndarray.NDArray, float, list, tuple)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def signbit(
    x: Union[(None, mx.ndarray.NDArray, float, int, list, tuple)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def hypot(
    x1: Union[(None, mx.ndarray.NDArray)],
    x2: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def allclose(
    x1: Union[(None, mx.ndarray.NDArray)],
    x2: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    rtol: float = 1e-05,
    atol: float = 1e-08,
    equal_nan: bool = False,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> bool:
    raise IvyNotImplementedException()


def fix(
    x: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def nextafter(
    x1: Union[(None, mx.ndarray.NDArray)],
    x2: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def diff(
    x: Union[(None, mx.ndarray.NDArray, list, tuple)],
    /,
    *,
    n: int = 1,
    axis: int = (-1),
    prepend: Optional[
        Union[(None, mx.ndarray.NDArray, int, float, list, tuple)]
    ] = None,
    append: Optional[Union[(None, mx.ndarray.NDArray, int, float, list, tuple)]] = None,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def angle(
    input: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    deg: Optional[bool] = None,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def imag(
    val: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def zeta(
    x: Union[(None, mx.ndarray.NDArray)],
    q: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def gradient(
    x: None,
    /,
    *,
    spacing: Union[(int, list, tuple)] = 1,
    axis: Optional[Union[(int, list, tuple)]] = None,
    edge_order: int = 1,
) -> Union[(None, List[None])]:
    raise IvyNotImplementedException()


def xlogy(
    x: Union[(None, mx.ndarray.NDArray)],
    y: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def real(
    x: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def conj(
    x: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def ldexp(
    x1: Union[(None, mx.ndarray.NDArray)],
    x2: Union[(None, mx.ndarray.NDArray, int)],
    /,
    *,
    out: Optional[Union[(None, mx.ndarray.NDArray)]] = None,
) -> Union[(None, mx.ndarray.NDArray)]:
    raise IvyNotImplementedException()


def frexp(
    x: Union[(None, mx.ndarray.NDArray)],
    /,
    *,
    out: Optional[
        Union[(Tuple[(None, None)], Tuple[(mx.ndarray.NDArray, mx.ndarray.NDArray)])]
    ] = None,
) -> Union[(Tuple[(None, None)], Tuple[(mx.ndarray.NDArray, mx.ndarray.NDArray)])]:
    raise IvyNotImplementedException()
