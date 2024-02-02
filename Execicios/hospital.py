planos = {'premium': 6, 'diamante': 5, 'ouro': 4, 'prata': 3, 'bronze': 2, 'resto': 1}

def compare_patients(patient1, patient2):
    if patient1[1] != patient2[1]:
        return patient1[1] < patient2[1]
    elif patient1[2] != patient2[2]:
        return patient1[2] > patient2[2]
    else:
        return patient1[0] < patient2[0]

N = int(input())

pacientes = []

for _ in range(N):
    nome, plano, gravidade = input().split()
    pacientes.append((nome, planos[plano], int(gravidade)))

pacientes.sort(key=lambda x: (-x[1], -x[2], x[0]))

for paciente in pacientes:
    print(paciente[0])
