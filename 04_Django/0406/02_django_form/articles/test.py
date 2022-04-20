genres = ['SF', 'TV영화', '가족', '공포', '다큐멘터리', '드라마', '로맨스', '어브벤처', '미스터리', '스릴러', '애니메이션', '액션', '코미디', '판타지']
genre_choice = set()
for i in range(len(genres)):
    genre_choice.add((genres[i], genres[i]))

print(genre_choice)