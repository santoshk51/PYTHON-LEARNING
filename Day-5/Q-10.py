class User:
	def __init__(self, username ):
		self.username = username

	def send_message(self, chatRoom, text):
		chatRoom.send_message(self, text)
		