def add(x,y):
    return x + y

add(1,2) 		# 위치 - 내부에서 바인딩 x = 1; y = 2
add(y=2, x=1) 	# 키워드 - 직접 x와 y의 값을 각각지정
add(x=1, 2)		# SyntaxError: positional argument 'follows' keyword argument
				# 키워드 인자를 사용하는 순간 위치로 바인딩 불가능
add(1, y=2)		# 위치 지정 먼저 하고 키워드 사용하면 가능하다.