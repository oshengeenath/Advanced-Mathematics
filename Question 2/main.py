import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as sfft

x = np.arange(-5, 5, 0.1)
x1 = np.arange(-5, 5, 1)

y = np.cos(20 * x)
y1 = np.cos(20 * x1)

yf = sfft.fft(y)
yf1 = sfft.fft(y1)

yf_ = sfft.ifft(yf)
yf1_ = sfft.ifft(yf1)

plt.plot(x, y)
plt.plot(x1, y1)
plt.plot(x, np.real(yf_))
plt.plot(x1,np.real(yf1_))
plt.legend(["100Hz", "10Hz", "ifft 100Hz", "ifft 10Hz"])
plt.show()
