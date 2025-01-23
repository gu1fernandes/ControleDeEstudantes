class Curso:
	def __init__(self, nome, cod, carga):
		self.__nome = nome
		self.__cod = cod
		self.__carga = carga
	
	# to string
	def __str__(self):
		return f'Nome: {self.__nome}, Carga: {self.__carga}, CÓD: {self.__cod}'
	
	# gets e sets
	def get_nome(self):
		return self.__nome
		
	def set_nome(self, nome):
		self.__nome = nome
	
	def get_cod(self):
		return self.__cod
	
	def set_cod(self, cod):
		self.__cod = cod
	
	def get_carga(self):
		return self.__carga
	
	def set_carga(self, carga):
		self.__carga = carga