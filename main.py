from pytest import main
from TuclaseExamen import TuclaseExamen

# create the class instance
obj = TuclaseExamen()

print(obj.arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49", "10 + 10"], True))

# Run unit tests automatically
main(['-vv'])
