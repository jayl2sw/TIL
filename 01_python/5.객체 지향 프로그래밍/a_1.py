name = '아이유'
age = 20

name_01 = '홍길동'

person_01 = {
    'name': '아이유',
    'age': 20
}

person_02 = {
    'name': '홍길동',
    'age': 999
}


def greeting(person):
    # person : dictionary
    print(f'안녕하세요 {person["name"]}')

greeting(person_01)
greeting(person_02)