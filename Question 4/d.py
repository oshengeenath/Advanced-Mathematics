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

imgc=sfft.dct((sfft.dct(img,norm='ortho')).T,norm='ortho')

imgc2 = imgc[0:240,0:240]
img1 = sfft.idct((sfft.idct(imgc2,norm='ortho')).T,norm='ortho')
plt.imshow(img1)
plt.show()

mgcl =np.zeros((360,360))
imgcl = imgc[:160,:160]
imgl = sfft.idct((sfft.idct(imgcl,norm='ortho')).T,norm='ortho')
plt.imshow(imgl)
plt.show()