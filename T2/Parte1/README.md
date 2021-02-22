# Trabalho prático 2 - Parte 1

## Entradas esperadas
É esperado que o usuário forneça o nome do diretório (obrigatório) onde estão os manifestos. Para isso, junto com a chamada do ```script.py```, o usuário deve adicionar a opção ```-directory``` ou ```-d``` e o nome do diretório. O script retornará as permissões por APK. **Exemplo de chamada:**
```python3 script.py -d manifests```

Caso queira a lista de permissões únicas ou a interseção das mesmas, o usuário deve adicionar as opções ```-u```/```-unique``` e ```-i```/```-intersec```, respectivamente. **Exemplo de uso:**
```python3 script.py -d manifests -i -u```
