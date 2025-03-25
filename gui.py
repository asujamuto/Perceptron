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



    def show(self):
        fig, ax = plt.subplots()
        x_vec_len = sum([ i**2 for i in self.x_vec[0][:2]])**(1/2)
        w_vec_len = sum([ i**2 for i in self.w_vec[0][:2]])**(1/2)
        n = [(i*j)/(w_vec_len) for i, j in zip(self.x_vec[0][:2], self.w_vec[0][:2])] 

        V=np.array([self.x_vec[0][:2], 
                    self.w_vec[0][:2],
                    self.w_vec[0][:2],
                    n,
                    [-1*n[0], -1*n[1]]])
        origin = np.array([[0,0,0,0,0], [0,0,0,0,0]])
        ax.set_xlabel("Wymiar 0")
        ax.set_ylabel("Wymiar 1")
        ax.set_title("Wykres Trenowania")

        ax.plot(0,0, 'g', label='X wektor')
        ax.plot(0,0, 'b', label='Wagi')
        ax.plot(0,0, 'grey', label='Poprzednie wagi')
        ax.plot(0,0, 'red', label='Hiperpłaszczyzna decyzyjna')


        plt.legend(loc='upper left')
        
        for i in range(len(self.x_vec)):
            shape = ""
            if self.y_vec[i] == 1:
                shape="g+"
            else:
                shape="rx"
            ax.plot(np.array(self.x_vec[i][0]), np.array(self.x_vec[i][1]), shape)

        ax.plot(0,0, 'ok')
        ax.axis('equal')
        ax.grid(which='major')
        Q = ax.quiver(*origin, V[:, 0], V[:, 1], color=['g', 'b', 'grey', 'red', 'red'], scale=1)

        def update_quiver(i,Q):
            if i >= len(self.w_vec) - 1:
                return Q,
            x_vec_len = sum([ i**2 for i in self.x_vec[0][:2]])**(1/2)
            w_vec_len = sum([ i**2 for i in self.w_vec[0][:2]])**(1/2)
            n = [(i*j)/(w_vec_len) for i, j in zip(self.x_vec[0][:2], self.w_vec[i+1][:2])]

            V = np.array([self.x_vec[i][:2], 
                          self.w_vec[i + 1][:2], 
                          self.w_vec[i][:2],
                          n,
                          [-1*n[0], -1*n[1]]])
            Q.set_UVC(V[:, 0], V[:, 1])
            return Q,
        
        anim = animation.FuncAnimation(fig, update_quiver, frames=60, fargs=(Q, ), interval=500, blit=False)
        plt.show()


    def add_info(self, x_vec, y_vec):
        self.x_vec = x_vec 
        self.y_vec = y_vec
        
