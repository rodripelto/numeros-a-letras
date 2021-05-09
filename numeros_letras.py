def unidades(numero):
    unidad = {0:"",1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco",6:"seis",7:"siete",8:"ocho",9:"nueve"}
    return unidad[numero]

def decenas(numero):
    letras=""
    ldecenas = {10:"diez",11:"once",12:"doce",13:"trece",14:"cartoce",15:"quince",16:"dieci",20:"veinte",21:"veinti"}
    ldecenas.update({30:"treinta",40:"cuarenta",50:"cincuenta",60:"sesenta",70:"setenta",80:"ochenta",90:"noventa"})
    resto = numero % 10
    decena = numero - resto
    if numero < 10 :
        return unidades(numero)
    elif 10 <= numero <= 15:
        letras = ldecenas[numero]
    elif 16 <= numero <= 19:
        letras = ldecenas[16] + unidades (resto)
    elif numero == 20:
        letras = ldecenas[20]
    elif 21 <= numero <= 29:
        letras = ldecenas[21] + unidades (resto)
    elif 30<= numero and resto == 0:
        letras += ldecenas[decena] + unidades(resto) 
    else:
        letras += ldecenas[decena] + " y " + unidades(resto)   
    return letras

def centenas(numero):
    letras =""
    resto = numero % 100
    if numero < 100:
        letras = decenas(numero)
    elif numero == 100:
        letras = "cien"
    elif 101 <= numero <= 199:
        letras = "ciento " + decenas(resto)
    elif 200 <= numero <= 499 or 600 <= numero <= 699 or 800 <= numero <=899:
        letras = unidades(numero // 100) + "cientos " + decenas(resto)
    elif 500 <= numero <= 599:
        letras = "quinientos " + decenas(resto)
    elif 700 <= numero <= 799:
        letras = "setecientos " + decenas(resto)
    elif 900 <= numero <= 999:
        letras = "novecientos " + decenas(resto)
    return letras

def millares(numero):
    resto = numero % 1000
    millar = numero // 1000
    if numero < 1000:
        letras = centenas(numero)
    elif 1000 <= numero <=1999:
        letras = "mil " + centenas(resto)
    elif 2000 <= numero <= 99999:
        letras = decenas(millar) + " mil " + centenas(resto)
    return letras

def numero_letra(numero):
    prefijo=""
    if numero == 0:
        return "Cero"
    elif numero < 0:
        prefijo = "Menos "
        numero *= -1
    elif numero >= 100000:
        return "Lo siento no se contar hasta ese número"
    letras = prefijo + millares(numero)
    return letras.capitalize()

while (numero := input("Introduzca un número: "))!="":
    print(numero_letra(int(numero)))
    


