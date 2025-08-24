# Mini-proyecto
## Descripción
Este programa procesa un mensaje de texto en base a reglas de costos y transformación de palabras.  
Utiliza un archivo de configuración (**contenido.txt**) y un archivo de entrada (**mensaje.txt**) para calcular el costo total del mensaje y generar una versión transformada del mismo.

## Archivos requeridos
1. **Sin título0.py**: Script principal en Python.  
2. **contenido.txt**: Archivo de configuración que contiene:  
   ```
   M
   costo_palabra_corta
   costo_palabra_larga
   costo_infinitivo
   ```
Donde:
   - **M** = límite de caracteres para considerar una palabra como "corta".  
   - **costo_palabra_corta** = costo asignado a palabras de longitud menor o igual a M.  
   - **costo_palabra_larga** = costo asignado a palabras de longitud mayor a M.  
   - **costo_infinitivo** = costo asignado a verbos terminados en **-ar, -er, -ir**.  

3. **mensaje.txt**: Contiene el mensaje a evaluar y transformar.

## Funcionalidades
**Calcular costos**: El programa analiza cada palabra del mensaje y suma el costo correspondiente según las reglas.  
**Transformar mensaje**: Aplica las siguientes reglas:  
  - Las palabras largas se acortan a **M-1 caracteres** y se les añade `#`.  
  - Si el mensaje termina en punto (`.`), se reemplaza por la palabra `END`.
## Ejecución
1. Guardar los archivos en la misma carpeta.  
2. Ejecutar el script con Python 3:  
3. La salida mostrará:  
   - **Costo total del mensaje**  
   - **Mensaje transformado**

