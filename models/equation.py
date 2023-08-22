from typing import List
from models.expression import Expression


class Equation:
    def __init__(
        self,
        l_exp: Expression,
        r_exp: Expression,
        const: float,
        is_ineq_gt: bool = False,
        is_ineq_lt: bool = False,
        is_z: bool = False,
    ) -> None:
        self._l_exp = l_exp
        self._r_exp = r_exp
        self._is_ineq_gt = is_ineq_gt
        self._is_ineq_lt = is_ineq_lt
        self._constant = const
        self._is_z = is_z

    def get_l_exp(self) -> Expression:
        return self._l_exp

    def set_l_exp(self, l_exp: Expression) -> None:
        self._l_exp = l_exp

    def get_r_exp(self) -> Expression:
        return self._r_exp

    def set_r_exp(self, r_exp: Expression) -> None:
        self._r_exp = r_exp

    def get_sign(self) -> str:
        return self._sign

    def set_sign(self, sgn: str) -> None:
        self._sign = sgn

    def get_constant(self) -> float:
        return self._constant

    def set_constant(self, const: float) -> None:
        self._constant = const

    def get_has_z(self) -> bool:
        return (self.l_exp.has_z or self.r_exp.has_z)

    l_exp: Expression = property(get_l_exp, set_l_exp)
    r_exp: Expression = property(get_r_exp, set_r_exp)
    sign: str = property(get_sign, set_sign)
    constant: float = property(get_constant, set_constant)
    has_z: float = property(get_has_z)
