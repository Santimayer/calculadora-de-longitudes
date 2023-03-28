from vars import *
entradaum=str(input("¿Que unidad de medida quieres convertir? \n"))
entradanum=int(input("Escribe el valor: "))
def centimetros():
    resinch=entradanum/inch
    resft=entradanum/ft
    resyd=entradanum/yd
    resmi=entradanum/mi
    reskm=entradanum/km
    reshm=entradanum/hm
    resdam=entradanum/dam
    resm=entradanum/m
    resdm=entradanum/dm
    resmm=entradanum/mm
    print("cm a in= "+str(resinch)) 
    print("cm a ft= "+str(resft))
    print("cm a yd= "+str(resyd))
    print("cm a mi= "+str(resmi))
    print("cm a km= "+str(reskm))
    print("cm a hm= "+str(reshm))
    print("cm a dam= "+str(resdam))
    print("cm a m= "+str(resm))
    print("cm a dm= "+str(resdm))
    print("cm a mm= "+str(resmm))
def pulgadas():
    resfinalencm=entradanum*2.54
    rescm=resfinalencm
    resft=resfinalencm/ft
    resyd=resfinalencm/yd
    resmi=resfinalencm/mi
    reskm=resfinalencm/km
    reshm=resfinalencm/hm
    resdam=resfinalencm/dam
    resm=resfinalencm/m
    resdm=resfinalencm/dm
    resmm=resfinalencm/mm
    print("in a cm= "+str(rescm)) 
    print("in a ft= "+str(resft))
    print("in a yd= "+str(resyd))
    print("in a mi= "+str(resmi))
    print("in a km= "+str(reskm))
    print("in a hm= "+str(reshm))
    print("in a dam= "+str(resdam))
    print("in a m= "+str(resm))
    print("in a dm= "+str(resdm))
    print("in a mm= "+str(resmm))
def pies():
    resfinalencm=entradanum*30.48
    rescm=resfinalencm
    resin=resfinalencm/inch
    resft=resfinalencm/ft
    resyd=resfinalencm/yd
    resmi=resfinalencm/mi
    reskm=resfinalencm/km
    reshm=resfinalencm/hm
    resdam=resfinalencm/dam
    resm=resfinalencm/m
    resdm=resfinalencm/dm
    resmm=resfinalencm/mm
    print("ft a cm= "+str(rescm)) 
    print("ft a in= "+str(resin))
    print("ft a yd= "+str(resyd))
    print("ft a mi= "+str(resmi))
    print("ft a km= "+str(reskm))
    print("ft a hm= "+str(reshm))
    print("ft a dam= "+str(resdam))
    print("ft a m= "+str(resm))
    print("ft a dm= "+str(resdm))
    print("ft a mm= "+str(resmm))
def yardas():
    resfinalencm=entradanum*91.4
    rescm=resfinalencm
    resin=resfinalencm/inch
    resft=resfinalencm/ft
    resyd=resfinalencm/yd
    resmi=resfinalencm/mi
    reskm=resfinalencm/km
    reshm=resfinalencm/hm
    resdam=resfinalencm/dam
    resm=resfinalencm/m
    resdm=resfinalencm/dm
    resmm=resfinalencm/mm
    print("yd a cm= "+str(rescm)) 
    print("yd a in= "+str(resin))
    print("yd a ft= "+str(resft))
    print("yd a mi= "+str(resmi))
    print("yd a km= "+str(reskm))
    print("yd a hm= "+str(reshm))
    print("yd a dam= "+str(resdam))
    print("yd a m= "+str(resm))
    print("yd a dm= "+str(resdm))
    print("yd a mm= "+str(resmm))
def millas():
    resfinalencm=entradanum*160934.4
    rescm=resfinalencm
    resin=resfinalencm/inch
    resft=resfinalencm/ft
    resyd=resfinalencm/yd
    resmi=resfinalencm/mi
    reskm=resfinalencm/km
    reshm=resfinalencm/hm
    resdam=resfinalencm/dam
    resm=resfinalencm/m
    resdm=resfinalencm/dm
    resmm=resfinalencm/mm
    print("mi a cm= "+str(rescm)) 
    print("mi a in= "+str(resin))
    print("mi a ft= "+str(resft))
    print("mi a yd= "+str(resyd))
    print("mi a km= "+str(reskm))
    print("mi a hm= "+str(reshm))
    print("mi a dam= "+str(resdam))
    print("mi a m= "+str(resm))
    print("mi a dm= "+str(resdm))
    print("mi a mm= "+str(resmm))
def kilometro():
    resfinalencm=entradanum*100000
    rescm=resfinalencm
    resin=resfinalencm/inch
    resft=resfinalencm/ft
    resyd=resfinalencm/yd
    resmi=resfinalencm/mi
    reskm=resfinalencm/km
    reshm=resfinalencm/hm
    resdam=resfinalencm/dam
    resm=resfinalencm/m
    resdm=resfinalencm/dm
    resmm=resfinalencm/mm
    print("km a cm= "+str(rescm)) 
    print("km a in= "+str(resin))
    print("km a ft= "+str(resft))
    print("km a yd= "+str(resyd))
    print("km a mi= "+str(resmi))
    print("km a hm= "+str(reshm))
    print("km a dam= "+str(resdam))
    print("km a m= "+str(resm))
    print("km a dm= "+str(resdm))
    print("km a mm= "+str(resmm))
def hectometro():
    resfinalencm=entradanum*10000
    rescm=resfinalencm
    resin=resfinalencm/inch
    resft=resfinalencm/ft
    resyd=resfinalencm/yd
    resmi=resfinalencm/mi
    reskm=resfinalencm/km
    reshm=resfinalencm/hm
    resdam=resfinalencm/dam
    resm=resfinalencm/m
    resdm=resfinalencm/dm
    resmm=resfinalencm/mm
    print("hm a cm= "+str(rescm)) 
    print("hm a in= "+str(resin))
    print("hm a ft= "+str(resft))
    print("hm a yd= "+str(resyd))
    print("hm a mi= "+str(resmi))
    print("hm a km= "+str(reskm))
    print("hm a dam= "+str(resdam))
    print("hm a m= "+str(resm))
    print("hm a dm= "+str(resdm))
    print("hm a mm= "+str(resmm))
def decametro():
    resfinalencm=entradanum*1000
    rescm=resfinalencm
    resin=resfinalencm/inch
    resft=resfinalencm/ft
    resyd=resfinalencm/yd
    resmi=resfinalencm/mi
    reskm=resfinalencm/km
    reshm=resfinalencm/hm
    resdam=resfinalencm/dam
    resm=resfinalencm/m
    resdm=resfinalencm/dm
    resmm=resfinalencm/mm
    print("dam a cm= "+str(rescm)) 
    print("dam a in= "+str(resin))
    print("dam a ft= "+str(resft))
    print("dam a yd= "+str(resyd))
    print("dam a mi= "+str(resmi))
    print("dam a km= "+str(reskm))
    print("dam a hm= "+str(reshm))
    print("dam a m= "+str(resm))
    print("dam a dm= "+str(resdm))
    print("dam a mm= "+str(resmm))
def metro():
    resfinalencm=entradanum*100
    rescm=resfinalencm
    resin=resfinalencm/inch
    resft=resfinalencm/ft
    resyd=resfinalencm/yd
    resmi=resfinalencm/mi
    reskm=resfinalencm/km
    reshm=resfinalencm/hm
    resdam=resfinalencm/dam
    resm=resfinalencm/m
    resdm=resfinalencm/dm
    resmm=resfinalencm/mm
    print("m a cm= "+str(rescm)) 
    print("m a in= "+str(resin))
    print("m a ft= "+str(resft))
    print("m a yd= "+str(resyd))
    print("m a mi= "+str(resmi))
    print("m a km= "+str(reskm))
    print("m a hm= "+str(reshm))
    print("m a dam= "+str(resdam))
    print("m a dm= "+str(resdm))
    print("m a mm= "+str(resmm))
def decimetro():
    resfinalencm=entradanum*10
    rescm=resfinalencm
    resin=resfinalencm/inch
    resft=resfinalencm/ft
    resyd=resfinalencm/yd
    resmi=resfinalencm/mi
    reskm=resfinalencm/km
    reshm=resfinalencm/hm
    resdam=resfinalencm/dam
    resm=resfinalencm/m
    resdm=resfinalencm/dm
    resmm=resfinalencm/mm
    print("dm a cm= "+str(rescm)) 
    print("dm a in= "+str(resin))
    print("dm a ft= "+str(resft))
    print("dm a yd= "+str(resyd))
    print("dm a mi= "+str(resmi))
    print("dm a km= "+str(reskm))
    print("dm a hm= "+str(reshm))
    print("dm a dam= "+str(resdam))
    print("dm a m= "+str(resm))
    print("dm a mm= "+str(resmm))
def milimetro():
    resfinalencm=entradanum*0.1
    rescm=resfinalencm
    resin=resfinalencm/inch
    resft=resfinalencm/ft
    resyd=resfinalencm/yd
    resmi=resfinalencm/mi
    reskm=resfinalencm/km
    reshm=resfinalencm/hm
    resdam=resfinalencm/dam
    resm=resfinalencm/m
    resdm=resfinalencm/dm
    resmm=resfinalencm/mm
    print("mm a cm= "+str(rescm)) 
    print("mm a in= "+str(resin))
    print("mm a ft= "+str(resft))
    print("mm a yd= "+str(resyd))
    print("mm a mi= "+str(resmi))
    print("mm a km= "+str(reskm))
    print("mm a hm= "+str(reshm))
    print("mm a dam= "+str(resdam))
    print("mm a dm= "+str(resdm))
    print("mm a m= "+str(resm))
if entradaum == "cm":
    centimetros()
if entradaum == "in":
    pulgadas()
if entradaum == "ft":
    pies()
if entradaum == "yd":
    yardas() 
if entradaum == "mi":
    millas()
if entradaum == "km":
    kilometro()
if entradaum == "hm":
    hectometro()
if entradaum == "dam":
    decametro()
if entradaum == "m":
    metro()
if entradaum == "dm":
    decimetro
if entradaum == "mm":
    milimetro()