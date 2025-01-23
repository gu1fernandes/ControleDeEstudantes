from utilitarios.banco_de_dados import BancoDeDados
from controles.curso_controle import CursoControle
from controles.estudante_controle import EstudanteControle
from controles.matricula_controle import MatriculaControle

class NotaControle:
	# menu notas
	def menu(self):
		opcao = 1
		while opcao != 0:
			print('\n# NOTAS')
			print('1 - Adicionar')
			print('2 - Listar por matrícula')
			print('3 - Editar')
			print('0 - Voltar')
			opcao = int(input('Opção: '))
			
			if opcao == 1:
				self.adicionar()
			elif opcao == 2:
				self.listar_matricula()
			elif opcao == 3:
				self.editar()
	
	# adicionar nota
	def adicionar(self):
		print('\n# ADICIONAR NOTA')
		
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
		
		bd = BancoDeDados()
		matricula = bd.buscar_matricula(curso, estudante)
		
		if not matricula:
			print('Matrícula não encontrada!')
			return
		
		nota = float(input('\nDigite a nota: '))
		matricula.add_nota(nota)
		
		bd.editar_matricula(matricula)
	
	# listar notas por matrícula
	def listar_matricula(self):
		print('\n# LISTAR NOTAS DE ESTUDANTE')
		
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
		
		bd = BancoDeDados()
		matricula = bd.buscar_matricula(curso, estudante)
		
		if not matricula:
			print('Matrícula não encontrada!')
			return
		
		lst_notas = matricula.get_notas()
		
		print('\nRELATÓRIO:')
		
		if len(lst_notas) == 0:
			print('Não há notas!')
			return
	
		print('Notas: ', lst_notas)
		print('Média: ', round(sum(lst_notas) / len(lst_notas), 1))