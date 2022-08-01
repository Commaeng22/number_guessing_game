import random
import time

print('\n','*'*100, '\n')
print('1~ 희망하시는 범위의 숫자 맞추기 게임 입니다.')
print('\n','*'*100, '\n')
username = input('\n 도전자의 이름을 입력하세요 : ')
limitchance = int(input('\n  1  ~ 희망하는 숫자의 범위를 입력하세요 : '))

starttime=time.time()
secret_number = random.randint(1,limitchance)
#print(secret_number)
for i in range(1,10000):
    input_number = int(input('예상 정답을 입력하세요 : '))
    if secret_number == input_number:
     print('\n 정답입니다!!!!!!! \n')
     endtime=time.time()
     print('축하드립니다.',username,'님은 1~',limitchance,'까지의 수 중',secret_number, '맞추기를', i,'회,',endtime - starttime, '초 만에 맞추셨습니다.\n')
     #print(username,'님은 정답을 맞추는데',endtime - starttime, '초 걸렸습니다.\n')
     exit()
    elif secret_number > input_number:
     print('\n',input_number,'보다 높여 주세요.(Up)\n')
    elif secret_number < input_number:
     print('\n',input_number,'보다 낮춰 주세요.(Down)\n')
    i = i+1
