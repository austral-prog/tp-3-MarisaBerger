def check_vowels():
    # Código a implementar utilizando input.
    texto = input("Ingresa tu nombre: ").lower()
    print("Contiene a: " + str("a" in texto))
    print("Contiene e: " + str("e" in texto))
    print("Contiene i: " + str("i" in texto))
    print("Contiene o: " + str("o" in texto))
    print("Contiene u: " + str("u" in texto))

# Para verificar este ejercicio ejecutar el comando
# `pytest tp3_in_string_test.py` o `python tp3_in_string_test.py`


