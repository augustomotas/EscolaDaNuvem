# --- Combustível

distancia = 300 #km
combustivel = 25 #litros

consumo_medio = distancia / combustivel #kml

print("--- Relatório de Consumo da Viagem ---")
print(f"Distância percorrida: {distancia} km")
print(f"Combustível gasto: {combustivel} litros")
print("--------------------------------------")
print(f"Consumo médio: {consumo_medio:.2f} km/l")