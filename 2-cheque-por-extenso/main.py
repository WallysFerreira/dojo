def cheque(numero):
    unidade = ["um", "dois", "tres", "quatro", "cinco", "seis", "sete", "oito", "nove"]
    dezenaDoDez = ["dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
    dezena = ["vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]
    centena = ["cem", "cento", "duzentos", "trezentos", "quatrocentos", "quinhentos", "seiscentos", "setecentos", "oitocentos", "novecentos"]

    num = int(numero // 1)
    numString = str(num)
    decString = str(dec)
    dec = numero % 1 
    indexDezDec = decString[2]
    indexUniDec = decString[3]

    # Unidade (ex: 3)
    if (len(numString) == 1):
        if (dec):
            if (int(indexDezDec) != 0):
                if (int(indexDezDec) == 1):
                    return unidade[num - 1] + " reais e " + dezenaDoDez[int(indexUniDec) + 1] + " centavos"
            else:
                return unidade[num - 1] + " reais e " + unidade[int(indexUniDec) - 1] + " centavos"
        else:
            return unidade[num - 1] + " reais"

    # Dezena (ex: 65)
    elif (len(numString) == 2):
        if (num < 20):
            return dezenaDoDez[num - 10] + " reais"
        else:
            if (numString[1] == "0"):
                indexDez = int(numString[0])
                return dezena[indexDez - 2] + " reais"
            else:
                indexDez = int(numString[0])
                indexUni = int(numString[1])

                return dezena[indexDez - 2] + " e " + unidade[indexUni - 1] + " reais"

    # Centena (ex: 432)
    elif (len(numString) == 3):
        if (num == 100):
            return centena[0] + " reais"
        elif (numString[1] == '0' and numString[2] == '0'):
            return centena[int(numString[0])] + " reais"
        elif (numString[2] == '0'):
            indexCen = int(numString[0])
            indexDez = int(numString[1])

            return centena[indexCen] + " e " + dezena[indexDez - 2] + " reais"
        elif (numString[1] == '0'):
            indexCen = int(numString[0])
            indexUni = int(numString[2])

            return centena[indexCen] + " e " + unidade[indexUni - 1] + " reais"        
        else:
            indexCen = int(numString[0])
            indexDez = int(numString[1])
            indexUni = int(numString[2])
            
            return centena[indexCen] + " e " + dezena[indexDez - 2] + " e " + unidade[indexUni - 1] + " reais"
           
    # Unidade de milhar (ex: 7130)
    elif (len(numString) == 4):
        if (numString[3] == '0' and numString[2] == '0' and numString[1] == '0'):
            if (numString[0] == '1'):
                return "mil reais"
            else:
                return unidade[int(numString[0]) - 1] + " mil reais"
        elif (numString[3] == '0' and numString[2] == '0'):
            indexUniMil = int(numString[0])
            indexCen = int(numString[1])

            return unidade[indexUniMil - 1] + " mil e " + centena[indexCen] + " reais"

        elif (numString[3] == '0'):
            indexUniMil = int(numString[0])
            indexCen = int(numString[1])
            indexDez = int(numString[2])

            if (indexDez == 1):
                return unidade[indexUniMil - 1] + " mil " + centena[indexCen] + " e " + dezenaDoDez[0] + " reais"
            else:
                return unidade[indexUniMil - 1] + " mil " + centena[indexCen] + " e " + dezena[indexDez - 2] + " reais"

        else:
            indexUniMil = int(numString[0])
            indexCen = int(numString[1])
            indexDez = int(numString[2])
            indexUni = int(numString[3])
            
            if (indexDez == 1):
                return unidade[indexUniMil - 1] + " mil " + centena[indexCen] + " e " + dezenaDoDez[indexUni] + " reais"
            elif (indexUni == 0):
                return unidade[indexUniMil - 1] + " mil " + centena[indexCen] + " e " + dezena[indexDez - 2] + " reais"
            else:
                return unidade[indexUniMil - 1] + " mil " + centena[indexCen] + " e " + dezena[indexDez - 2] + " e " + unidade[indexUni - 1] + " reais"
