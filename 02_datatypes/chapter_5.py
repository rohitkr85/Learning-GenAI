import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp = 95.5
current_temp = 95.49999999

print(f"Ideal team {ideal_temp}")
print(f"Current temp {current_temp}")
print(f"Difference temp {ideal_temp - current_temp}")

current_2nd_temp = 95.49

print(f"Difference temp {ideal_temp - current_2nd_temp}")
print(sys.float_info)