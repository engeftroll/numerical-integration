from sympy import Expr, parse_expr
from logging import Logger

import matplotlib.pyplot as plt


class MathFunction:
    """Кастомный класс, чтобы упростить себе жизнь в решениях ниже"""

    def __init__(self, entered_function: str):
        self.equation: Expr = parse_expr(entered_function)
    
    def __call__(self, *args, **kwds) -> float:
        """На вход подаются аргументы, которые надо заменить на числа"""
        return self.equation.evalf(subs=kwds)
    
    def get_derivative(self, *args) -> "MathFunction":
        return MathFunction(str(self.equation.diff(*args)))
    
    def __repr__(self):
        return f"<MathFunction expr=[{self.equation}]>"


class NumericalIntegration:
    method_name = "Method name"

    def __init__(self, raw_function: str, integrate_from: float, integrate_to: float, precise_answer: float, logger: Logger):
        self.raw_function: str = raw_function
        self.function: MathFunction = MathFunction(raw_function)
        self.logger = logger
        self.integrate_from: float = integrate_from
        self.integrate_to: float = integrate_to
        self.precise_answer = precise_answer

    def get_step(self, amount_of_intervals: int):
        """Равномерный шаг"""
        return (self.integrate_to - self.integrate_from) / amount_of_intervals
    
    def count_i_sum_element(self, x_prev: float, x_next: float):
        """Требуется реализация в конкретном методе"""
        return 0

    def solve(self, amount_of_intervals: int) -> float:
        total_summary = 0
        delta = self.get_step(amount_of_intervals)
        self.logger.info(f"--= SOLVING INTEGRAL (method '{self.method_name}') =--")
        self.logger.info(f"h = {delta}")

        i = 0
        x_prev = self.integrate_from
        x_next = x_prev + delta
        
        while x_prev <= self.integrate_to:
            temporary_result = self.count_i_sum_element(x_prev, x_next)
            total_summary += temporary_result

            self.logger.info(f"x_{i} = {x_prev}; x_{i+1} = {x_next}; sum += {temporary_result}")
            
            i += 1
            x_prev = x_next
            x_next = x_prev + delta

        self.logger.info(f"I* = {total_summary}")
        self.logger.info(f"I_precise = {self.precise_answer}")
        self.logger.info("--= END SOLVING INTEGRAL =--")
        return total_summary


    def show_graphics(self, from_n: int = 100, to_n: int = 500, step: int = 10):
        input_n_list = list()
        output_result_list = list()

        for n in range(from_n, to_n, step):
            result = self.solve(n)

            input_n_list.append(n)
            output_result_list.append(abs(self.precise_answer - result))
        
        plt.plot(input_n_list, output_result_list)
        plt.xlabel("Количество интервалов")
        plt.ylabel("|I* - I_precise|")
        plt.title(self.method_name)
        plt.show()

        return
