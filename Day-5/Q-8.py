class player:
	player_count = 0
	def __init__(self, name, level):
		self.name = name
		self.level = level
		player.player_count += 1


p1 = player("SK", 5)
p2 = player("RK", 9)
p3 = player("CK", 7)

print("Total players:", player.player_count)
		