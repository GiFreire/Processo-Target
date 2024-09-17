def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

string = input("Digite uma string para inverter: ")

resultado = inverter_string(string)
print("String invertida:", resultado)
