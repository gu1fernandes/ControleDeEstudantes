from utilitarios.banco_de_dados import BancoDeDados
from entidades.matricula import Matricula
from controles.curso_controle import CursoControle
from controles.estudante_controle import EstudanteControle

class MatriculaControle:
	# menu matrículas
	def menu(self):
		opcao = 1
		while opcao != 0:
			print('\n# MATRÍCULAS')
			print('1 - Adicionar')
			print('2 - Listar todas')
			print('3 - Listar por Estudante')
			print('4 - Listar por Curso')
			print('0 - Voltar')
			opcao = int(input('Opção: '))
			
			if opcao == 1:
				self.adicionar()
			elif opcao == 2:
				self.listar()
			elif opcao == 3:
				self.listar_estudante()
			elif opcao == 4:
				self.listar_curso()
			
	# adicionar nova matrícula
	def adicionar(self):
		print('\n# ADICIONAR MATRÍCULA')
		
		cc = CursoControle()
		curso = cc.buscar(True)
		
		if curso:
			print('Curso selecionado: ', curso.get_nome())
		else:
			print('Curso não encontrado!')
			return
		
		ec = EstudanteControle()
		estudante = ec.buscar(True)
	
		if estudante:
			print('Estudante selecionado: ', estudante.get_nome())
		else:
			print('Estudante não encontrado!')
			return
		
		data = input('\nDigite a data de início [aaaa-mm-dd]: ')
		
		matricula = Matricula(curso, estudante, data)
		
		bd = BancoDeDados()
		bd.add_matricula(matricula)
	
	# imprimir todas as matrículas
	def listar(self):
		bd = BancoDeDados()
		lst_matriculas = bd.get_matriculas()
		
		print('\n# LISTAR TODAS AS MATRÍCULAS')
		if len(lst_matriculas) > 0:
			for m in lst_matriculas:
				print(m)
		else:
			print('Não há matrículas.')
	
	# listar por Estudante
	def listar_estudante(self):
		print('\n# LISTAR POR ESTUDANTE')
		id = int(input('Digite o ID do Estudante: '))
		
		bd = BancoDeDados()
		lst_matriculas = bd.listar_estudante(id)
		
		print('\nMATRÍCULAS:')
		if len(lst_matriculas) > 0:
			for m in lst_matriculas:
				print(m)
		else:
			print('O estudante não possui matrículas.')
	
	# listar por Curso
	def listar_curso(self):
		print('\n# LISTAR POR CURSO')
		cod = int(input('Digite o Cód. do Curso: '))
		
		bd = BancoDeDados()
		lst_matriculas = bd.listar_curso(cod)
		
		print('\nMATRÍCULAS:')
		if len(lst_matriculas) > 0:
			for m in lst_matriculas:
				print(m)
		else:
			print('Não há matrículas nesse curso.')
	
	