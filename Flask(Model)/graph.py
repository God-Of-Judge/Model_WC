#%%
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.animation import FuncAnimation
from matplotlib import rc







with open('runs/detect/exp34/labels/video_cross3.txt', 'r') as f:
    data = f.readlines()

print(data)
column_name = ['fram','class','x','y','w','h','p']
column_name

data_split = [x.strip().split() for x in data[:]]

print(data_split)


df = pd.DataFrame(data_split, columns = column_name)

df.head()

df_cross=df[df['class']=='6']
df_straight=df[df['class']=='7']

# def animate(i):
#     # data =pd.read_csv('sam_results.csv')
#     # x1=df_cross['class']	#dy_day(데이터 프레임)의 index(날짜, 시간)를 리스트로 저장 
#     # y1=df_cross['p']	
#     x2=df_straight['class']	#dy_day(데이터 프레임)의 index(날짜, 시간)를 리스트로 저장 
#     y2=df_straight['p']	
#     # x = f['x_value']
#     # y1 = data['total_1']
#     # y2 = data['total_2']
 
#     plt.cla()
#     # plt.barh(x1,y1, label='블로그')
#     plt.barh(x2,y2, label='유튜브')
    
#     plt.legend(loc = 'upper left')
#     plt.tight_layout()
 
# ani = FuncAnimation(plt.gcf(),animate, interval = 1000)
 
# plt.tight_layout()
# plt.show()

fig, ax = plt.subplots(figsize=(10,6))
ax.grid()

x, y = [], []
line, = plt.plot([], [], )

def init():    
    ax.set_xlim(0, 4*np.pi)
    ax.set_ylim(-1.2, 1.2)
    
    # X축 단위 표시를 pi 단위로 표시
    ax.set_xticks([0,np.pi,2* np.pi,3*np.pi,4*np.pi])
    ax.set_xticklabels(['0',r'$\pi$',r'$2\pi$',r'$3\pi$',r'$4\pi$']) 
          
    return line,

def update(i):    
    x.append(i)    
    y = np.sin(x) 
    
    line.set_data(x, y)
    
    return line,

ani = FuncAnimation(fig=fig, func=update, frames=np.linspace(0, 4*np.pi, 200),
                    init_func=init, interval=20, blit=True)

rc('animation', html='html5')
ani



