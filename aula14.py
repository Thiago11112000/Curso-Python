a = 'AAAAA'
b = 'B'
c = 1.1
string = 'a={nome2} b={nome1} c= {nome1} {nome3:.2f}'
formato =  string.format(
   nome1= a,nome2=b, nome3=c)

print(formato)