temp = input().split("\t")
# print(temp)
n = temp[0]
m = temp[1]
parkingLot = {
	'cols': int(n),
	'rows':	int(m),
}

def rotate_clockwise(shape):
	return [ [ shape[y][x]
			for y in range(len(shape)) ]
		for x in range(len(shape[0]) - 1, -1, -1) ]

def check_collision(board, shape, offset):
	off_x, off_y = offset
	for cy, row in enumerate(shape):
		for cx, cell in enumerate(row):
			try:
				if cell and board[ cy + off_y ][ cx + off_x ]:
					return False
			except IndexError:
				return False
	return True

def join_matrixes(mat1, mat2, mat2_off):
	off_x, off_y = mat2_off
	for cy, row in enumerate(mat2):
		for cx, val in enumerate(row):
			mat1[cy+off_y][cx+off_x] += val
	return mat1

def draw_Matrix(cols, rows, value):
	board = [ [ value for x in range(cols) ]
			for y in range(rows) ]
	return board

def parking_lot(parking, car, rotate):
    for x in range(parkingLot['cols']):
        for y in range(parkingLot['rows']):
            if (int(rotate) == 1):
                # print("There's a Rotation")
                car = rotate_clockwise(car)

            if ( check_collision(parking, car, (x, y)) ):
                join_matrixes(parking, car, (x, y))
                return True

def check_availablity(parking):
    checked = draw_Matrix(1, 1, 0)

    for x in range(parkingLot['cols']):
        for y in range(parkingLot['rows']):
            if ( check_collision(parking, checked, (x, y)) ):
                return True
            else:
                return False
    return False

def check_parking_lot(parking, car_space):
    mat1 = draw_Matrix(1, 1, 0)
    blank_space = False
    sum = 0

    for x in range(parkingLot['cols']):
        for y in range(parkingLot['rows']):
            if (parking[y][x] == mat1[0][0]):
                blank_space = True

    if ( blank_space and car_space != sum ):
        return
    else:     
        show_parking_lot(parking)


def show_parking_lot(parking):
    for j in parking:
        print(*j)

parking_sequence = []
def gen_seq(string, index): 
    if index == len(string): 
        parking_sequence.append(''.join(string))
        return
  
    if string[index] == "?": 
  
        string[index] = '0'
        gen_seq(string, index + 1) 
  
        string[index] = '1'
        gen_seq(string, index + 1) 
  
        string[index] = '?'
    else: 
        gen_seq(string, index + 1)  

def main():
    j = input()
    j = int(j)
    car_config = []
    for n in range(j):
        temp = input().split("\t")
        lenght = temp[0]
        width = temp[1]
        temp = (int(lenght), int(width))
        car_config.append(temp)
    cars = []
    car_space = 0
    a = [i for i in range(j+1)]
    k = 1
    for i in car_config:
        car_space += i[0] * i[1] * a[k]
        k += 1

    for i in range(j):
        carLen = car_config[i][0]
        carWid = car_config[i][1]
        car = draw_Matrix(carLen, carWid, i+1)
        cars.append(car)

    string = "?" * j
    string = list(string)
    gen_seq(string, 0)
    ro = parking_sequence
    count = 0

    for index in ro:
        parking = draw_Matrix(parkingLot['cols'], parkingLot['rows'], 0)
        for i in range(j):
            if ( check_availablity(parking) ):
                parking_lot(parking, cars[i], index[i])
        check_parking_lot(parking, car_space)
        
        count = count + 1

main()