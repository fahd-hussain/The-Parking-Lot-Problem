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

def parking_lot(parking, car, rotate):
    # print(rotate, type(rotate))
    for x in range(parkingLot['cols']):
        for y in range(parkingLot['rows']):
            # print(type(rotate))
            if (int(rotate) == 1):
                # print("Rotation ho rai hai")
                car = rotate_clockwise(car)

            if ( check_collision(parking, car, (x, y)) ):
                join_matrixes(parking, car, (x, y))
                return True

def check_availablity(parking):
    checked = draw_Matrix(1, 1, 0)
    for x in range(parkingLot['cols']):
        for y in range(parkingLot['rows']):
            if ( check_collision(parking, checked, (x,y)) ):
                return True
    return False

def show_parking_lot(parking):
    for i in parking:
        print(i)

parking_sequence = []
def gen_seq(string, index): 
    if index == len(string): 
        # print(''.join(string))
        parking_sequence.append(''.join(string))
        return
  
    if string[index] == "?": 
  
        # replace '?' by '0' and recurse 
        string[index] = '0'
        gen_seq(string, index + 1) 
  
        # replace '?' by '1' and recurse 
        string[index] = '1'
        gen_seq(string, index + 1) 
  
        string[index] = '?'
    else: 
        gen_seq(string, index + 1)  

def main():
    parking = draw_Matrix(parkingLot['cols'], parkingLot['rows'], 0)
    j = 7

    car_config = [(4, 2), (3, 2), (1, 2), (2, 5), (2, 2), (2, 1), (3, 1)]
    cars = []
    # for i in range(j):
    for i in range(j):
        carLen = car_config[i][0]
        carWid = car_config[i][1]
        car = draw_Matrix(carLen, carWid, i+1)
        cars.append(car)

    # print(cars)
    # ro = [[0,1,1,0,0,1,1], [0,1,1,0,0,1,0], [0,1,1,0,0,0,0]]
    string = "???????"
    string = list(string)
    gen_seq(string, 0)
    ro = parking_sequence
    rotate = "0110011"
    count = 0

    for index in ro:
        print(index)
    # while ( count < (60) ):
        print(count)
        for i in range(j):
            # print(index[i])
            if ( check_availablity(parking) ):
                # print(ro[count][i])
                parking_lot(parking, cars[i], index[i])
            # print(parking)
                # parking_lot(parking, cars[i], ro[count][i])
            print(parking)
        count = count + 1
    return parking

main()
# pko = main()
# show_parking_lot(pko)

#   0110011