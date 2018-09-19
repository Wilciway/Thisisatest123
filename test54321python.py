def standaardtarief(afstandKM):
    #Als de afstand negatief is.
    if afstandKM < 0:
        prijs = 0
        return prijs
    #Als de afstand tussen de 0 en 50 kilometer is.
    elif afstandKM > 0 and afstandKM < 50:
        prijs=round((afstandKM * 0.80), 2)
        return prijs
    #Als de afstand boven de 50 kilometer is.
    elif afstandKM >= 50:
        prijs=round(((afstandKM*0.60)+15),2)
        return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    if (leeftijd >= 65 or leeftijd <= 12):  #Als de leeftijd tussen de 12 en 65 jaar is.
        if weekendrit == True:              #Als het een weekend rit is.
            rprijs = round((afstandKM * 0.65), 2)
            return rprijs
        else:         #Als het geen weekendrit is.
            rprijs = round((afstandKM * 0.70), 2)
            return rprijs
    else: #Als de leeftijd niet tussen de 12 en 65 jaar is.
        if weekendrit == True:              #Als het een weekend rit is.
            rprijs = round((afstandKM * 0.6), 2)
            return rprijs
        else:           #Als het geen weekendrit is.
            return rprijs





#km=float(input("Hoeveel kilometer is de rit?:"))
#wk=bool(input("Is het weekend (kies uit True of False):?"))
#lftd=int(input("hoe oud ben je?:"))
#print(ritprijs(lftd,wk,standaardtarief(km)))


