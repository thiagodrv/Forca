#!/usr/bin/env python2

import sys, string

file = 'wordlist.txt'
fd = open(file, 'r')

if __name__=='__main__':
    palavra = sys.argv[1]
    comprimento = len(palavra)
    lines = fd.readlines()
    for line in lines:
        line = line.replace('\n', '')
        compri_linha = len(line)
        #apenas retirar da wordlist palavras com o mesmo numero de letras
        if compri_linha == comprimento:
            for posicao in range(1,comprimento+1):
                i = posicao-1
                if palavra[i] == '_': #se letra for 'nao descoberta', passa.
                    if posicao == comprimento: #Se for a ultima letra, libera.
                        print line
                    pass
                elif line[i] == palavra[i]: #se a letra da palavra da wordlist for igual a informada, continua.
                    if posicao == comprimento: #Se for a ultima letra, libera.
                        print line
                else:
                    break
