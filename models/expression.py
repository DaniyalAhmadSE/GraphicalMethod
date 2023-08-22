from typing import List

from models.term import Term


class Expression:
    def __init__(
        self,
        terms: List[Term],
        consts: List[float],
    ) -> None:
        self._terms = terms
        self._constants = consts

    def get_terms(self) -> List[Term]:
        return self._terms

    def set_terms(self, terms: List[float]) -> None:
        self._terms = terms

    def get_sign(self) -> str:
        return self._sign

    def set_sign(self, sgn: str) -> None:
        self._sign = sgn

    def get_constants(self) -> List[float]:
        return self._constants

    def set_constants(self, consts: List[float]) -> None:
        self._constants = consts

    def get_term(self, i: int) -> Term:
        return self._terms[i]

    def set_term(self, term: float, i: int) -> None:
        self._terms[i] = term

    def get_constant(self, i: int = 0) -> float:
        return self._constants[i]

    def set_constant(self, const: float, i: int = 0) -> None:
        self._constants[i] = const

    def get_has_z(self) -> bool:
        for each_t in self.terms:
            if each_t.var_name == 'z':
                return True
        return False

    terms: List[Term] = property(get_terms, set_terms)
    sign: str = property(get_sign, set_sign)
    constants: List[float] = property(get_constants, set_constants)
    constant: float = property(get_constant, set_constant)
    has_z: float = property(get_has_z)
