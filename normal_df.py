import math
def normal_pdf(x, mu=0, sigma=1):
    # TODO
    # hits: math.exp
    var = float(sigma)**2
    dnm = (2*math.pi*var)**.5
    num = math.exp(-(float(x)-float(mu))**2/(2*var))
    return num/dnm

from matplotlib import pyplot as plt
xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mu=0,sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '-', label='mu=0,sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], '-', label='mu=0,sigma=0.5')
plt.plot(xs, [normal_pdf(x, sigma=-1) for x in xs], '-', label='mu=0,sigma=-1')
plt.legend()
plt.show()
