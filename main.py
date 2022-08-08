import os
from PIL import Image, ImageFont, ImageDraw
from pathlib import Path
import pandas as pd

def format_date(date_str):
  splitted_data = date_str.split('/')
  formatted_date = splitted_data[2] + "-" + splitted_data[1] + "-" + splitted_data[0]
  return formatted_date

coord_pessoa = (143, 391)
coord_horas = (143, 656)
coord_setor = (525, 656)
coord_data_inicio = (600, 744)
coord_data_saida = (815, 744)

nome_pessoa = input('Insira o nome do membro: ')
carga_horaria_semanal = int(input('Insira a carga horária semanal: '))
data_inicio = input("Insira a data de entrada do membro no formato dd/mm/aaaa: ")
data_saida = input("Insira a data de saída do membro no formato dd/mm/aaaa: ")
setor = input("Insira o cargo do membro: ")

# Cálculo da carga horária
data_range = len(pd.bdate_range(format_date(data_inicio), format_date(data_saida)))
carga_horaria = str(int((data_range / 5) * carga_horaria_semanal))

script_location = Path(__file__).absolute().parent
file_location = script_location/'certificado.png'
print(script_location)

file_save_location = script_location/'output'/'{}.pdf'.format(nome_pessoa)

imagem_original = Image.open(file_location)
imagem = Image.new('RGB', imagem_original.size, (255, 255, 255))
imagem.paste(imagem_original, mask = imagem_original.split()[3])

caminho_fonte = os.path.join(os.getcwd(),  "arial-nova.ttf")
caminho_fonte_bold = os.path.join(os.getcwd(),  "arial-nova-bold.ttf")
font = ImageFont.truetype(caminho_fonte, 36)
font_bold = ImageFont.truetype(caminho_fonte_bold, 36)
rgb_preto = (0,0,0)
desenho = ImageDraw.Draw(imagem)

desenho.text(coord_pessoa, "{name},".format(name = nome_pessoa),font = font_bold, fill = rgb_preto)
desenho.text(coord_horas, carga_horaria, font = font_bold, fill = rgb_preto)
desenho.text(coord_setor, setor, font = font, fill = rgb_preto)
desenho.text(coord_data_inicio, data_inicio, font = font_bold, fill = rgb_preto)
desenho.text(coord_data_saida, data_saida, font = font_bold, fill = rgb_preto)

imagem.save(file_save_location, 'PDF', resolution = 100.0)
