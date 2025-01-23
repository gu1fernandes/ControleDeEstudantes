from utilitarios.banco_de_dados import BancoDeDados
from entidades.estudante import Estudante

class EstudanteControle:
	# menu estudantes
	def menu(self):
		opcao = 1
		while opcao != 0:
			print('\n# ESTUDANTES')
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
	
	# adicionar novo estudante	
	def adicionar(self):
		print('\n# ADICIONAR ESTUDANTE')
		nome = input('Digite o nome: ')
		nasc = input('Digite a data de nascimento [aaaa-mm-dd]: ')
		id = int(input('Digite o ID: '))
		
		novo_estudante = Estudante(nome, nasc, id)
		
		bd = BancoDeDados()
		bd.add_estudante(novo_estudante)
	
	# imprimir todos os estudantes
	def listar(self):
		bd = BancoDeDados()
		lst_estudantes = bd.get_estudantes()
		
		print('\n# LISTAR TODOS OS ESTUDANTES')
		if len(lst_estudantes) > 0:
			for e in lst_estudantes:
				print(e)
		else:
			print('Não há estudantes.')
	
	# buscar estudante
	def buscar(self, retornar = False):
		print('\n# BUSCAR ESTUDANTE')
		id = int(input('Digite o ID: '))
		
		bd = BancoDeDados()
		estudante_encontrado = bd.buscar_estudante(id)
		
		if retornar:
			return estudante_encontrado
		
		if estudante_encontrado:
			print(estudante_encontrado)
		else:
			print('Não encontrado!')
	
	# editar um estudante
	def editar(self):
		print('\n# EDITAR ESTUDANTE')
		id = int(input('Digite o ID: '))
		
		bd = BancoDeDados()
		estudante_encontrado = bd.buscar_estudante(id)
		
		if estudante_encontrado:
			novo_nome = input('Digitar novo nome: ')
			novo_nasc = input('Digitar nova data de nascimento [aaaa-mm-dd]: ')
			
			estudante_encontrado.set_nome(novo_nome)
			estudante_encontrado.set_nasc(novo_nasc)
			
			bd.editar_estudante(estudante_encontrado)
		else:
			print('Não encontrado!')