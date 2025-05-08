# Численное интегрирование
Задача: приближённо вычислить интеграл вида:

$$\int_a^b f(x) dx$$

1. Разбиваем $[a, b]$ на точки ${\{x_n\}}$, получив интервалы вида $[x_i, x_{i+1}]$. В каждой точке можем найти значение подынтегральной функции $f(x_i)$.

## Методы расчёта интеграла приближённо
### Методы прямоугольников
1. Формула левых прямоугольников
$$
\begin{equation}
\int_a^b f(x) dx \approx 
\sum_{i=0}^{n-1} f(x_i) (x_{i+1} - x_i)
\end{equation}
$$
2. Формула правых прямоугольников
$$
\begin{equation}
\int_a^b f(x) dx \approx 
\sum_{i=0}^{n-1} f(x_{i+1}) (x_{i+1} - x_i)
\end{equation}
$$

3. Формула cредних прямоугольников
$$
\begin{equation}
\int_a^b f(x) dx \approx 
\sum_{i=0}^{n-1} f(\frac{x_{i+1} + x_i}{2}) (x_{i+1} - x_i)
\end{equation}
$$

### Методы трапеций и парабол

1. Формула трапеций
$$
\begin{equation}
\int_a^b f(x) dx \approx 
\sum_{i=0}^{n-1} \frac{f(x_i) + f(x_{i+1})}{2} (x_{i+1} - x_i)
\end{equation}
$$

2. Формула парабол
$$
\begin{equation}
\int_a^b f(x) dx \approx 
\frac{1}{6} \sum_{i=0}^{n-1} ( f(x_i) + 4 f\Big(\frac{x_i + x_{i+1}}{2}\Big) + f(x_i)) (x_{i+1} - x_i)
\end{equation}
$$

