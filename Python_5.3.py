leeftijd=input("Hoe oud ben je?: ")
paspoort=input("Bezit je een Nederlands paspoort?: ")
if int(leeftijd)>=18 and paspoort == "ja":
   print("Gefeliciteerd, je mag stemmen!")
else:
    print("Je mag niet stemmen")