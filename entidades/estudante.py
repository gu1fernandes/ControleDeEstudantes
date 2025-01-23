class Estudante:
	def __init__(self, nome, data_nasc, id, matriculas = []):
		self.__nome = nome
		self.__data_nasc = data_nasc
		self.__id = id
		self.__lst_matriculas = matriculas

	# to string
	def __str__(self):
		return f'Nome: {self.__nome}, Nasc: {self.__data_nasc}, ID: {self.__id}'
	
	# gets e sets
	def get_nome(self):
		return self.__nome
	
	def set_nome(self, nome):
		self.__nome = nome
	
	def get_nasc(self):
		return self.__data_nasc
	
	def set_nasc(self, data_nasc):
		self.__data_nasc = data_nasc
	
	def get_id(self):
		return self.__id
	
	def get_matriculas(self):
		return self.__lst_matriculas
	
	def set_matriculas(self, matriculas):
		self.__lst_matriculas = matriculas