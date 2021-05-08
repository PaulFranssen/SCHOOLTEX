import numpy as np
import matplotlib.pyplot as plt

x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

plt.axis((10,100, 200,400))



font1 = {'family':'serif','color':'blue','size':20}
font2 = {'family':'serif','color':'darkred','size':15}



plt.subplot(2, 2, 1)
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage", fontdict=font2)
plt.title("Sports Watch Data", fontdict=font1)
plt.grid(axis='x', color = 'green', linestyle = '--', linewidth = 0.5)
plt.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([1, 10, 100, 1000])


plt.subplot(2, 2, 2)
plt.plot(x,y, color ='yellow')

x = np.array([0, 1, 2, 3])
y = np.array([15, 9, 18, 25])
plt.plot(x,y, color = 'pink')

plt.subplot(2, 2, 3)
x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

plt.bar(x,y)

plt.subplot(2,2,4)
x = np.linspace(0, 10, 100)
y = x**0.5

plt.plot(x,y, color = 'blue')
plt.show()

plt.suptitle("MY SHOP")

plt.show()
