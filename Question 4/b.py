import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.fftpack as sfft
import scipy.signal as signal

img = mpimg.imread('Fruit.jpg')

kernel = np.outer(signal.gaussian(360,5),signal.gaussian(360,5))
kf = sfft.fft2(sfft.ifftshift(kernel)) # freq domain kernel
imgf = sfft.fft2(img)
img_b = imgf*kf
imgg = sfft.ifft2(img_b)
plt.imshow(np.abs(imgg))
plt.show()