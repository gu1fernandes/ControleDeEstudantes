# Singleton
class BancoDeDados:
	# variavel de classe
	_instancia = None
	
	# metodo singletom
	def __new__(cls, *args, **kwargs):
		if not cls._instancia:
			cls._instancia = super().__new__(cls)
		
		return cls._instancia	
	
	# inicializador
	def __init__(self, lst_estudantes = [], lst_cursos = [], lst_matriculas = []):
		if not hasattr(self, 'lst_estudantes'):
			self.__lst_estudantes = lst_estudantes
		
		if not hasattr(self, 'lst_cursos'):
			self.__lst_cursos = lst_cursos
			
		if not hasattr(self, 'lst_matriculas'):
			self.__lst_matriculas = lst_matriculas
			
	########################
	
	# estudante: adicionar
	def add_estudante(self, estudante):
		self.__lst_estudantes.append(estudante)
	
	# estudante: pegar lista
	def get_estudantes(self):
		return self.__lst_estudantes
	
	# estudante: buscar por ID
	def buscar_estudante(self, id):
		for e in self.__lst_estudantes:
			if e.get_id() == id:
				return e
				
		return None
	
	# estudante: editar
	def editar_estudante(self, estudante):
		for e in self.__lst_estudantes:
			if e.get_id() == estudante.get_id():
				e = estudante
		
	########################
	
	# curso: adicionar
	def add_curso(self, curso):
		self.__lst_cursos.append(curso)
	
	# curso: pegar lista
	def get_cursos(self):
		return self.__lst_cursos
	
	# curso: buscar por Código
	def buscar_curso(self, cod):
		for c in self.__lst_cursos:
			if c.get_cod() == cod:
				return c
				
		return None
	
	# curso: editar
	def editar_curso(self, curso):
		for c in self.__lst_cursos:
			if c.get_cod() == curso.get_cod():
				c = curso
	
	########################
	
	# matrícula: adicionar
	def add_matricula(self, matricula):
		self.__lst_matriculas.append(matricula)
	
	# matrícula: pegar lista
	def get_matriculas(self):
		return self.__lst_matriculas
	
	# matrícula: buscar por Cód. de Curso e ID de Estudante
	def buscar_matricula(self, curso, estudante):
		for m in self.__lst_matriculas:
			if m.get_curso().get_cod() == curso.get_cod() and m.get_estudante().get_id() == estudante.get_id():
				return m
				
		return None
	
	# matrícula: listar por ID de Estudante
	def listar_estudante(self, id):
		lst_resultado = []
		
		for m in self.__lst_matriculas:
			if m.get_estudante().get_id() == id:
				lst_resultado.append(m)
				
		return lst_resultado
	
	# matrícula: listar por Cód de Curso
	def listar_curso(self, cod):
		lst_resultado = []
		
		for m in self.__lst_matriculas:
			if m.get_curso().get_cod() == cod:
				lst_resultado.append(m)
				
		return lst_resultado
	
	# matrícula: editar
	def editar_matricula(self, matricula):
		for m in self.__lst_matriculas:
			if m.get_curso().get_cod() == matricula.get_curso().get_cod() and m.get_estudante().get_id() == matricula.get_estudante().get_id():
				m = matricula