from typing import List
from models.equation import Equation


class ProblemModel:
    def __init__(
        self,
        prob_eq: Equation,
        const_eqs: List[Equation],
        is_max: bool = True,
        has_def_const: bool = False,
    ) -> None:
        self._is_max = is_max
        self._prob_eq = prob_eq
        self._const_eqs = const_eqs
        self._has_def_const = has_def_const

    def get_is_max(self) -> bool:
        return self._is_max

    def set_is_max(self, is_max: bool) -> None:
        self._is_max = is_max

    def get_prob_eq(self) -> Equation:
        return self._prob_eq

    def set_prob_eq(self, prob_eq: Equation) -> None:
        self._prob_eq = prob_eq

    def get_const_eqs(self) -> List[Equation]:
        return self._const_eqs

    def set_const_eqs(self, const_eqs: List[Equation]) -> None:
        self._const_eqs = const_eqs

    def get_has_def_const(self) -> bool:
        return self._has_def_const

    def set_has_def_const(self, has_def_const: bool) -> None:
        self._has_def_const = has_def_const

    is_max: bool = property(get_is_max, set_is_max)
    prob_eq: Equation = property(get_prob_eq, set_prob_eq)
    const_eqs: List[Equation] = property(get_const_eqs, set_const_eqs)
    has_def_const: bool = property(
        get_has_def_const, set_has_def_const,
    )
