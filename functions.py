from progress.bar import IncrementalBar
from PIL import Image, ImageDraw

def help():
	print('1. Contrast - функция изменения контраста. Значения могут быть дробными но не превышать диапазон от -50000 до +50000. 0 - нулевая контрастность, 1 - контрастность как в оригинале')
	print('2. Saturation - фукция изменения насыщености. Значения могут быть дробными но не превышать диапазон от -50000 до +50000. 0 - нулевая насыщеность (чб), 1 - насыщеность как в оригинале')
	print('3. Black and white - фукция преобразования изображения в градации серого')
	print('4. Inverse - фукция инвертирования цветов изображения')
	print('5. Blur - гаусовское размытие с  радиусом 1')
	print('6. Noise - функция доюавления шума на изображение. Значения могут быть дробными но не превышать диапазон от -50000 до +50000')
	print('7. Median - функция медианной фильтрации. Подходит для удаления шума типа соль и перец')
	print('8. Resize - функция увеличения изображения в 3 раза')
	print('9. Brightnes - функция изменения яркости изображения. Значения могут быть дробными но не превышать диапазон от -50000 до +50000')
	print('10. Line - функция определения контура')

def logo():
	print(r'▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')
	print(r'▓                                                               ▓')
	print(r'▓   ____            ____   ________        __        ______     ▓')
	print(r'▓   \   \          /   /  |    ____|      /  |      /  __  \    ▓')
	print(r'▓    \   \        /   /   |   |          /_  |      | |  | |    ▓')
	print(r'▓     \   \  /\  /   /    |   |___         | |      | |  | |    ▓')
	print(r'▓      \   \/  \/   /     |    ___|        | |      | |  | |    ▓')
	print(r'▓       \          /      |   |          __| |__    | |__| |    ▓')
	print(r'▓        \___/\___/       |___|         |_______| ▓ \______/    ▓')
	print(r'▓                                                               ▓')
	print(r'▓                                                               ▓')
	print(r'▓                                                               ▓')
	print(r'▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓')

def add_str(img):
	pix = img.load()
	out = Image.new("RGB", (img.size[0]+2, img.size[1]+2))
	dr_o = ImageDraw.Draw(out)

	for i in range(img.size[0]):
		dr_o.point((i+1, 0), (pix[i, 0]))
	for i in range(img.size[0]):
		dr_o.point((i+1, out.size[1]-1), (pix[i, img.size[1]-1]))
	for i in range(img.size[1]):
		dr_o.point((0, i+1), (pix[0, i]))
	for i in range(img.size[1]):
		dr_o.point((out.size[0]-1, i+1), (pix[img.size[0]-1, i]))

	for i in range(img.size[0]):
		for j in range(img.size[1]):
			dr_o.point((i+1, j+1), (pix[i, j]))

	dr_o.point((0, 0), (pix[0, 0]))
	dr_o.point((0, out.size[1]-1), (pix[0, img.size[1]-1]))
	dr_o.point((out.size[0]-1, 0), (pix[img.size[0]-1, 0]))
	dr_o.point((out.size[0]-1, out.size[1]-1), (pix[img.size[0]-1, img.size[1]-1]))

	return out

def contrast(img, k):
	bar = IncrementalBar('Progress', max = img.size[0])
	pix = img.load()

	out = Image.new("RGB", (img.size[0], img.size[1]))
	dr_o = ImageDraw.Draw(out)

	r = 0
	g = 0
	b = 0

	for i in range(img.size[0]):
		for j in range(img.size[1]):
			r += pix[i, j][0]
			g += pix[i, j][1]
			b += pix[i, j][2]
	
	rs = int(r / (img.size[0]*img.size[1]))
	gs = int(g / (img.size[0]*img.size[1]))
	bs = int(b / (img.size[0]*img.size[1]))

	for i in range(img.size[0]):
		for j in range(img.size[1]):
			(r, g, b) = (pix[i, j][0], pix[i, j][1], pix[i, j][2])
			rk = int(((r - rs)*k)+rs)
			gk = int(((g - gs)*k)+gs)
			bk = int(((b - bs)*k)+bs)

			if rk>255:
				rk=255
			if rk<0:
				rk = 0
			if gk>255:
				gk=255
			if gk<0:
				gk = 0
			if bk>255:
				bk=255
			if bk<0:
				bk = 0

			dr_o.point((i, j), (rk, gk, bk))
		bar.next()

	return out

def noise(img, k):
	from random import randint
	bar = IncrementalBar('Progress', max = img.size[0])
	pix = img.load()

	out = Image.new("RGB", (img.size[0], img.size[1]))
	dr_o = ImageDraw.Draw(out)

	for i in range(img.size[0]):
		for j in range(img.size[1]):
			r = randint(0, int(k))-int(k/2)
			rk = pix[i, j][0]+r
			gk = pix[i, j][1]+r
			bk = pix[i, j][2]+r

			if rk>255:
				rk=255
			if rk<0:
				rk = 0
			if gk>255:
				gk=255
			if gk<0:
				gk = 0
			if bk>255:
				bk=255
			if bk<0:
				bk = 0

			dr_o.point((i, j), (rk, gk, bk))
		bar.next()
	return out

def bw(img):
	bar = IncrementalBar('Progress', max = img.size[0])
	pix = img.load()

	out = Image.new("RGB", (img.size[0], img.size[1]))
	dr_o = ImageDraw.Draw(out)

	for i in range(img.size[0]):
		for j in range(img.size[1]):
			s = int(pix[i, j][0]*0.2989 + pix[i, j][1]*0.5870 + pix[i, j][2]*0.114)
			dr_o.point((i, j), (s, s, s))
		bar.next()
	return out

def saturation(img, k):
	bar = IncrementalBar('Progress', max = img.size[0])
	pix = img.load()

	out = Image.new("RGB", (img.size[0], img.size[1]))
	dr_o = ImageDraw.Draw(out)

	for i in range(img.size[0]):
		for j in range(img.size[1]):
			s = (pix[i, j][0] + pix[i, j][1] + pix[i , j][2])/3
			rr = int(((pix[i, j][0] - s)*(k-1))+pix[i, j][0])
			gr = int(((pix[i, j][1] - s)*(k-1))+pix[i, j][1])
			br = int(((pix[i, j][2] - s)*(k-1))+pix[i, j][2])
			if rr>255:
				rr = 255
			if rr<0:
				rr = 0
			if gr>255:
				gr = 255
			if gr<0:
				gr = 0
			if br>255:
				br = 255
			if br<0:
				br = 0
			dr_o.point((i, j), (rr, gr, br))
		bar.next()
	return out

def invert(img):
	pix = img.load()
	bar = IncrementalBar('Progress', max = img.size[0])

	out = Image.new("RGB", (img.size[0], img.size[1]))
	dr_o = ImageDraw.Draw(out)

	for i in range(img.size[0]):
		for j in range(img.size[1]):
			dr_o.point((i, j), (255-pix[i, j][0], 255-pix[i, j][1], 255-pix[i, j][2]))
		bar.next()
	return out

def blur(img):
	bar = IncrementalBar('Progress', max = img.size[0])
	img = add_str(img)
	pix = img.load()

	out = Image.new("RGB", (img.size[0]-2, img.size[1]-2))
	dr_o = ImageDraw.Draw(out)

	for i in range(1, img.size[0]-1):
		for j in range(1, img.size[1]-1):
			rs = (pix[i-1, j-1][0] + pix[i, j-1][0] + pix[i+1, j-1][0] + pix[i-1, j][0] + pix[i+1, j][0] + pix[i-1, j+1][0] + pix[i, j+1][0] + pix[i+1, j+1][0])/8
			gs = (pix[i-1, j-1][1] + pix[i, j-1][1] + pix[i+1, j-1][1] + pix[i-1, j][1] + pix[i+1, j][1] + pix[i-1, j+1][1] + pix[i, j+1][1] + pix[i+1, j+1][1])/8
			bs = (pix[i-1, j-1][2] + pix[i, j-1][2] + pix[i+1, j-1][2] + pix[i-1, j][2] + pix[i+1, j][2] + pix[i-1, j+1][2] + pix[i, j+1][2] + pix[i+1, j+1][2])/8
			dr_o.point((i-1, j-1), (int(rs), int(gs), int(bs)))
		bar.next()
	return out

def siz(img):
	bar = IncrementalBar('Progress', max = img.size[0])
	img = add_str(img)
	pix = img.load()

	out = Image.new("RGB", ((img.size[0]-2)*3, (img.size[1]-2)*3))
	dr_o = ImageDraw.Draw(out)

	for i in range(img.size[0]-2):
		for j in range(img.size[1]-2):
			dr_o.point((i*3, j*3), (pix[i, j]))
			dr_o.point((i*3+1, j*3), (pix[i+1, j]))
			dr_o.point((i*3+2, j*3), (pix[i+2, j]))
			dr_o.point((i*3, j*3+1), (pix[i, j+1]))
			dr_o.point((i*3+1, j*3+1), (pix[i+1, j+1]))
			dr_o.point((i*3+2, j*3+1), (pix[i+2, j+1]))
			dr_o.point((i*3, j*3+2), (pix[i, j+2]))
			dr_o.point((i*3+1, j*3+2), (pix[i+1, j+2]))
			dr_o.point((i*3+2, j*3+2), (pix[i+2, j+2]))
		bar.next()
	return out

def median(img):
	bar = IncrementalBar('Progress', max = img.size[0])
	img = add_str(img)
	pix = img.load()

	out = Image.new("RGB", (img.size[0]-2, img.size[1]-2))
	dr_o = ImageDraw.Draw(out)
	pos = 4
	for i in range(img.size[0]-2):
		for j in range(img.size[1]-2):
			x = i+1
			y = j+1
			rgb_list = [[pix[x-1, y-1][0], pix[x-1, y-1][1], pix[x-1, y-1][2]], [pix[x, y-1][0], pix[x, y-1][1], pix[x, y-1][2]], [pix[x+1, y-1][0],pix[x+1, y-1][1], pix[x+1, y-1][2]], [pix[x-1, y][0], pix[x-1, y][1], pix[x-1, y][2]], [pix[x, y][0], pix[x, y][1], pix[x, y][2]], [pix[x+1, y][0], pix[x+1, y][1], pix[x+1, y][2]], [pix[x-1, y+1][0], pix[x-1, y+1][1], pix[x-1, y+1][2]], [pix[x, y+1][0], pix[x, y+1][1], pix[x, y+1][2]], [pix[x+1, y+1][0], pix[x+1, y+1][1], pix[x+1, y+1][2]]]
			s_list = [int((pix[x-1, y-1][0]+ pix[x-1, y-1][1]+ pix[x-1, y-1][2])/3), int((pix[x, y-1][0]+pix[x, y-1][1]+pix[x, y-1][2])/3), int((pix[x+1, y-1][0]+pix[x+1, y-1][1]+pix[x+1, y-1][2])/3),int((pix[x-1, y][0]+pix[x-1, y][1]+pix[x-1, y][2])/3), int((pix[x, y][0]+pix[x, y][1]+pix[x, y][2])/3),int((pix[x+1, y][0]+pix[x+1, y][1]+pix[x+1, y][2])/3), int((pix[x-1, y+1][0]+pix[x-1, y+1][1]+pix[x-1, y+1][2])/3), int((pix[x, y+1][0]+pix[x, y+1][1]+pix[x, y+1][2])/3), int((pix[x+1, y+1][0]+pix[x+1, y+1][1]+pix[x+1, y+1][2])/3)]
			for m in range(8):
				for n in range(8):
					if s_list[n]>s_list[n+1]:
						rgb_prom = rgb_list[n]
						s_prom = s_list[n]
						rgb_list[n]=rgb_list[n+1]
						s_list[n] = s_list[n+1]
						rgb_list[n+1]=rgb_prom
						s_list[n+1]=s_prom
			dr_o.point((i, j), (rgb_list[pos][0], rgb_list[pos][1], rgb_list[pos][2]))
		bar.next()
	return out

def brightnes(img, k):
	bar = IncrementalBar('Progress', max = img.size[0])
	pix = img.load()

	out = Image.new("RGB", (img.size[0], img.size[1]))
	dr_o = ImageDraw.Draw(out)

	for i in range(img.size[0]):
		for j in range(img.size[1]):
			(r, g, b) = pix[i, j]

			red = int(r + k)
			red = min(255, max(0, red)) 
			green = int(g + k)
			green = min(255, max(0, green))
			blue = int(b + k)
			blue = min(255, max(0, blue))
			dr_o.point((i, j), (red, green, blue))
		bar.next()
	return out

def kont(img):
	bar = IncrementalBar('Progress', max = img.size[0])
	img = add_str(img)
	pix = img.load()

	out = Image.new("RGB", (img.size[0]-2, img.size[1]-2))
	dr_o = ImageDraw.Draw(out)

	for i in range(img.size[0]-2):
		for j in range(img.size[1]-2):
			sr_r = (pix[i, j][0]+pix[i+1, j][0]+pix[i+2, j][0]+pix[i, j+1][0]+pix[i+2, j+1][0]+pix[i, j+2][0]+pix[i+1, j+2][0]+pix[i+2, j+2][0])/8
			sr_g = (pix[i, j][1]+pix[i+1, j][1]+pix[i+2, j][1]+pix[i, j+1][1]+pix[i+2, j+1][1]+pix[i, j+2][1]+pix[i+1, j+2][1]+pix[i+2, j+2][1])/8
			sr_b = (pix[i, j][2]+pix[i+1, j][2]+pix[i+2, j][2]+pix[i, j+1][2]+pix[i+2, j+1][2]+pix[i, j+2][2]+pix[i+1, j+2][2]+pix[i+2, j+2][2])/8
			s_p = (sr_r+sr_g+sr_b)/3
			r_r = abs(sr_r-pix[i+1, j+1][0])
			r_g = abs(sr_g-pix[i+1, j+1][1])
			r_b = abs(sr_b-pix[i+1, j+1][2])
			r_p = int((r_r+r_g+r_b)/3)
			dr_o.point((i+1, j+1), ((r_p, r_p, r_p)))
		bar.next()
	return out
