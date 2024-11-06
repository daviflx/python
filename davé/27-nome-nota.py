##Aréa inicial
alunos = []
notas = []
print("Este é o seu sistema de notas, nós usamos ele para mostrar a nota de 5 alunos por vez.")
print("Digite o nome dos 5 alunos abaixo.")
for i in range(5):
    aluno = input("Digite o nome do aluno: ")
    nota = int(input("Digite a nota do aluno: "))
    alunos.append(aluno)
    notas.append(nota)

for i in range(5):
    print(f"O aluno {aluno[i]} tirou nota {nota[i]}")