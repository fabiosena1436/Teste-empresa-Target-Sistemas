# Para inverter uma string:

def inverter_string(texto):
    return texto[::-1]  # Método Pythônico
    
# Ou uma implementação manual:
def inverter_string_manual(texto):
    resultado = ""
    for i in range(len(texto)-1, -1, -1):
        resultado += texto[i]
    return resultado

texto = input("Digite um texto: ")
print(f"Texto invertido: {inverter_string_manual(texto)}")