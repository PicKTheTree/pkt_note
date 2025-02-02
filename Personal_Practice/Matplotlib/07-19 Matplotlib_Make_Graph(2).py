# 일자 : 23.07.19
# 내용 : Python 모듈 'matplotlib'를 연습하기 위한 코드이다. 
import matplotlib.pyplot as plt


plt.plot([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7], [0.7, 0.6, 0.5, 0.9, 0.8, 0.8, 0.8, 0.4], 'bs-', label = 'DAB' )
plt.plot([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7], [0.65, 0.55, 0.3, 0.4, 0.9, 0.38, 0.5, 0.0], 'ro-', label = 'RAB' )
plt.plot([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7], [0.35, 0.4, 0.42, 0.3, 0.42, 0.5, 0.4, 0.2], 'g2-', label = 'RAB' )
plt.legend( loc = 'lower left')



plt.show()