from PIL import Image, ImageDraw
import functions as func
import os
import time

func.logo()
time.sleep(3)
os.system("cls")
func.help()
print('\n')

while (True):
	inter = 0

	name = input('Name file: ')
	if name=='answ':
		img = out
	else:
		name_lock = name
		try:
			img = Image.open(name_lock)
		except FileNotFoundError:
			print('File not found!')
			inter = 1
	name_with = name[0:name.find('.')]
	
	if not(inter==1):
		print('1. Contrast')
		print('2. Saturation')
		print('3. Black and white')
		print('4. Inverse')
		print('5. Blur')
		print('6. Noise')
		print('7. Median')
		print('8. Resize')
		print('9. Brightnes')
		print('10. Line')

		cmd = input('Operation: ')
		if cmd=='1':
			print('-Contrast-')
			k = float(input('Coefficient: '))
			out = func.contrast(img, k)
			out.save(name_with+'_contrst_'+str(k)+'.png', "PNG")
		if cmd=='2':
			print('-Saturation-')
			k = float(input('Coefficient: '))
			out = func.saturation(img, k)
			out.save(name_with+'_saruration_'+str(k)+'.png', "PNG")
		if cmd=='3':
			print('-Black and white-')
			out = func.bw(img)
			out.save(name_with+'_bw.png', "PNG")
		if cmd=='4':
			print('-Inverse-')
			out = func.invert(img)
			out.save(name_with+'_invert.png', "PNG")
		if cmd=='5':
			print('-Blur-')
			out = func.blur(img)
			out.save(name_with+'_blur.png', "PNG")
		if cmd=='6':
			print('-Noise-')
			k = float(input('Coefficient: '))
			out = func.noise(img, k)
			out.save(name_with+'_noise_'+str(k)+'.png', "PNG")
		if cmd=='7':
			print('-Median-')
			out = func.median(img)
			out.save(name_with+'_median.png', "png")
		if cmd=='8':
			k = int(input('Quantity: '))
			print('-Resize-')
			out = func.siz(img)
			print()
			for i in range(k):
				out = func.median(out)
				print()
			out.save(name_with+'_resizemedian_'+str(k)+'.png', "PNG")
		if cmd=='9':
			print('-Brightnes-')
			k = float(input('Coefficient: '))
			out = func.brightnes(img, k)
			out.save(name_with+'_brightnes_'+str(k)+'.png', "PNG")
		if cmd=='10':
			print('-Line-')
			out = func.kont(img)
			out.save(name_with+'_kont.png', "PNG")
		if cmd=='2004':
			print('-?????-')
			out = func.siz(img)
			out.save(name_with+'_size.png', "PNG")
	os.system("cls")