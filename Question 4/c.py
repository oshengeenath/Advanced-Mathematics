import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import scipy.fftpack as sfft
img = mpimg.imread('Fruit.jpg')

imgc=sfft.dct((sfft.dct(img,norm='ortho')).T,norm='ortho')

imgc2 = imgc[0:240,0:240]
img1 = sfft.idct((sfft.idct(imgc2,norm='ortho')).T,norm='ortho')
plt.imshow(img1)
plt.show()