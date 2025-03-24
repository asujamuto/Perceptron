import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation

class GUI():

    def __init__(self):
        self.x_vec = []
        self.y_vec = []
        self.w_vec = []
        self.current_epoch = 0
        self.current_id = 0
        
    def append(self, weights, epoch, id):
        self.w_vec.append(weights)
        self.current_epoch = epoch
        self.current_id = id


    def animate(self):
        fig, ax = plt.subplots(1,1)
        quiv = ax.quiver()

        self.show(self.x_vec[0], self.w_vec[0], self.w_vec[0])
        for i in range(len(self.x_vec)):
            self.show(self.x_vec[i-1], self.w_vec[i], self.w_vec[i-1])



    def show(self, x_vec, w_vec, old_w_vec):
        V=np.array([x_vec[:2], 
                    w_vec[:2],
                    old_w_vec[:2]])
        origin = np.array([[0,0,0], [0,0,0]])
        plt.quiver(*origin, V[:, 0], V[:, 1], color=['g', 'b', 'grey'], scale=1)
        plt.xlabel("Wymiar 0")
        plt.ylabel("Wymiar 1")
        plt.title("Rzutowanie 4D → 2D")

        for i in range(len(self.x_vec)):
            print(self.y_vec)
            shape = ""
            if self.y_vec[i] == 1:
                shape="g+"
            else:
                shape="rx"

            plt.plot(np.array(self.x_vec[i][0]), np.array(self.x_vec[i][1]), shape)
        plt.plot(0,0, 'ok')
        plt.axis('equal')
        plt.grid(which='major') 
        plt.show()
    


    def add_info(self, x_vec, y_vec):
        self.x_vec = x_vec 
        self.y_vec = y_vec
        

    def test(self):
        fig, ax = plt.subplots()
        t = np.linspace(0, 3, 40)
        g = -9.81
        v0 = 12
        z = g * t**2 / 2 + v0 * t

        v02 = 5
        z2 = g * t**2 / 2 + v02 * t

        scat = ax.scatter(t[0], z[0], c="b", s=5, label=f'v0 = {v0} m/s')
        line2 = ax.plot(t[0], z2[0], label=f'v0 = {v02} m/s')[0]
        ax.set(xlim=[0, 3], ylim=[-4, 10], xlabel='Time [s]', ylabel='Z [m]')
        ax.legend()

        def update(frame):
             # for each frame, update the data stored on each artist.
            x = t[:frame]
            y = z[:frame]
            # update the scatter plot:
            data = np.stack([x, y]).T
            scat.set_offsets(data)
            # update the line plot:
            line2.set_xdata(t[:frame])
            line2.set_ydata(z2[:frame])
            return (scat, line2)

        ani = animation.FuncAnimation(fig=fig, func=update, frames=40, interval=30)
        plt.show()

