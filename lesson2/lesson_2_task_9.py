var_1 = 37
var_2 = 99
print(f'var_1 = {var_1}, var_2 = {var_2}')
# var_3 = var_1 # временная переменная
# var_1 = var_2
# var_2 = var_3
var_1, var_2 = var_2,var_1
print(f'var_1 = {var_1}, var_2 = {var_2}')