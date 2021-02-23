import pefile
import sys


def get_sections(filename, sections):
    sections[filename] = []

    pe = pefile.PE(filename)
    for section in pe.sections:
        permissions = 'r' if getattr(section, 'IMAGE_SCN_MEM_READ') else '-'
        permissions += 'w' if getattr(section, 'IMAGE_SCN_MEM_WRITE') else '-'
        permissions += 'x' if getattr(section, 'IMAGE_SCN_MEM_EXECUTE') else '-'
        sections[filename].append((section.Name.decode('utf-8').rstrip('\x00'), permissions)) # Remove o '\x000' do final das strings


def print_intersec(intersec):
    print()
    print('===================')
    print()
    print('Seções comuns dos PE')
    print()
    print('===================')
    print()
    print(intersec)


def print_unique(unique):
    print()
    print('===================')
    print()
    print('Seções únicas dos PE')
    print()
    print('===================')
    print()
    for element in unique:
        print(element + ':', unique[element])
        print()


def get_intersec(sections, file1, file2):
    # Obtem intersecoes dos PE
    intersec = []
    for tup in sections[file1]:
        if tup in sections[file2]:
            intersec.append(tup)
    print_intersec(intersec)
    return intersec


def get_unique(sections, intersec):
    # Obtem as secoes unicas de cada PE
    unique = {}
    for key in sections:
        unique[key] = []
        for element in sections[key]:
            if element not in intersec:
                unique[key].append(element)
    print_unique(unique)


# Lê arquivos
file1 = sys.argv[1]
file2 = sys.argv[2]

sections = {}

# Obtem secoes e imprime
get_sections(file1, sections)
get_sections(file2, sections)

# Obtem intersecoes e secoes unicas
intersec = get_intersec(sections, file1, file2)
get_unique(sections, intersec)