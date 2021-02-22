import os
import xml.etree.ElementTree as ET
import argparse
import pandas as pd


def get_permissions(args):
    # Normaliza nome do diretorio
    if args.directory.endswith('/'):
        directory = args.directory
    else:
        directory = args.directory + '/'

    totalpermissions = {}
    for filename in os.listdir(directory):
        filename_strip = '.'.join(filename.split('_')[1].split('.')[0:-1]) # Obtem o nome da apk
        tree = ET.parse(directory + filename)
        root = tree.getroot()
        apkpermission = []
        for child in root:
            if 'permission' in child.tag: # Seleciona tags com permission
                for permission in child.attrib.values():
                    splt = permission.split('.')
                    if ('permission' in splt) and splt[-1].isupper(): # Seleciona atributos com permission
                        apkpermission.append(splt[-1]) # Adiciona elemento a lista
        totalpermissions[filename_strip] = apkpermission # Adiciona lista ao dicionario
    return totalpermissions


def print_dictionary(dictionary):
    for key, value in dictionary.items():
        print(key + ':', value)
        print()


def print_permissions(totalpermissions):
    print()
    print('===================')
    print()
    print('Permissões por APK')
    print()
    print('===================')
    print()
    print_dictionary(totalpermissions)


def get_intesection(totalpermissions):
    permissionslst = [lst for lst in totalpermissions.values()] # Junta todas as listas dentro de uma so lista
    intersec = set.intersection(*map(set, permissionslst)) # Faz intersecao entre cada lista
    return list(intersec)


def print_intersection(intersec):
    print()
    print('===================')
    print()
    print('Permissões comuns das APKs')
    print()
    print('===================')
    print()
    print(intersec)


def get_unique(totalpermissions):
    # Obtem as permissoes repetidas
    permissionslst = []
    uniquepermissions = {}
    for lst in totalpermissions.values():
        permissionslst.extend(list(set(lst))) # Transforma as listas em set (para remover permissoes duplicadas) e junta tudo em uma lista
    serie = pd.Series(permissionslst)
    duplicatedpermissions = list(serie[serie.duplicated()]) # Obtem lista das permissoes que se repetiram

    for key, value in totalpermissions.items():
        uniquepermissions[key] = []
        for element in value:
            if element not in duplicatedpermissions: # Confere se a permissao nao eh repetida
                uniquepermissions[key].append(element) # Adiciona ao dicionario de permissoes unicas

    return uniquepermissions


def print_unique(uniquepermissions):
    print()
    print('===================')
    print()
    print('Permissões únicas por APK')
    print()
    print('===================')
    print()
    print_dictionary(uniquepermissions)


# Parser - opcao de linha de comando
parser = argparse.ArgumentParser(description='Ler opções de entrada')
parser.add_argument('-directory', '-d', required=True) # Recebe nome do diretorio
parser.add_argument('-unique', '-u', action='store_true')
parser.add_argument('-intersec', '-i', action='store_true')

args = parser.parse_args()

# Obtem todas as permissoes e imprime
totalpermissions = get_permissions(args)
print_permissions(totalpermissions)

# Obtem as permissoes repetidas em todas as apks
if args.intersec:
    intersec = get_intesection(totalpermissions)
    print_intersection(intersec)

# Obtem as permissoes unicas de cada aplicacao
if args.unique:
    uniquepermissions = get_unique(totalpermissions)
    print_unique(uniquepermissions)