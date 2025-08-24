def cargarDatos(contenido):
    """
    Recibe el contenido del archivo de configuración como string.
    Ejemplo:
    "10\n0.2\n0.5\n0.3"
    """
    lineas = contenido.strip().splitlines()
    M = int(lineas[0])
    corta = float(lineas[1])
    larga = float(lineas[2])
    infinitivo = float(lineas[3])

    return {"M": M, "Corta": corta, "Larga": larga, "Infinitivo": infinitivo}


def calcularCostos(datos, contenido):
    """
    Calcula el costo total del mensaje a partir de un string que contiene el mensaje.
    """
    M = datos["M"]
    costo_total = 0.0

    lineas = contenido.strip().splitlines()

    for linea in lineas:
        palabras = linea.strip().split()
        for palabra in palabras:
            if palabra.endswith("."):
                palabra = palabra[:-1]

            if palabra.lower().endswith(("ar", "er", "ir")):
                costo_total += datos["Infinitivo"]
            elif len(palabra) <= M:
                costo_total += datos["Corta"]
            else:
                costo_total += datos["Larga"]

    return costo_total


def cambiarMensaje(datos, contenido):
    """
    Genera un nuevo mensaje aplicando las reglas:
    - Palabras largas se acortan a M-1 caracteres y se añade '#'
    - El punto final se reemplaza con 'END'
    Retorna el nuevo mensaje como string.
    """
    M = datos["M"]

    lineas = contenido.strip().splitlines()
    nuevo_mensaje = []

    total_lineas = len(lineas)
    for i in range(total_lineas):
        linea = lineas[i]
        palabras = linea.strip().split()
        nuevas_palabras = []
        total_palabras = len(palabras)

        j = 0
        while j < total_palabras:
            palabra = palabras[j]

            # última palabra del mensaje
            if palabra.endswith(".") and i == total_lineas - 1 and j == total_palabras - 1:
                nuevas_palabras.append("END")
            else:
                if palabra.endswith("."):
                    palabra = palabra[:-1]

                if len(palabra) > M:
                    palabra = palabra[:M-1] + "#"

                nuevas_palabras.append(palabra)
            j += 1

        nuevo_mensaje.append(" ".join(nuevas_palabras))

    return "\n".join(nuevo_mensaje)


# ============================
# Ejemplo de uso (sin archivos)
# ============================
if __name__ == "__main__":
    # Contenido de los "archivos"
    costos_txt = "10\n0.2\n0.5\n0.3"
    mensaje_txt = "Hola este es un mensaje para probar enviar comunicar programar."

    # Cargar datos
    datos = cargarDatos(costos_txt)

    # Calcular costo
    costo = calcularCostos(datos, mensaje_txt)
    print("Costo total del mensaje: $", costo)

    # Cambiar mensaje
    nuevo_mensaje = cambiarMensaje(datos, mensaje_txt)
    print("Mensaje transformado:\n", nuevo_mensaje)
