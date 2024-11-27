"""
Encontrar alunos que cursam apenas uma disciplina dado as disciplinas:
    -matematica com os nomes dos alunos que fazem Matemática
    -fisica com os nomes dos alunos que fazem Física
"""
matematica = {'Sara', 'Daniel', 'Pedro', 'Laura', 'Lucas', 'Everson'}
fisica = {'Sara', 'Daniel', 'Roberto', 'Pedro', 'Samuel', 'Laura'}

filtro = matematica ^ fisica

print('Alunos que cursam apenas uma matéria:', end=' ')
for pessoa in filtro:
    print(f'{pessoa}', end=' ')
print()
