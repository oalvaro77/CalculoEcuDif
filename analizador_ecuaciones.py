import re
from typing import Tuple, Dict

def analizar_ecuacion(ecuacion: str) -> Dict:
    """
    Analiza una ecuación diferencial y determina su tipo, orden y linealidad.
    
    Args:
        ecuacion (str): La ecuación diferencial en formato de string
        
    Returns:
        Dict: Diccionario con las características de la ecuación
    """
    # Limpiar la ecuación de espacios
    ecuacion = ecuacion.replace(" ", "")
    
    # Determinar el tipo
    tipo = determinar_tipo(ecuacion)
    
    # Determinar el orden
    orden = determinar_orden(ecuacion)
    
    # Determinar la linealidad
    linealidad = determinar_linealidad(ecuacion)
    
    return {
        "tipo": tipo,
        "orden": orden,
        "linealidad": linealidad
    }

def determinar_tipo(ecuacion: str) -> str:
    """
    Determina si la ecuación es ordinaria o parcial.
    """
    if "∂" in ecuacion or "∂y/∂x" in ecuacion:
        return "Parcial"
    return "Ordinaria"

def determinar_orden(ecuacion: str) -> int:
    """
    Determina el orden de la ecuación diferencial.
    """
    # Buscar derivadas de orden superior
    patrones = [
        r"d\^(\d+)y/dx\^\d+",  # Para dy/dx, d²y/dx², etc.
        r"y\^\((\d+)\)",       # Para y(1), y(2), etc.
        r"y'*",                # Para y', y'', y''', etc.
    ]
    
    max_orden = 0
    for patron in patrones:
        coincidencias = re.findall(patron, ecuacion)
        if coincidencias:
            if patron == r"y'*":
                # Para el caso de comillas, contar el número de comillas en cada coincidencia
                for coincidencia in coincidencias:
                    orden = coincidencia.count("'")
                    max_orden = max(max_orden, orden)
            else:
                ordenes = [int(x) for x in coincidencias]
                max_orden = max(max_orden, max(ordenes))
    
    return max_orden if max_orden > 0 else 1

def determinar_linealidad(ecuacion: str) -> str:
    """
    Determina si la ecuación es lineal o no lineal.
    """
    # Verificar términos no lineales
    terminos_no_lineales = [
        r"y\^2",      # y²
        r"y\^3",      # y³
        r"sin\(y\)",  # sin(y)
        r"cos\(y\)",  # cos(y)
        r"e\^y",      # e^y
        r"ln\(y\)",   # ln(y)
        r"y\*y",      # y*y
        r"y/y"        # y/y
    ]
    
    for termino in terminos_no_lineales:
        if re.search(termino, ecuacion):
            return "No lineal"
    
    return "Lineal"

def main():
    print("Analizador de Ecuaciones Diferenciales")
    print("--------------------------------------")
    
    while True:
        ecuacion = input("\nIngrese la ecuación diferencial (o 'salir' para terminar): ")
        
        if ecuacion.lower() == 'salir':
            break
            
        try:
            resultado = analizar_ecuacion(ecuacion)
            print("\nResultados del análisis:")
            print(f"Tipo: {resultado['tipo']}")
            print(f"Orden: {resultado['orden']}")
            print(f"Linealidad: {resultado['linealidad']}")
        except Exception as e:
            print(f"Error al analizar la ecuación: {str(e)}")

if __name__ == "__main__":
    main() 