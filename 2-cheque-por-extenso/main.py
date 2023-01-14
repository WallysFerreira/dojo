def cheque(num):
    unidade = ["um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenaDoDez = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezena = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centena = ["cem", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

    numString = str(num)

    if (len(numString) == 1):
        return unidade[num - 1] + " reais"
    elif (len(numString) == 2):
        if (num < 20):
            return dezenaDoDez[num - 10] + " reais"
        else:
            if (numString[1] == "0"):
                index = int(numString[0])
                return dezena[index - 2] + " reais"
            else:
                index1 = int(numString[0])
                index2 = int(numString[1])

                return dezena[index1 - 2] + " e " + unidade[index2 - 1] + " reais"
    elif (len(numString) == 3):
        if (num == 100):
            return centena[0] + " reais"
        elif (numString[2] == '0'):
            index1 = int(numString[0])
            index2 = int(numString[1])

            return centena[index1] + " e " + dezena[index2 - 2] + " reais"
        elif (numString[1] == '0'):
            index1 = int(numString[0])
            index2 = int(numString[2])

            return centena[index1] + " e " + unidade[index2 - 1] + " reais"        
        else:
            index1 = int(numString[0])
            index2 = int(numString[1])
            index3 = int(numString[2])
            
            return centena[index1] + " e " + dezena[index2 - 2] + " e " + unidade[index3 - 1] + " reais"
           