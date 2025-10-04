turma = {'Ana', 'Bruno', 'Carlos', 'Daniel', 'Eduardo', 'Felipe'}
presentes = {'Ana', 'Bruno', 'Carlos', 'Daniel'}

#print(presentes.issubset(turma))  # Verifica se todos os presentes estão na turma
#print(turma.issuperset(presentes))  # Verifica se a turma contém todos os presentes

faltantes = turma.difference(presentes)
print(faltantes)  # Mostra quem está presente mas não está na turma
