# --- Conversor de Moeda 

valor_em_reais = 100.00
taxa_dolar = 5.20
taxa_euro = 6.15

valor_em_dolares = valor_em_reais / taxa_dolar
valor_em_euros = valor_em_reais / taxa_euro

print("--- Resultado da Conversão ---")
print(f"Valor original: R$ {valor_em_reais:.2f}")
print("------------------------------")
print(f"Valor em Dólares: US$ {valor_em_dolares:.2f}")
print(f"Valor em Euros: € {valor_em_euros:.2f}")