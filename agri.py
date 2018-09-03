import os
import psycopg2
DB_URL = os.environ['DATABASE_URL']

connection = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

print("Test")

"""class Coordinates:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		
class User:
	def __init__(self, name, coords, desc):
		self.arg = arg

	def create(self):
		pass

	@property
	def commit(self):
		
"""