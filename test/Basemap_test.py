
# from mpl_toolkits.basemap import Basemap
# import matplotlib.pyplot as plt

# # 新建地图
# map = Basemap() #Basemap类有很多属性，这里全都使用默认参数

# # 画图
# map.drawcoastlines()

# # 显示结果
# plt.show()

# # 存储结果
# plt.savefig('test.png')


# from mpl_toolkits.basemap import Basemap
# import matplotlib.pyplot as plt

# # 更改投影方式
# map = Basemap(projection = 'ortho', lat_0 = 0, lon_0 = 0) #’ortho’指正射投影，具体参数后面再讨论；后面两个参数是设置中心点

# # 给整个地图上蓝色
# map.drawmapboundary(fill_color = 'aqua')

# # 给陆地涂上珊瑚色，湖泊涂上蓝色
# map.fillcontinents(color = 'coral', lake_color = 'aqua')

# # 画图
# map.drawcoastlines()

# # 显示结果
# plt.show()
# 
# 
# 


import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111)

map = Basemap(projection='cyl', lat_0=0, lon_0=0)

map.drawmapboundary(fill_color='#7777ff')
map.fillcontinents(color='#ddaa66', lake_color='#7777ff', zorder=0)
map.drawcoastlines()

lons = np.array([-13.7, -10.8, -13.2, -96.8, -7.99, 7.5, -17.3, -3.7])
lats = np.array([9.6, 6.3, 8.5, 32.7, 12.5, 8.9, 14.7, 40.39])
cases = np.array([1971, 7069, 6073, 4, 6, 20, 1, 1])
deaths = np.array([1192, 2964, 1250, 1, 5, 8, 0, 0])
places = np.array(['Guinea', 'Liberia', 'Sierra Leone','United States', 'Mali', 'Nigeria', 'Senegal', 'Spain'])

x, y = map(lons, lats)

map.scatter(x, y, s=cases, c='r', alpha=0.5)

axins = zoomed_inset_axes(ax, 7, loc=1)
axins.set_xlim(-20, 0)
axins.set_ylim(3, 18)

plt.xticks(visible=False)
plt.yticks(visible=False)

map2 = Basemap(llcrnrlon=-20,llcrnrlat=3,urcrnrlon=0,urcrnrlat=18, ax=axins)
map2.drawmapboundary(fill_color='#7777ff')
map2.fillcontinents(color='#ddaa66', lake_color='#7777ff', zorder=0)
map2.drawcoastlines()
map2.drawcountries()

map2.scatter(x, y, s=cases/5., c='r', alpha=0.5)

mark_inset(ax, axins, loc1=2, loc2=4, fc="none", ec="0.5")

plt.show()