from numerical_integration import NumericalIntegration
import matplotlib.pyplot as plt


class LeftRectangles(NumericalIntegration):
    method_name = "LeftRectangles"
    def count_i_sum_element(self, x_prev: float, x_next: float):
        return self.function(x=x_prev) * (x_next - x_prev)


class RightRectangles(NumericalIntegration):
    method_name = "RightRectangles"

    def count_i_sum_element(self, x_prev: float, x_next: float):
        return self.function(x=x_next) * (x_next - x_prev)


class MediumRectangles(NumericalIntegration):
    method_name = "MediumRectangles"

    def count_i_sum_element(self, x_prev, x_next):
        return self.function(x=(x_prev + x_next) / 2) * (x_next - x_prev)


class Trapezoids(NumericalIntegration):
    method_name = "Trapezoids"

    def count_i_sum_element(self, x_prev, x_next):
        return (self.function(x=x_next) + self.function(x=x_prev)) / 2 * (x_next - x_prev)


class Paraboloids(NumericalIntegration):
    method_name = "Paraboloids"

    def count_i_sum_element(self, x_prev, x_next):
        return 1/6 * (
            self.function(x=x_prev) + 
            4 * self.function(x=(x_next + x_next) / 2) +
            self.function(x=x_next)
            ) * (x_next - x_prev)
