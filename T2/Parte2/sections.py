import pefile
import argparse
import os

def print_sections(sections):
    print()
    print('===================')
    print()
    print('Seções executáveis dos PE')
    print()
    print('===================')
    print()
    for element in sections:
        print(element + ':', sections[element])


def get_sections(filename, sections, directory=None):
    sections[filename] = []
    if directory:
        pe = pefile.PE(directory + filename)
    else:
        pe = pefile.PE(filename)
    for section in pe.sections:
        if getattr(section, 'IMAGE_SCN_MEM_EXECUTE'):
            sections[filename].append(section.Name.decode('utf-8').rstrip('\x00'))


# Parser - opcao de linha de comando
parser = argparse.ArgumentParser(description='Ler opções de entrada')
parser.add_argument('-directory', '-d') # Recebe nome do diretorio
parser.add_argument('-file', '-f') # Recebe nome do arquivo
args = parser.parse_args()

sections = {}

if args.directory:
    if args.directory.endswith('/'):
        directory = args.directory
    else:
        directory = args.directory + '/'
    for  filename in os.listdir(directory):
        get_sections(filename, sections, directory)
    print_sections(sections)
elif args.file:
    get_sections(args.file, sections)
    print_sections(sections)
else:
    raise ValueError('Arquivo/Diretório não fornecido')