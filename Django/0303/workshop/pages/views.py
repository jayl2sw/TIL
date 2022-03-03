from django.shortcuts import render
from random import sample
import json
import requests

# Create your views here.
def main(request):
    return render(request, 'main.html')
    
def lotto(request):
    pick = sample(range(1, 45), 6)
    pick.sort()
    context = {
        'pick': pick
    }
    return render(request, 'lotto.html', context)

def lotto_p(request, round=None, times=None):
    round = request.GET.get('round')
    times = int(request.GET.get('times'))


    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={round}'
    r = requests.get(url)
    data = json.loads(r.text)

    wins = []
    for i in range(1, 7):
        wins.append(data['drwtNo' + str(i)])
    bns = data['bnusNo']

    wins = set(wins)
    result = [0] * 6
    for j in range(times):
        pick = sample(range(1, 45), 6)
        if len(set(pick) & wins) == 6:
            result[0] += 1
        elif len(set(pick) & wins) == 5 and bns in pick:
            result[1] += 1
        elif len(set(pick) & wins) >= 3:
            result[7 - len(set(pick) & wins)]+= 1
        else:
            result[5] += 1

    context = {
        'result' : result,
        'wins': wins,
        'bonus': bns
    }
    
    return render(request, 'lottop.html', context)
