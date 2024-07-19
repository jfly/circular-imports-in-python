print(f"{__name__}: start")
from .lower_bound import pi_lower_bound
print(f"{__name__}: from foo.py: {pi_lower_bound=}")

pi_upper_bound = pi_lower_bound + 1
print(f"{__name__}: just set {pi_upper_bound=}")
