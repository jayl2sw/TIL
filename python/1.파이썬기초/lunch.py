# import 가지고 오는 행위
# 이 이후로 활용할 코드를 가지고 올 것이기 때문에 
# import는 항상 최 상단에 작성한다.
import random # 코드 쓰다가 필요할 때, 사용

menu = ['짜장면', '짬뽕', '탕수육']
choice = random.choice(menu)

print(choice)

