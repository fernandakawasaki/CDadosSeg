# Trabalho prático 2 - Parte 2

## Entradas esperadas
**É necessário que o módulo pefile seja instalado (https://github.com/erocarrera/pefile)**

### Script ```sections.py``` - Extrair seções executáveis
Espera-se que o usuário forneça um diretório ou o nome de um arquivo. A chamada do script é feita da seguinte forma:

```python3 sections.py -d directory_name/``` ou ```python3 sections.py -directory direcotry_name/``` para diretórios

```python3 sections.py -f file.exe``` ou ```python3 sections.py -file file.exe``` para um arquivo

Pressupõe-se que o diretório só possui arquivos PE.

### Script ```compare.py``` - Obter seções únicas e a interseção destas
Para o bom funcionamento do script, é preciso que o usuário forneça dois arquivos PE (```.exe```).

Exemplo de uso: ```python3 compare.py file1.exe file2.exe```
