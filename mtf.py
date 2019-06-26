#!/usr/bin/env python

#ihtiyacımız olan kütüphaneleri import ediyoruz
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.signal import find_peaks



def main(picture):
	try:
		##Elimizdeki veriyi okutuyoruz.
		img = Image.open(picture)
		pix = img.load()
		
		#Verinin boyutlarını tuple'dan int'e çeviriyoruz
		image_size = img.size
		image_height = image_size[1]
		image_width = image_size[0]


		
		
		
		#fotoğrafın alt tarafı blurred olduğu için 2 farklı çıktı alacağız, her pixelsin konum ve renk bilgisi için dictionary kullanıyoruz.
		colors_dict1 = {}
		colors_dict2 = {}
		
		i = 1
		while i < image_width:
			colors_dict1.update({i : (pix[i, (image_height/2)] / 255)})
			i += 1

		i = 1
		while i < image_width:
			colors_dict2.update({i : (pix[i, (image_height/2 + 1)] / 255)})
			i += 1
		
		#Elde edilen değerler üzerinden işlem yapabilmek için dictionary formatından matrix formatına çeviriyoruz.
		degerler1 = np.fromiter(colors_dict1.values(), dtype=float)
		degerler2 = np.fromiter(colors_dict2.values(), dtype=float)

		x = degerler1
		y = degerler2
		
		#Her iki farklı grafik için de peak yaptığı noktaları buluyoruz.
		peaks1, _ = find_peaks(x, height=0)
		peaks2, _ = find_peaks(y, height=0)
		
		
		plt.plot(peaks1, x[peaks1], "x", color="green")
		plt.plot(peaks2, y[peaks2], "x", color="gray")
		
		#dictionary de key-value çiftlerini list tipine çevirip key ve value'lara göre grafik çizilir.
		lists1 = sorted(colors_dict1.items())
		lists2 = sorted(colors_dict2.items())
		x1, y1 = zip(*lists1)
		x2, y2 = zip(*lists2)

		plt.plot(x1, y1, color = "red")
		plt.plot(x2, y2, color = "blue")
		plt.show()



	except IOError:
		print("Fotoğraf Seçilmedi")

if __name__ == "__main__":
	main("test2.png")
