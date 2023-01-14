def cheque(num):
    unidade = ["um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenaDoDez = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezena = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centena = ["cem", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

    numString = str(num)

    if (len(numString) == 1):
        return unidade[num - 1]
    elif (len(numString) == 2):
        if (num < 20):
            return dezenaDoDez[num - 10]
        else:
            if (numString[1] == "0"):
                index = int(numString[0])
                return dezena[index - 2]
            else:
                index1 = int(numString[0])
                index2 = int(numString[1])

                return dezena[index1 - 2] + " e " + unidade[index2 - 1]
    elif (len(numString) == 3):
        if (num == 100):
            return centena[0]
        elif