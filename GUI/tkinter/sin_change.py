
from pylab import show, arange, sin, plot, pi

t = arange(0.7, 2.0, 0.001)
s = sin(2*pi*t)
plot(t, s)
show()