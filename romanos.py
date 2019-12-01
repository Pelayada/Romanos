numerosRomanos = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "(IV)": 4000, "(V)": 5000, "(VI)": 6000, "(VII)": 7000, "(VIII)": 8000, "(IX)": 9000}
numerosRomanos5 = {"V": 5, "L": 50, "D": 500}
numerosOrdenados = ["I", "V", "X", "L", "C", "D", "M"]

numerosArabigos = {"1": "I", "5": "V", "10": "X", "50": "L", "100": "C", "500": "D", "1000": "M"}
unidadesArabigas = {"1": "I", "2": "II", "3": "III","4": "IV", "5": "V", "6": "VI","7":"VII", "8": "VIII", "9": "IX"}
decenasArabigas = {"10": "X", "20": "XX", "3": "XXX","40": "XL", "50": "L", "60": "LX","70":"LXX", "80": "LXXX", "90": "XC"}
centenasArabigas = {"100": "C", "200": "CC", "300": "CCC","400": "CD", "500": "D", "600": "DC","700":"DCC", "800": "DCCC", "900": "CM"}
millaresArabigos = {"1000": "M", "2000": "MM", "3000": "MMM","4000": "(IV)", "5000": "(V)", "6000": "(VI)","7000":"(VII)", "8000": "(VIII)", "9000": "(IX)"}

def cambiarArabigo(palabra):

        letraAnterior = ""
        acumRepet = 1
        sumaArabigo = 0
        for i in range(len(palabra)):

            if letraAnterior == palabra[i]:
                acumRepet += 1
                if acumRepet == 4:
                    return 0
            else:
                acumRepet = 1
                letraAnterior = palabra[i]

            letraActual = palabra[i]
            if i+1 == len(palabra):
                sumaArabigo += numerosRomanos[letraActual]
                return sumaArabigo
            else:
                letraSig = palabra[i+1]
                numActual = numerosRomanos[letraActual]
                numSig = numerosRomanos[letraSig]
                if numActual < numSig:
                    if palabra[i] in numerosRomanos5:
                        return 0
                    else:
                        sumaArabigo = sumaArabigo - numActual
                    if acumRepet == 2:
                        return 0
                    distancia = numerosOrdenados.index(letraSig) - numerosOrdenados.index(letraActual)
                    if distancia > 2:
                        return 0
                else:
                    sumaArabigo = sumaArabigo + numActual
        return sumaArabigo

def cambiarRomano(valor):
    result = ""
    valorDecena0 = "0"

    for i in range(len(valor)):
        if len(valor) == 1:
            numActual = valor[i]
            result += unidadesArabigas[numActual]
            return result
        elif len(valor) == 2:
            numDecenas = valor[i] + valorDecena0
            numUnidades = valor[i+1]
            result += (decenasArabigas[numDecenas] + unidadesArabigas[numUnidades])
            return result
        elif len(valor) == 3:
            numCentenas = valor[i] + valorDecena0*2
            numDecenas = valor[i+1] + valorDecena0
            numUnidades = valor[i+2]
            result += centenasArabigas[numCentenas] + decenasArabigas[numDecenas] + unidadesArabigas[numUnidades]
            return result
        else:
            numMillares = valor[i] + valorDecena0*3
            numCentenas = valor[i+1] + valorDecena0*2
            numDecenas = valor[i+2] + valorDecena0
            numUnidades = valor[i+3]
            result += millaresArabigos[numMillares] + centenasArabigas[numCentenas] + decenasArabigas[numDecenas] + unidadesArabigas[numUnidades]
            return result

def cambiarRomano2(valor):
    result = ""
    for i in range(len(valor)):
        
        if len(valor) == 4:
            numActual = int(valor[i])
            valorMillar = numerosArabigos["1000"]
            result += numActual * valorMillar
            
            numActual = int(valor[i+1])
            valorCentena5 = numerosArabigos["500"]
            valorCentena1 = numerosArabigos["100"]
            
            if numActual >= 5 and numActual <= 8:
                numLetras = numActual // 5
                restoLetras = numActual % 5
                result += (numLetras*valorCentena5) + (restoLetras*valorCentena1)
            elif numActual <= 3:
                numLetras = numActual // 1
                result += numLetras*valorCentena1
            elif numActual == 4:
                result += valorCentena1 + valorCentena5
            else:
                result += valorCentena1 + valorMillar

            numActual = int(valor[i+2])
            valorDecena5 = numerosArabigos["50"]
            valorDecena1 = numerosArabigos["10"]

            if numActual >= 5 and numActual <= 8:
                numLetras = numActual // 5
                restoLetras = numActual % 5
                result += (numLetras*valorDecena5) + (restoLetras*valorDecena1)
            elif numActual <= 3:
                numLetras = numActual // 1
                result += numLetras*valorDecena1
            elif numActual == 4:
                result += valorDecena1 + valorDecena5
            else:
                result += valorDecena1 + valorCentena1

            numActual = int(valor[i+3])
            valorUnidad5 = numerosArabigos["5"]
            valorUnidad1 = numerosArabigos["1"]


            if numActual >= 5 and numActual <= 8:
                numLetras = numActual // 5
                restoLetras = numActual % 5
                result += (numLetras*valorUnidad5) + (restoLetras*valorUnidad1)
            elif numActual <= 3:
                numLetras = numActual // 1
                result += numLetras*valorUnidad1
            elif numActual == 4:
                result += valorUnidad1 + valorUnidad5
            else:
                result += valorUnidad1 + valorDecena1
        
        elif len(valor) == 3:
            numActual = int(valor[i])
            valorCentena5 = numerosArabigos["500"]
            valorCentena1 = numerosArabigos["100"]
            
            if numActual >= 5 and numActual <= 8:
                numLetras = numActual // 5
                restoLetras = numActual % 5
                result += (numLetras*valorCentena5) + (restoLetras*valorCentena1)
            elif numActual <= 3:
                numLetras = numActual // 1
                result += numLetras*valorCentena1
            elif numActual == 4:
                result += valorCentena1 + valorCentena5
            else:
                result += valorCentena1 + valorMillar

            numActual = int(valor[i+1])
            valorDecena5 = numerosArabigos["50"]
            valorDecena1 = numerosArabigos["10"]

            if numActual >= 5 and numActual <= 8:
                numLetras = numActual // 5
                restoLetras = numActual % 5
                result += (numLetras*valorDecena5) + (restoLetras*valorDecena1)
            elif numActual <= 3:
                numLetras = numActual // 1
                result += numLetras*valorDecena1
            elif numActual == 4:
                result += valorDecena1 + valorDecena5
            else:
                result += valorDecena1 + valorCentena1

            numActual = int(valor[i+2])
            valorUnidad5 = numerosArabigos["5"]
            valorUnidad1 = numerosArabigos["1"]


            if numActual >= 5 and numActual <= 8:
                numLetras = numActual // 5
                restoLetras = numActual % 5
                result += (numLetras*valorUnidad5) + (restoLetras*valorUnidad1)
            elif numActual <= 3:
                numLetras = numActual // 1
                result += numLetras*valorUnidad1
            elif numActual == 4:
                result += valorUnidad1 + valorUnidad5
            else:
                result += valorUnidad1 + valorDecena1

        elif len(valor) == 2:

            numActual = int(valor[i])
            valorDecena5 = numerosArabigos["50"]
            valorDecena1 = numerosArabigos["10"]

            if numActual >= 5 and numActual <= 8:
                numLetras = numActual // 5
                restoLetras = numActual % 5
                result += (numLetras*valorDecena5) + (restoLetras*valorDecena1)
            elif numActual <= 3:
                numLetras = numActual // 1
                result += numLetras*valorDecena1
            elif numActual == 4:
                result += valorDecena1 + valorDecena5
            else:
                result += valorDecena1 + valorCentena1

            numActual = int(valor[i+1])
            valorUnidad5 = numerosArabigos["5"]
            valorUnidad1 = numerosArabigos["1"]


            if numActual >= 5 and numActual <= 8:
                numLetras = numActual // 5
                restoLetras = numActual % 5
                result += (numLetras*valorUnidad5) + (restoLetras*valorUnidad1)
            elif numActual <= 3:
                numLetras = numActual // 1
                result += numLetras*valorUnidad1
            elif numActual == 4:
                result += valorUnidad1 + valorUnidad5
            else:
                result += valorUnidad1 + valorDecena1

        else:
            numActual = int(valor[i])
            valorUnidad5 = numerosArabigos["5"]
            valorUnidad1 = numerosArabigos["1"]


            if numActual >= 5 and numActual <= 8:
                numLetras = numActual // 5
                restoLetras = numActual % 5
                result += (numLetras*valorUnidad5) + (restoLetras*valorUnidad1)
            elif numActual <= 3:
                numLetras = numActual // 1
                result += numLetras*valorUnidad1
            elif numActual == 4:
                result += valorUnidad1 + valorUnidad5
            else:
                result += valorUnidad1 + valorDecena1

        return result
                
def controlRepet(palabra):
    letraAnterior = ""
    acumRepet = 1
    for i in range (len(palabra)):
        if letraAnterior == palabra[i]:
            acumRepet += 1
            if acumRepet == 4:
                return 0
        else:
            acumRepet = 1
            letraAnterior = palabra[i]