# Расчет уставки токовой отсечки с накоплением коэффициентов.
from pymonad.tools import curry
from pymonad.state import State

calc_init = {'I_kz_max': 1000.0, 'result': 1.0, 'steps': []}
calc = State.insert(calc_init)

@curry(2)
def apply_coeff(coeff_name, state):
    def calc_op(_):
        coeffs = {'k_otstr': 1.2, 'k_zap': 1.3, 'k_sh': 1.1}
        
        if coeff_name in coeffs:
            new_result = state['result'] * coeffs[coeff_name]
            return {
                **state,
                'result': new_result,
                'steps': state['steps'] + [coeff_name]
            }
        return state
    return State(calc_op)

calculation = (calc
    .then(apply_coeff('k_otstr'))
    .then(apply_coeff('k_zap'))
    .then(apply_coeff('k_sh'))
)

final = calculation.run(calc_init)
