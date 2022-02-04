# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
wifi = (random.randint(1,2))
if wifi == 1:
    print("lan:stop")
elif wifi == 2:
    brandenLampen = (random.randint(1,2))
    if brandenLampen == 1:
        print("nee:koop nieuwe router")
        print("https://www.bol.com/nl/nl/p/tp-link-archer-ax50-router-wifi-6-3000-mbps/9200000120245339/?bltgh=uON9GM4Acqm-XOb5QipILA.4_54.58.ProductImage")
        print("stop")
    elif brandenLampen == 2:
        print("als je de stekker in en uit doet, branden dan de zelfde lampen")
        JaNeeLamp = (random.randint(1,2))
        if JaNeeLamp == 1:
            print("nee:koop nieuwe router1")
            print("https://www.bol.com/nl/nl/p/tp-link-archer-ax50-router-wifi-6-3000-mbps/9200000120245339/?bltgh=uON9GM4Acqm-XOb5QipILA.4_54.58.ProductImage")
            print("stop")
        elif JaNeeLamp == 2:
            print("contactpagina")
            belOfChat = (random.randint(1,2))
            if belOfChat == 1:
                print("bellen")
                print("stop")
            elif belOfChat == 2:
                print("chatten")
                print("stop")

orgineel = str(input("typ de orginele prijs: "))
print("orginele prijs is: "+ orgineel)
tip = str(input("typ hoeveel procent je wilt geven: "))
print("je wilt " + tip+" geven")
orgineel = int(orgineel)
tip = int(tip)
uitkomst = ((orgineel/100*tip)+orgineel)
uitkomst = str(uitkomst)
orgineel = str(orgineel)
print("je moet betalen: " +  uitkomst)