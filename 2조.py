#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import random

def drawAngel():
    print("""
                  -----------
                  |         |
                  |         |    
                  |         |
                  |         |
                  |         |
                  |----------
                  Angel
                  축하합니다.
                  """)
    return


def drawAngel():
    print("""
                  -----------
                  |         |
                  |         |    
                  |         |
                  |         |
                  |         |
                  |----------
                  Devil
                  저런 모든 걸 잃었네요.
                  """)
    return

def drawPrize():
     for i in range(10):
            print(" "*(5-i)+"*"*(2*i+1))
            print("축하합니다! ")
    
    return 

def getCardNum():
    card = int(input('어떤 카드를 고르시겠어요? 1 또는 2 :'))
    return getCardNum() if card != 1 || 2 else card
    
def compareCardNum(cardNum):
    RealCard = random.randint(1,2)
    print('당신이 고른 카드는')
    time.sleep(2)
        
    if cardNum==RealCard:
        drawAngel()
        drawPrize()
        return 
    else:
        drawDevil()
        return
    
    
def openning():
    Goback = 'yes'
    while Goback != 'No':
        print('-----------------인생 역전 게임-------------------')
        print('당신은 MBs의 유명한 섭이벌 게임인 "해냈어!"에 참가했습니다.')
        print('드디어 마지막 라운드 도전입니다.')
        print("""당신앞 에는 천사카드와 악마카드가 뒤집어져 있습니다. 
        천사카드를 고르면 상금 1,000,000,000을 타게 될 것이고 
        악마카드를 고르면 모두 잃고 빈손으로 돌아가게됩니다.""")
        
        
        compareCardNum(getCardNum)
        
        Goback = input("선택의 순간으로 되돌아가겠습니까? Y/N>")
        while Goback != 'N' and Goback != 'Y':
            print("Y 또는 N을 입력하셔요! ")
            Goback = input("선택의 순간으로 되돌아가겠습니까? Y/N>")

            
            
        
openning()  


# In[ ]:




