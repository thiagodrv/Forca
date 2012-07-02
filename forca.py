#!/usr/bin/env python2

import sys

file = 'wordlist-preao-20120701.txt'
fd = open(file, 'r')
wordlist = fd.read()
#open(file, 'w')
#wordlist = fd.read()

if __name__=='__main__':
    palavra = sys.argv[1]
    comprimento = len(palavra)
    print palavra
    print comprimento
    print len(wordlist)
    #apenas retirar da wordlist palavras com o mesmo numero de letras
    for line in wordlist:
        print 'entrou'
        print 'linha: '+line
        if len(line) == comprimento:
            print line
