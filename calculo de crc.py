def calcular_crc(data, generador):
    # Convertir data y generador a listas de bits
    data_bits = [int(bit) for bit in data]
    generador_bits = [int(bit) for bit in generador]
    
    # Agregar ceros al final de los datos
    data_bits.extend([0] * (len(generador_bits) - 1))
    
    # Dividir datos por generador
    for i in range(len(data)):
        if data_bits[i] == 1:
            for j in range(len(generador_bits)):
                data_bits[i + j] ^= generador_bits[j]
    
    # Extraer el residuo (CRC)
    crc = data_bits[-(len(generador_bits) - 1):]
    return ''.join(str(bit) for bit in crc)

# Programa principal
print("Cálculo de CRC")
data = input("Ingrese los datos en formato binario (por ejemplo, 1101011011): ")
generador = input("Ingrese el generador en formato binario (por ejemplo, 10011): ")

crc = calcular_crc(data, generador)
print(f"El CRC calculado es: {crc}")