from logging import Logger
import logging

from methods import LeftRectangles, RightRectangles, MediumRectangles
from methods import Trapezoids, Paraboloids


logger = logging.getLogger("EQUATION LOGS")
logging.basicConfig(
    filename="integration.log", 
    format="%(levelname)s\t\t %(message)s", 
    filemode="w",
    level=logging.INFO
)

# leftRect = LeftRectangles("(x-1)/(x+1)**3", 0, 1, -0.25, logger)
# rightRect = RightRectangles("(x-1)/(x+1)**3", 0, 1, -0.25, logger)
# mediumRect = MediumRectangles("(x-1)/(x+1)**3", 0, 1, -0.25, logger)

# trapezoids = Trapezoids("(x-1)/(x+1)**3", 0, 1, -0.25, logger)
# paraboloids = Paraboloids("(x-1)/(x+1)**3", 0, 1, -0.25, logger)

leftRect = LeftRectangles("(6*x**2+15*x+2)/(x-2)/((x+2)**3)", 0, 1, -0.475175, logger)
rightRect = RightRectangles("(6*x**2+15*x+2)/(x-2)/((x+2)**3)", 0, 1, -0.475175, logger)
mediumRect = MediumRectangles("(6*x**2+15*x+2)/(x-2)/((x+2)**3)", 0, 1, -0.475175, logger)

trapezoids = Trapezoids("(6*x**2+15*x+2)/(x-2)/((x+2)**3)", 0, 1, -0.475175, logger)
paraboloids = Paraboloids("(6*x**2+15*x+2)/(x-2)/((x+2)**3)", 0, 1, -0.475175, logger)

# leftRect = LeftRectangles("(sin(x))/(sin(x)+1)**2", 0, 1.5708, 1/3, logger)
# rightRect = RightRectangles("(sin(x))/(sin(x)+1)**2", 0, 1.5708, 1/3, logger)
# mediumRect = MediumRectangles("(sin(x))/(sin(x)+1)**2", 0, 1.5708, 1/3, logger)

# trapezoids = Trapezoids("(sin(x))/(sin(x)+1)**2", 0, 1.5708, 1/3, logger)
# paraboloids = Paraboloids("(sin(x))/(sin(x)+1)**2", 0, 1.5708, 1/3, logger)

from_n = 1
to_n = 25
step = 1

leftRect.show_graphics(from_n, to_n, step)
rightRect.show_graphics(from_n, to_n, step)
mediumRect.show_graphics(from_n, to_n, step)

trapezoids.show_graphics(from_n, to_n, step)
paraboloids.show_graphics(from_n, to_n, step)
