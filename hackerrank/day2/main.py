

import math
import os
import random
import re
import sys



def solve(meal_cost, tip_percent, tax_percent):
    
    comida = meal_cost
    propina = meal_cost * (tip_percent/100)
    inpuesto = meal_cost * (tax_percent/100)

    total = comida + propina + inpuesto
    
    print(f'total a pagar: {round(total)}')
    
if __name__ == '__main__':
    meal_cost = float(input("comida: ").strip())

    tip_percent = int(input("propina: ").strip())

    tax_percent = int(input("inpuesto: ").strip())

    solve(meal_cost, tip_percent, tax_percent)
