parkingLot = {
	'cols':		 7,
	'rows':		 5,
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

def parking_lot(parking, car):
    for x in range(parkingLot['cols']):
        # print("cols", x)
        for y in range(parkingLot['rows']):
            # print("rows", y)
            if ( check_collision(parking, car, (x, y)) ):
                join_matrixes(parking, car, (x, y))
                return True
            
    return False

def show_parking_lot(parking):
    for i in parking:
        print(i)
        # for j in i:

def main():
    parking = draw_Matrix(parkingLot['cols'], parkingLot['rows'], 0)
    j = 7
    car = [(4, 2), (3, 2), (1, 2), (2, 5), (2, 2), (2, 1), (3, 1)]
    for i in range(j):
        carLen = car[i][0]
        carWid = car[i][1]

        car1 = draw_Matrix(carLen, carWid, i+1)
        # car1 = 
        if ( parking_lot(parking, car1) ):
            continue
        else:
            car1 = rotate_clockwise(car1)
            parking_lot(parking, car1)
    return parking

pko = main()
show_parking_lot(pko)

