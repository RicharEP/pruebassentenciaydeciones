def es_palindromo(cadena):
    cadena = cadena.lower().replace(" ", "")
    return cadena == cadena[::-1]
