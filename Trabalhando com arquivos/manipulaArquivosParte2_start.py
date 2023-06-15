#
# Exemplos de como trabalhar com arquivos
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def criaZipModol():
  shutil.make_archive("ArquivoCompactado", "zip", "C:\\Users\\Grupo.L2R\\Desktop\\aulas\\LinkedIn\\Python\\Trabalhando com arquivos")
  
#criaZipModol()

def CriaZipModo2():
  with ZipFile("ArquivoZipModo2.zip", "w") as novoZip:
    novoZip.write("NovoArquivo.bkp")
    novoZip.write("NovoArquivo.txt")
    novoZip.write("ZipModo1.zip.zip")
    
  #CriaZipModo2()
  
  def DeletaArquivo():
    os.remove("ArquivoZipModo2.zip")
  
  DeletaArquivo()