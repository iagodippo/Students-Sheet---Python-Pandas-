import pandas as pd


# open the sheet
# verify all the students means
# if the mean is less than 7 and greater than 5, write "Exame Final" in the "Situação" column
# if the mean is less than 5 write "Reprovado por nota" and if it is greater than 7, write "Aprovado"
# calculate the mean of the students and put in the column "Nota para Aprovação Final" how much they will need to make in the final exam through the formula (mean - 100)
# check if any student failed for absense (>15) and write "Reprovado por falta" in the "Situação" column

tabela_alunos = pd.read_excel("students sheet.xlsx")

tabela_naf = tabela_alunos['Nota para Aprovação Final']

for media in tabela_alunos.index:

    if (tabela_alunos.P1[media] + tabela_alunos.P2[media] + tabela_alunos.P3[media])/3 >= 70:
        tabela_alunos.Situação[media] = 'Aprovado'

    elif 50 <= (tabela_alunos.P1[media] + tabela_alunos.P2[media] + tabela_alunos.P3[media])/3 < 70:
        tabela_alunos.Situação[media] = 'Exame Final'

    elif (tabela_alunos.P1[media] + tabela_alunos.P2[media] + tabela_alunos.P3[media])/3 < 50:
        tabela_alunos.Situação[media] = 'Reprovado por nota'


for faltas in tabela_alunos.index:

    if tabela_alunos.Faltas[faltas] > 15:
        tabela_alunos.Situação[faltas] = 'Reprovado por falta'


for naf in tabela_alunos.index:

    if tabela_alunos.Situação[naf] == 'Exame Final':
        tabela_naf[naf] = 100 - ((tabela_alunos.P1[naf] + tabela_alunos.P2[naf] + tabela_alunos.P3[naf])/3)
        tabela_naf[naf] = round(tabela_naf[naf] + 0.5)

print(tabela_alunos)

tabela_alunos.to_excel('students sheet.xlsx', sheet_name='students', index=False)







