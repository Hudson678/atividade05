#Crie um programa que receba três notas de um aluno e calcule a média aritmética.
n1 = float(input("primeira nota do aluno: "))
n2 = float(input("segunda nota do aluno: "))
n3 = float(input("terceira nota do aluno: "))

media = ((n1 + n2 + n3)/3)
media_r = round(media, 1)
print(f"a media total do aluno é {media_r}")

