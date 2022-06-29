num = int(input('Digite un numero: '))
 
if num >= 0:
  absoluto = num
  print('El valor absoluto de %d es %d' %(num,absoluto))
else:
  absoluto = num * -1
  print('El valor absoluto de %d es %d' %(num,absoluto))
