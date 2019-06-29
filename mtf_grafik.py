#!/usr/bin/env python

#ihtiyacımız olan kütüphaneleri import ediyoruz
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from scipy.signal import find_peaks
from scipy import optimize
import pandas as pd
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score



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
		peaks1, _1 = find_peaks(x, height=0)
		peaks2, _2= find_peaks(y, height=0)

		peak_degerleri1 = []
		peak_degerleri2 = []

		for i in _2.values():
			peak_degerleri2.append(i)

		for i in _1.values():
			peak_degerleri1.append(i)


		peak_degerleri_numpy1 = np.array(peak_degerleri1)
		peak_degerleri_numpy2 = np.array(peak_degerleri2)

		zero_noktasi1 = np.zeros_like(peak_degerleri1)
		zero_noktasi2 = np.zeros_like(peak_degerleri2)

		a = peak_degerleri1 - zero_noktasi1
		b = peak_degerleri2 - zero_noktasi2

				
		x1 = peaks1.reshape(21)
		y1 = a.reshape(21)

		#linear regression'ın yapıldığı yer
		coefint1 = np.polyfit(x1,y1,1)
		coefint2 = np.polyfit(x1,y1,2)
		coefint3 = np.polyfit(x1,y1,3)
		coefint4 = np.polyfit(x1,y1,4)
		coefint5 = np.polyfit(x1,y1,5)


		x2 = peaks1.reshape(21)
		y2 = a.reshape(21)

		#linear regression'ın yapıldığı yer
		coefint1 = np.polyfit(x2,y2,1)
		coefint2 = np.polyfit(x2,y2,2)
		coefint3 = np.polyfit(x2,y2,3)
		coefint4 = np.polyfit(x2,y2,4)
		coefint5 = np.polyfit(x2,y2,5)
		

		#regression'ı çiz
		plt.plot(x2,y2, "o", color="green")
		plt.plot(x2, np.polyval(coefint4,x2),"r")
		plt.plot(x1,y1, "o", color="green")
		plt.plot(x1, np.polyval(coefint4,x1),"r")

		plt.ylabel("mtf")
		plt.ylim(0,1.1)
		plt.show()



	except IOError:
		print("Fotoğraf Seçilmedi")

if __name__ == "__main__":
	main("test2.png")
