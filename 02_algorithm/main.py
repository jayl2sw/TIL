import math
import matplotlib.pyplot as plt



map = [[500] * 100 for _ in range(300)]

target1_x = (3**0.5)*100 + 50
target1_y = 150

x = 0
y = 0

r = 5.74

ball1_x = (3**0.5)*100
ball1_y = 100

y_difference = ball1_y - y
x_difference = ball1_x - x

distance = (y_difference ** 2 + x_difference ** 2) ** 0.5

# 두 공의 좌표 차이 설정
y_target_d = target1_y - ball1_y
x_target_d = target1_x - ball1_x

# 맞을 r_각 
r_difference = []

for i in range(0, 21):
    r_difference.append(-4/3*r + i/20*8/3*r)

angle_difference = []
rds = []
for rd in r_difference:
    angle_difference.append(math.degrees(math.atan(rd/distance)))
    rds.append(rd/distance)


plt.plot(math.atan(rd/distance),)
print(r_difference)
for i in range(len(r_difference)-1):
    print(r_difference[i+1]-r_difference[i],end='')
print(angle_difference)
ans = []
for an in angle_difference:
    ans.append(distance * math.tan(math.radians(an)))

print(ans)
plt.plot(r_difference, angle_difference)
plt.show()

theta = math.degrees(math.atan(y_difference/x_difference))
theta_p = math.degrees(math.atan(y_target_d/x_target_d)) - theta

print(theta)
print(theta_p)


