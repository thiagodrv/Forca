#!/usr/bin/env python2

import sys, string

file = 'wordlist.txt'
fd = open(file, 'r')

if __name__=='__main__':
    #wordlist = fd.read()
    palavra = sys.argv[1]
    comprimento = len(palavra)
    print palavra
    print comprimento
    #apenas retirar da wordlist palavras com o mesmo numero de letras
    lines = fd.readlines()
    for line in lines:
        line = line.replace('\n', '')
        compri_linha = len(line)
        hyphen = line.count('-')
        if hyphen != 0:
            compri_linha = compri_linha - hyphen
        if compri_linha == comprimento:
            #print 'entrou1'
            for i in range(comprimento):
                #print 'entrou2'
                if palavra[i] == '_':
                    #print 'entrou3'
                    pass
                if line[i] == palavra[i]:
                    #print 'entrou4'
                    print line
            
            #for i in palavra:
            #    if i != '_':
            #print line
