#1. 인사
print('어서오세요! 파스타 맛집 오일리입니다!')
seat=input('테이블과 바 테이블 자리 중, 어느 자리를 선호하십니까?')
print('네.' +seat +'자리로 안내하겠습니다')
print()

#2. 메뉴 설명

print('저희 가게의 메인 메뉴는 파스타와 리조또로 나뉩니다.')
print('모든 메인 메뉴의 가격은 10,900원, 모든 서브 메뉴의 가격은 5,800원으로 동일합니다.')
print()
foods=['까르보나라 파스타', '봉골레 파스타', '새우 로제 파스타', '버섯 크림 리조또', ' 크림 에그 리조또' ]
foods={ '까르보나라 파스타' : '베이컨 시저 샐러드', '봉골레 파스타' : '바게트 빵', '새우 로제 파스타' : '카프레제', 
'버섯 크림 리조또' : '베이컨 시저 샐러드', ' 크림 에그 리조또' : ' 카프레제' }
order=[ ]
myfood=[ ]
myfood=input(str(list(foods.keys())) + '중 어떤 음식을 선택하시겠습니까?')
order.append( myfood )

side=['베이컨 시저 샐러드','바게트 빵','카프레제']
print('사이드 메뉴는' + str(side) + ' 가 있습니다.')

print('<%s> 과 어울리는 사이드 메뉴는 <%s>입니다.' %(myfood, foods[myfood]))
print()
print('사이드 메뉴로 추가하시겠습니까?')
check=int(input('추가하신다면 0, 추가하지 않는다면 1을 입력해주세요.'))
myside=[ ]

if check== 0 :
    order.append(foods[myfood])
    myside.append(foods[myfood])
    print('추가되었습니다. 다음 음료 주문으로 넘어가겠습니다.')
else :
    print('네. 다음 음료 주문으로 넘어가겠습니다.')

print()
drink=['레몬에이드', '청포도에이드', '콜라', '사이다', '클라우드 생맥주', '레드 진와인', '화이트 진와인']
print('음료는' + str(drink) +'이 있습니다')
print('음료의 가격은 모두 6,000원으로 동일합니다.')
mydrink=input(str('이 중 어떤 음료를 선택하시겠습니까?'))
print()
order.append( mydrink )

print('주문을 확인해드리겠습니다.')

while True:
    print('주문하신 메뉴는 <%s> 맞습니까?' %(order))
    plus=[ ]
    check=[ ]
    check=int(input('맞으시다면 0, 다른 메뉴를 추가하신다면 1, 메뉴를 취소하신다면 2를 입력해주세요.'))
    print()
    if check == 1:
        plus= input(str('어떤 메뉴를 추가하시겠습니까?'))
        order.append( plus )
        print('메뉴 다시 확인해드리겠습니다.')
    elif check == 2:
        hate = input(str('어떤 메뉴를 취소하시겠습니까?'))
        order.remove(hate)
        print('메뉴 다시 확인해드리겠습니다.')
    else:
        order.sort()
        print('주문이 완료되었습니다.')
        print('조리 시간은 약 10분 소요될 예정입니다. 감사합니다.')
        break



#3. 결제(회원 조회, 적립, 총액 안내, 결제)

print()
print('결제를 진행해드리겠습니다.')
print('파스타 오일리의 회원이신가요?')
member=( )
member=int(input('맞으면 0, 새로 가입을 원하신다면 1, 바로 결제를 진행하고 싶으시다면 2를 눌러주세요.'))

password=' '
if member==0 :
    print('회원 적립을 도와드리겠습니다.')
    while True:
        password!=210
        password=int(input('비밀번호 3자리를 입력해주세요.'))
        if password==210:
            break
    print('로그인에 성공했습니다. 1200포인트 적립되었습니다.')
elif member==1:
    print('회원 가입을 도와 드리겠습니다.')
    myName=input('성함을 입력해주세요.')
    password2=input('비밀번호를 입력해주세요.')
    print(myName+'님.  비밀번호 ' + password2 +'(으)로 가입 완료되셨습니다.')
    print('1200 포인트 적립되었습니다.')
else:
    print('네. 바로 결제 진행해드리겠습니다.')

print('카드를 아래 쪽에 꽂아주세요')

print()
print('결제가 완료되었습니다. 이용해 주셔서 감사합니다.')

          


