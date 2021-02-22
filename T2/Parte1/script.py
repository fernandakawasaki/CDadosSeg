import os
import xml.etree.ElementTree as ET
import argparse
import pandas as pd


def get_permissions(args):
    if args.directory.endswith('/'):
        directory = args.directory
    else:
        directory = args.directory + '/'

    totalpermissions = {}
    for filename in os.listdir(directory):
        filename_strip = '.'.join(filename.split('_')[1].split('.')[0:-1])
        tree = ET.parse(directory + filename)
        root = tree.getroot()
        apkpermission = []
        for child in root:
            if 'permission' in child.tag:
                for permission in child.attrib.values():
                    splt = permission.split('.')
                    if ('permission' in splt) and splt[-1].isupper():
                        apkpermission.append(splt[-1])
                    else:
                        print(permission)
        totalpermissions[filename_strip] = apkpermission
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
    permissionslst = [lst for lst in totalpermissions.values()]
    intersec = set.intersection(*map(set, permissionslst))
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
    permissionslst = []
    uniquepermissions = {}
    for lst in totalpermissions.values():
        permissionslst.extend(list(set(lst)))
    serie = pd.Series(permissionslst)
    duplicatedpermissions = list(serie[serie.duplicated()])

    for key, value in totalpermissions.items():
        uniquepermissions[key] = []
        for element in value:
            if element not in duplicatedpermissions:
                uniquepermissions[key].append(element)

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
parser.add_argument('-directory', '-d', required=True)
parser.add_argument('-unique', '-u', action='store_true')
parser.add_argument('-intersec', '-i', action='store_true')

args = parser.parse_args()

# Todas as permissoes
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