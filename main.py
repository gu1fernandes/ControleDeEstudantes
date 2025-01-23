from controles.estudante_controle import EstudanteControle
from controles.curso_controle import CursoControle
from controles.matricula_controle import MatriculaControle
from controles.nota_controle import NotaControle

if __name__ == '__main__':
	opcao = 1
	
	while opcao != 0:
		print('\n# GERENCIAMENTO DE ESTUDANTES')
		print('1 - Estudantes')
		print('2 - Cursos')
		print('3 - Matrículas')
		print('4 - Notas')
		print('0 - Sair')
		opcao = int(input('Digite uma opção: '))
		
		if opcao == 1:
			ec = EstudanteControle()
			ec.menu()
		elif opcao == 2:
			cc = CursoControle()
			cc.menu()
		elif opcao == 3:
			mc = MatriculaControle()
			mc.menu()
		elif opcao == 4:
			nc = NotaControle()
			nc.menu()