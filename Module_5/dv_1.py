import numpy as np
import matplotlib.pyplot as plt
import mpld3

x = np.linspace(0,10,100)
y1,y2,y3 = np.cos(x),np.cos(x+1), np.cos(x+2)

names = [ 'Signal 1', 'Signal 2' , 'Signal 3']

fig,axes = plt.subplots(nrows =3)

for ax,y,name in zip(axes, [y1,y2,y3], names) :
    ax.plot(x,y,color='blue')
    ax.set(xticks=[], yticks=[], title=name)

plt.show()


html_str = mpld3.fig_to_html(fig)
Html_file= open("C:/Users/dell/OneDrive/Documents/Study_Fall_2022/Statistical_Computing/Module_5/test1.html","w")
Html_file.write(html_str)
Html_file.close()