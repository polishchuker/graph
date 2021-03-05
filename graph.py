from matplotlib import pyplot as plt

# graph for the daily active users (DAU) of Facebook
year = [2011,2012,2013,2014,2015,2016,2017,2018,2019,2020]


dau = [483,618,757,890,1040,1230,1400,1523,1660,1840]
mau= [845,1060,1228,1393,1590,1860,2130,2320,1500,2800]

yticks = [400,600,800,1000,1200,1400,1600,1800,2000]

ax = plt.subplot()
plt.plot(year,dau,color = "black",marker= "o")
plt.title('DAU in millions')
ax.set_xticks(year)
ax.set_yticks(yticks)
plt.xlabel('number of users')
plt.ylabel('DAU')
plt.grid(which='major',axis = 'both')

plt.savefig('Dau.jpg')

plt.show()
