import os
from PIL import Image, ImageFont, ImageDraw
from pathlib import Path


coord_pessoa = (147,384)
coord_horas = (148,656)
coord_setor = (527,654)
coord_data_inicio = (610,741)
coord_data_saida = (827,741)

nome_pessoa = input('Insira o nome do membro: ')
#fazer o calculo automático da carga horária
carga_horaria = input('Insira a quantidade de horas totais do membro: ')

data_inicio = input("Insira a data de entrada do membro no formato dd/mm/aaaa: ")
data_saida = input("Insira a data de saída do membro no formato dd/mm/aaaa: ")

setor = input("Insira o cargo do membro: ")

script_location = Path(__file__).absolute().parent
file_location = script_location/'certificado.png'

file_save_location = script_location/'output'/'{}.png'.format(nome_pessoa)

imagem = Image.open(file_location)
caminho_fonte = r"C:\Windows\Fonts\ARIALN.TTF"
font = ImageFont.truetype(caminho_fonte,40)
rgb_preto = (0,0,0)
desenho = ImageDraw.Draw(imagem)

desenho.text(coord_pessoa,nome_pessoa,font=font,fill=rgb_preto,stroke_width=1)
desenho.text(coord_horas,carga_horaria,font=font,fill=rgb_preto,stroke_width=1)
desenho.text(coord_setor,setor,font=font,fill=rgb_preto)
desenho.text(coord_data_inicio,data_inicio,font=font,fill=rgb_preto,stroke_width=1)
desenho.text(coord_data_saida,data_saida,font=font,fill=rgb_preto,stroke_width=1)

imagem.save(file_save_location)
imagem.show()
