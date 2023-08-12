# Escrever funcao que calcule a media de # notas usando funcoes, indentacao e bloco

nota1, nota2, nota3 = float(input()), float(input()), float(input())
peso1, peso2, peso3 = float(input()), float(input()), float(input())

def calcula_media(nota1, nota2, nota3, peso1, peso2, peso3):
    media = (nota1*peso1 + nota2*peso2 + nota3*peso3)/(peso1+peso2+peso)
    return media
print(calcula_media(nota1, nota2, nota3, peso1, peso2, peso3), "fim do programa")

# a definicao da funcao precisa sempre de def e do return. a funcao precisa sempre estar independente e a gente precisa tirar as infos dela. 