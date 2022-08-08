import os
import string
from PIL import Image, ImageFont, ImageDraw
from pathlib import Path


coord_pessoa = (143, 391)
coord_horas = (143, 656)
coord_setor = (525, 656)
coord_data_inicio = (600, 744)
coord_data_saida = (815, 744)

nome_pessoa = input('Insira o nome do membro: ')
#fazer o calculo automático da carga horária
carga_horaria = input('Insira a quantidade de horas totais do membro: ')

data_inicio = input("Insira a data de entrada do membro no formato dd/mm/aaaa: ")
data_saida = input("Insira a data de saída do membro no formato dd/mm/aaaa: ")

setor = input("Insira o cargo do membro: ")

script_location = Path(__file__).absolute().parent
file_location = script_location/'certificado.png'
print(script_location)

file_save_location = script_location/'output'/'{}.png'.format(nome_pessoa)

cwd = os.getcwd()
# print(os.path.join(cwd,  "arial-nova-bold.ttf"))
imagem = Image.open(file_location)
caminho_fonte = os.path.join(cwd,  "arial-nova.ttf")
caminho_fonte_bold = os.path.join(cwd,  "arial-nova-bold.ttf")
font = ImageFont.truetype(caminho_fonte, 36)
font_bold = ImageFont.truetype(caminho_fonte_bold, 36)
rgb_preto = (0,0,0)
desenho = ImageDraw.Draw(imagem)

desenho.text(coord_pessoa, "{name},".format(name = nome_pessoa),font=font_bold, fill=rgb_preto)
desenho.text(coord_horas, carga_horaria, font=font_bold, fill=rgb_preto)
desenho.text(coord_setor, setor, font=font, fill=rgb_preto)
# desenho.text(coord_data_inicio, "{0}  -  {1}".format(data_inicio, data_saida), font=font_bold, fill=rgb_preto)
desenho.text(coord_data_inicio, data_inicio, font=font_bold, fill=rgb_preto)
desenho.text(coord_data_saida, data_saida, font=font_bold, fill=rgb_preto)

imagem.save(file_save_location)
imagem.show()
