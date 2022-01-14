# 1~45 중에 6개만 뽑아서 리스트에 담아서 출력
import random
# request 불러오기 
import requests 

# requests 사용해서 api에 데이터 요청
url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=997'
# https : hyper text transfer protocol
# www.dhlottery.co.kr : 고유 주소값
# common.do : 특정 페이지
# ?뒤에 작성되는 내용은 이 주소로 요청을 보낼 건데~ ?뒤의 값과 같이 요청을 보낼거다.
# method=getLottoNumber : 조건 1
# drwNo=997 : 조건 2

# get()어떤 url을 집어 넣어주면 조희 요청을 보냄 (post 도 있음)
# request가 가지고 있는 get함수에 url을 넣어서 조회 요청을 하고 이를 json()을 통해 json 문법을 python문법으로 바꾸어주는 함수
response = requests.get(url).json() 

print(response)

# 404 = Page Not Found (페이지를 찾을 수 없을 때)
# 403 = Forbidden (권한 때문에 거절 되었을 때)
# 500 = Server Error (서버 때문에 실패했을 때)
# 200 = 성공적

# 요청 보내서 응답 받은 문서를 출력
winners = []
for i in range(1,7):
    # print(response[f'drwtNo{i}'])
    winners.append(response[f'drwtNo{i}'])

n = 0
count = 0
numbers = list(range(1, 46))

while count < 6:
    count = 0
    lotto = random.sample(numbers, 6)
    lotto.sort()
    for i in range(len(lotto)):
        if lotto[i] == winners[i]:
            count += 1
        n += 1


# for i in range(1000000):
#     lotto = random.sample(numbers, 6)
#     # 당첨 횟수를 기록
#     count = 0
#     for num in lotto:
#         # lotto가 가지고 있는 값들 하나하나가 winners안에 들어있다면....
#         # 한개 당첨
#         # 당첨 횟수 기록
#         # 6개 당첨 == 1등
#         if num in winners:
#             count += 1
#     if count == 6:
#         print('1등 당첨')


print(f'Conglaturation! You tried {n} times')
