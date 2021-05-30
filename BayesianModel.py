import numpy as np
import scipy.special
from scipy.stats import beta
import matplotlib.pyplot as plt
import imageio

def plot_beta(a, b,count):
    fig, ax = plt.subplots(figsize=(10,5))
    # a, b = 2, 3
    mean, var, skew, kurt = beta.stats(a, b, moments='mvsk')
    y = np.linspace(0, 1, 100)
    ax.plot(y, beta.pdf(y, a, b), label='beta pdf')
    ax.grid()
    ax.set_ylim(0, 20)
    fig.canvas.draw()
    image = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8')
    image  = image.reshape(fig.canvas.get_width_height()[::-1] + (3,))
    plt.title("curve Fig a={} b={}.png".format(a,b))
    plt.savefig("curve Fig {}.png".format(count))
    plt.close()
    return image

def main():
    n = np.random.random([150,1])
    data = []
    for val in n:
        if(val<0.5):
            data.append(0)
        else:
            data.append(1)

    data = np.array(data)
    count = 0
    # print(data)
    a = 2
    b = 3
    img_list = []
    img_list.append(plot_beta(a, b,count))
    for i in data:
        count = count + 1
        if i==0:
            a += 1
            img_list.append(plot_beta(a, b,count))
        else:
            b += 1
            img_list.append(plot_beta(a, b,count))

    kwargs_write = {'fps':1.0, 'quantizer':'nq'}
    imageio.mimsave('graph.gif', img_list, format='GIF', duration=0.25)
    plot_beta(a,b,151)

if __name__ == "__main__":
	main()
