import numpy as np
import scipy.special
from scipy.stats import beta
import matplotlib.pyplot as plt
import imageio
from mpl_toolkits.mplot3d import Axes3D

def plot_circle_val(num):
    nx = np.random.uniform(-1,1,num)
    ny = np.random.uniform(-1,1,num)
    nz = np.random.uniform(-1,1,num)
    x = []
    y = []
    pi = 0
    for i in range(len(nx)):
        f = nx[i]**2 + ny[i]**2
        if f<1 :
            # plot x,y with red
            x.append(nx[i])
            y.append(ny[i])
            pi += 1
    pi *= (4.0/num)
    print("pi for "+str(num)+" points is ")
    print(pi)
    #plt.plot([nx[i] for i in red], [ny[i] for i in red], 'ro')
    #plt.plot([nx[i] for i in blue], [ny[i] for i in blue], 'bo')
    #plt.show()
    plt.figure(figsize = [8,8])
    plt.scatter(nx,ny,color = 'b' , s = 2)
    plt.scatter(x,y,color = 'r' , s = 2)
    plt.title("Pi Approximation (Samples = {})".format(num))
    plt.savefig("Circle Fig {}.png".format(num))
    plt.close()

def plot_sphere_val(num):
    nx = np.random.uniform(-1,1,num)
    ny = np.random.uniform(-1,1,num)
    nz = np.random.uniform(-1,1,num)
    x = []
    y = []
    z = []
    pi = 0
    for i in range(len(nx)):
        f = nx[i]**2 + ny[i]**2 + nz[i]**2
        if f<1 :
        	x.append(nx[i])
        	y.append(ny[i])
        	z.append(nz[i])
        	pi = pi + 1
    pi *= (6.0/num)
    print("pi for "+str(num)+" points is ")
    print(pi)
    #plt.plot([nx[i] for i in red], [ny[i] for i in red], 'ro')
    #plt.plot([nx[i] for i in blue], [ny[i] for i in blue], 'bo')
    #plt.show()
    fig = plt.figure(figsize = [8, 8])
    ax = fig.add_subplot(111, projection = '3d')
    ax.scatter(x, y, z, color = 'r', s = 6)   # Plotting only the inner points
    plt.title("Pi Approximation (Samples = {})".format(num))
    #plt.show()
    plt.savefig("Sphere Fig {}.png".format(num))
    plt.close()

def main():
    print("spherical Approximation")
    for i in range(1,8):
        plot_sphere_val(10**i)
    print("circle Approximation")
    for i in range(1,8):
        plot_circle_val(10**i)

if __name__ == "__main__":
	main()
