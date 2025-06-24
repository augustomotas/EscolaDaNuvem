# --- Calculadora de Desconto

nome_produto = "Camiseta"
preco_original = 50.00
percentual_desconto = 20

valor_do_desconto = preco_original * (percentual_desconto / 100)

preco_final = preco_original - valor_do_desconto

print("--- Detalhes da Compra com Desconto ---")
print(f"Produto: {nome_produto}")
print(f"Preço Original: R$ {preco_original:.2f}")
print(f"Desconto de {percentual_desconto}%: R$ {valor_do_desconto:.2f}")
print("---------------------------------------")
print(f"Preço Final a Pagar: R$ {preco_final:.2f}")