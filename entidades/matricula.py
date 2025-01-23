class Matricula:
	def __init__(self, curso, estudante, data, lst_notas = []):
		self.__curso = curso
		self.__estudante = estudante
		self.__data = data
		self.__lst_notas = lst_notas
	
	# to string
	def __str__(self):
		return f'Curso: {self.__curso.get_nome()}, Estudante: {self.__estudante.get_nome()}, Data: {self.__data}, Notas: {self.get_notas()}'
		
	# gets e sets
	def get_curso(self):
		return self.__curso
	
	def set_curso(self, curso):
		self.__curso = curso
	
	def get_estudante(self):
		return self.__estudante
	
	def set_estudante(self, estudante):
		self.__estudante = estudante
	
	def get_data(self):
		return self.__data
			
	def set_data(self, data):
		self.__data = data
	
	def get_notas(self):
		return self.__lst_notas
	
	def set_notas(self, notas):
		self.__lst_notas = notas
		
	def add_nota(self, nota):
		self.__lst_notas.append(nota)