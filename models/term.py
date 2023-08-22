class Term:
    def __init__(self, cof, v_name) -> None:
        self._coeff = cof
        self._var_name = v_name

    def get_coeff(self) -> int:
        return self._coeff

    def set_coeff(self, cof: int) -> None:
        self._coeff = cof

    def get_var_name(self) -> str:
        return self._var_name

    def set_var_name(self, v_name: str) -> None:
        self._var_name = v_name

    def get_str(self) -> str:
        return str(self._coeff) + self._var_name

    coeff = property(get_coeff, set_coeff)
    var_name = property(get_var_name, set_var_name)
