"""
Created on Thu Jul 15 21:20:26 2021

@author: Mustaqimov Muhammad

"""
import random
# O'YLAGAN SONNI TOPADIGAN DASTUR !!!
def son_top(n=10):
    print(f" 1 dan {n} gacha son o'yladim.\n Topa olasizmi?: ")
    sonlar=random.sample(range(1,n+1),1)
    son=int(sonlar[0])
    amal=True 
    k=0
    while amal:
        k+=1
        son2=int(input(">>>>"))
        if son>son2:
            print(f"Xato, men o'ylagan son {son2} dan katta \n Yana harakat qilib ko'ring")
            amal=True
        elif son<son2:
            print(f"Xato, men o'ylagan son {son2} dan kichik \n Yana harakat qilib ko'ring")
            amal=True
        else: amal=False
    print(f"O'ylagan sonim {son2} edi . Topdingiz Tabriklayman ")
           
    print(f"O'ylagan sonimni {k} ta taxminda topdiz ")
    return k

def komp_son_top(n=10):
    print(f"\n 1 dan {n} gacha son o'ylang.\n Topishga harakat qilaman")
    amal=True
    x,y=1,(n+1)
    input("Son o'ylagan bo'lsangiz istalgan tugmani bosing \n >>>")
    k1=0
    while amal:
        son=random.randrange(x,y,1)      
        print(f">>>{son} o'yladingiz \n o'ylagan sonizdan katta bo'lsa (+)\n kichik bo'lsa (-) \n topgan bo'lsam (t) ni bosing")
        k1+=1
        belgi=str(input(">>>>"))
        if belgi=="+":
           y=son
           amal=True
        elif belgi=="-":
           x=son
           amal=True
        elif belgi=="t": amal=False
    print(f"O'ylagan sonniz {son} topdim!!! {k1} ta urunishda") 
    return k1


def igra(n=10):
    javob=True
    while javob:
        k1=son_top(n)
        k2=komp_son_top(n)
        if k1>k2:
            print(f"Men {k1} taxmin bilan topdim va  yutdim!")
        elif k1<k2:
            print(f"Siz {k2} taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        javob = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0):"))         
            
print(igra())            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            