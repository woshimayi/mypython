from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

fig = Figure(figsize=(12, 8), facecolor='white')
axis = fig.add_subplot(111)
x = [1,2,3,4]
y = [5,6,7,8]

axis.plot(x, y)

axis.set_xlabel('H')
axis.set_ylabel('V')

axis.grid(linestyle='-')
def _destroyWindow():
    root.quit()
    root.destory()

root = tk.Tk()
root.withdraw()
root.protocal('WM_DELETE', _destroyWindow)

canvas = FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.update()
root.deiconify()

root.mainloop()
