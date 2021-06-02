import time 
import random
        
def Opening():
    print('-------인생 역전 게임--------')
    print('당신은 MBS의 유명한 서바이벌 게임인 "해냈어!" 참가하였습니다')
    print('드디어 마지막 라운드 도전!!!!')
    print('당신 앞에는 천사카드와 악마카드가 뒤집어져 있습니다.')
    print('천사카드를 고르면 상금 1,000,000,000을 타게 될 것이고')
    print('악마카드를 고르면 모든 것을 잃고 빈 손으로 돌아가게 됩니다.')
def drawAngel():
     print('''
        |-------------|
        |             |
        |   ANGEL     |
        |             |
        |             |
        |   CARD      |
        |             |
        |             |
        |-------------|
             Angel
        ''')
def drawDevil():
     print('''
        |-------------|
        |             |
        |   DEVIL     |
        |             |
        |             |
        |   CARD      |
        |             |
        |             |
        |-------------|
            Devil
        ''')
def drawPrize():
    print('''
                    < WIN >
                  /////////////          
               ///100,000,000 ///
           //////////////////////////    
        ''')
def getCardNum():
    CardNum=1
    CardNum=int(input('어떤 카드를 고르시겠습니까? (1) or (2)'))
    while CardNum!=1 and CardNum!=2:
        print('(1) or (2) 중에 하나를 골라주세요.')
        CardNum=int(input('어떤 카드를 고르시겠습니까? (1) or (2)' ))   

def compareCard(cardNum):
    RealCard = random.randint(1,2)
    print('당신이 고른 카드는...')
    time.sleep(2)
    if cardNum == RealCard:
        drawAngel()
        drawPrize()
    if cardNum!=RealCard:
        drawDevil()
    
Goback='Yes'
while Goback!='No':
    #게임설명
    Opening()
    #카드선택
    cardNum= getCardNum()
    #실제카드 선택 y및 결과
    compareCard(cardNum) 
    
#게임 재시작
    print()

    Goback=input('선택의 순간으로 되돌아 가겠습니까? Yes or No  : ' )
    while Goback !='No' and Goback!='Yes':
        print('Yes or No 중에 하나를 골라주세요.')
        Goback=input('선택의 순간으로 되돌아 가겠습니까? Yes or No  : ' )
        
