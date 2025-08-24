def cargarDatos(ruta="contenido.txt"):
    """
    Lee el archivo de configuración
    y devuelve el diccionario de datos.
    """
    with open(ruta, "r", encoding="utf-8") as f:
        contenido = f.read()

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


if __name__ == "__main__":
    datos = cargarDatos("contenido.txt")

    with open("mensaje.txt", "r", encoding="utf-8") as f:
        mensaje_txt = f.read()

    costo = calcularCostos(datos, mensaje_txt)
    print("Costo total del mensaje: $", costo)

    nuevo_mensaje = cambiarMensaje(datos, mensaje_txt)
    print("Mensaje transformado:\n", nuevo_mensaje)



