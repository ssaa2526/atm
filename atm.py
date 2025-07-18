# balance : 초기 잔액을 설정하는 변수를 초기화해주세요.
# 금액은 여러분 마음대로 설정해줴요.

# 사용자로부터 atm 기계에 사용 목적에 맞는 기능을 선택할 수 있도록
# 기능 입력을 받는 기능을 입력해주세요.

balance = 10000

receipts = []

while True:
     num = input("사용하실 기능의 번호를 선택해주세요 (1.입금, 2.출금, 3.영수증 보기, 4.종료) : ") 

     if num == '4':
          break

     if num == '1': # 입금 기능 -> feat/deposit
          deposit_amount = int(input('입금할 금액을 입력해주세요: '))
          balance  += deposit_amount 
          print(f'입금하신 금액{deposit_amount}원이고, 현재 잔액은{balance}원 입니다.')
          receipts.append(('입금', deposit_amount, balance))

     if num == '2':
          withdraw_amout = int(input("출금할 금액을 입력해주세요."))
          withdraw_amout = min(balance,withdraw_amout)
          balance -= withdraw_amout 
          print(f"출금하신 금액은 {withdraw_amout}원이고, 현재 잔액은 {balance}원 입니다.")
          receipts.append(('출금', withdraw_amout, balance))

     if num == '3':
          if receipts:
             for i in receipts:
                print(f"{i[0]}: {i[1]}원 | 잔액: {i[2]}원")
          else:
               print("영수증 내역이 없습니다.") 

print(f'서비스를 종료합니다. 현재 잔액은 {balance}원 남았습니다.')
