from math import gcd
import random



def RSA(p,q,metin):
    n=p*q
    phi=(q-1)*(p-1)
    phiList=findE(phi)
    e=random.choice(phiList)
    Dlist=findD(e,phi)
    d=random.choice(Dlist)
    print(e,d,(e*d)%phi)
    
    cipher=encryption(e,n,metin)
    decipher=decrytion(d,n,cipher)

    print("şifrelenen metin : {0} , çözülen metin :{1}".format(cipher,decipher))



def findE(phi):
    phiList=[]
    for item in range(2,phi):
        if (gcd(item,phi)==1):
            phiList.append(item)

    return phiList

def findD(e,phi):
    dList=[]
    for item in range(phi):
        if ((item*e)%phi)==1:
            dList.append(item)
    return dList
                    
       
def encryption(e,n,metin):
    a=pow(metin,e)
    cipher = a%n
    return cipher

def decrytion(d,n,cipher):
    x=pow(cipher,d)
    cozum=(x%n)   
    return cozum   

def main():
    metin="1235"
    print("number:")
    ascii_values = []
    for character in metin:
        ascii_values.append(ord(character))
    print(ascii_values)

    for item in ascii_values:
        RSA(61,53,item)
        
    return

main()

