print('\n'.join([''.join([('Love'[(x-y) % len('Love')]
                          if ((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3 <= 0 else ' ')#此处是根据心形曲线公式来的(x2+y2-1)3-x2y3=0
                          for x in range(-30, 30)])#定义高
                for y in range(30, -30, -1)]))#定义宽