from board import Board

test = Board(5)
map = test.get_map()

map[0][0] = 22

print(test.get_map())