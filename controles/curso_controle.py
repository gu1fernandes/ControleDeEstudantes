from utilitarios.banco_de_dados import BancoDeDados
from entidades.curso import Curso

class CursoControle:
	# menu cursos
	def menu(self):
		opcao = 1
		while opcao != 0:
			print('\n# CURSOS')
			print('1 - Adicionar')
			print('2 - Listar')
			print('3 - Buscar')
			print('4 - Editar')
			print('0 - Voltar')
			opcao = int(input('Opção: '))
			
			if opcao == 1:
				self.adicionar()
			elif opcao == 2:
				self.listar()
			elif opcao == 3:
				self.buscar()
			elif opcao == 4:
				self.editar()
	
	# adicionar novo curso
	def adicionar(self):
		print('\n# ADICIONAR CURSO')
		nome = input('Digite o nome: ')
		cod = int(input('Digite o código: '))
		carga = int(input('Digite a carga horária: '))
		
		novo_curso = Curso(nome, cod, carga)
		
		bd = BancoDeDados()
		bd.add_curso(novo_curso)
	
	# imprimir todos os cursos
	def listar(self):
		bd = BancoDeDados()
		lst_cursos = bd.get_cursos()
		
		print('\n# LISTAR TODOS OS CURSOS')
		if len(lst_cursos) > 0:
			for c in lst_cursos:
				print(c)
		else:
			print('Não há cursos.')
	
	# buscar curso
	def buscar(self, retornar = False):
		print('\n# BUSCAR CURSO')
		cod = int(input('Digite o código: '))
		
		bd = BancoDeDados()
		curso_encontrado = bd.buscar_curso(cod)
		
		if retornar:
			return curso_encontrado
		
		if curso_encontrado:
			print(curso_encontrado)
		else:
			print('Não encontrado!')
	
	# editar um curso
	def editar(self):
		print('\n# EDITAR CURSO')
		cod = int(input('Digite o código: '))
		
		bd = BancoDeDados()
		curso_encontrado = bd.buscar_curso(cod)
		
		if curso_encontrado:
			novo_nome = input('Digitar novo nome: ')
			nova_carga = input('Digitar nova carga horária: ')
			
			curso_encontrado.set_nome(novo_nome)
			curso_encontrado.set_carga(nova_carga)
			
			bd.editar_curso(curso_encontrado)
		else:
			print('Não encontrado!')