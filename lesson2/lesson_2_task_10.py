def bank(first_deposit_rub,deposit_term_in_years):
    percentOneYear = 0.1           # 10%
    for result in range(deposit_term_in_years):
        first_deposit_rub += first_deposit_rub * percentOneYear  
    return first_deposit_rub

print(bank(50, 5))
