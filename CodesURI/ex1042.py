def main():
 
  entrada = raw_input()
  a,b,c = entrada.split()
  a = int(a)
  b = int(b)
  c = int(c)
  
  n1 = 0
  n2 = 0
  n3 = 0
  
  if(a<b and a<c):
        n1 = a
        if(b<c):
           n2 = b
           n3 = c
        else:
           n2 = c
           n3 = b
  elif(b<a and b<c):
        n1 = b
        if(a<c):
            n2 = a
            n3 = c
        else:
            n2 = c
            n3 = a
  elif(c<a and c<b):
        n1 = c
        if(b<a):
            n2 = b
            n3 = a
        else:
            n2 = a
            n3 = b

  print str(n1)
  print str(n2)
  print str(n3)
  print 
  print str(a)
  print str(b)
  print str(c)



main()