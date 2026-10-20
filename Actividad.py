"""Operaciones aritméticas, relacionales y lógicas."""


def leer_numero(mensaje):
    """Solicita un número hasta que el dato ingresado sea válido."""
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("Error: ingrese un número válido.")


def leer_booleano(mensaje):
    """Solicita un valor lógico usando si/no."""
    while True:
        respuesta = input(mensaje).strip().lower()
        if respuesta in ("si", "sí", "s", "true", "verdadero"):
            return True
        if respuesta in ("no", "n", "false", "falso"):
            return False
        print("Error: responda si o no.")


def mostrar_resultados(numero1, numero2, valor1, valor2):
    """Muestra los resultados de las operaciones solicitadas."""
    print("\n--- Operaciones aritméticas ---")
    print(f"Suma: {numero1} + {numero2} = {numero1 + numero2}")
    print(f"Resta: {numero1} - {numero2} = {numero1 - numero2}")
    print(f"Multiplicación: {numero1} * {numero2} = {numero1 * numero2}")

    if numero2 != 0:
        print(f"División: {numero1} / {numero2} = {numero1 / numero2}")
        print(f"División entera: {numero1} // {numero2} = {numero1 // numero2}")
        print(f"Resto: {numero1} % {numero2} = {numero1 % numero2}")
    else:
        print("División, división entera y resto: no se puede dividir entre cero.")

    print(f"Potencia: {numero1} ** {numero2} = {numero1 ** numero2}")

    print("\n--- Operaciones relacionales ---")
    print(f"{numero1} > {numero2}: {numero1 > numero2}")
    print(f"{numero1} < {numero2}: {numero1 < numero2}")
    print(f"{numero1} >= {numero2}: {numero1 >= numero2}")
    print(f"{numero1} <= {numero2}: {numero1 <= numero2}")
    print(f"{numero1} == {numero2}: {numero1 == numero2}")
    print(f"{numero1} != {numero2}: {numero1 != numero2}")

    print("\n--- Operaciones lógicas ---")
    print(f"{valor1} and {valor2}: {valor1 and valor2}")
    print(f"{valor1} or {valor2}: {valor1 or valor2}")
    print(f"not {valor1}: {not valor1}")
    print(f"not {valor2}: {not valor2}")


def main():
    print("=== OPERACIONES EN PYTHON ===")
    numero1 = leer_numero("Ingrese el primer número: ")
    numero2 = leer_numero("Ingrese el segundo número: ")
    valor1 = leer_booleano("Ingrese el primer valor lógico (si/no): ")
    valor2 = leer_booleano("Ingrese el segundo valor lógico (si/no): ")

    mostrar_resultados(numero1, numero2, valor1, valor2)


if __name__ == "__main__":
    main()
