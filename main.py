def somar(x,y):
  return x+y

def subtrair(x,y):
  return x-y

def multiplicar(x,y):
  return x*y

def dividir(x,y):
  return x/y

print("Escolha a Operação")
print("1) Somar")
print("2) Subtração")
print("3) Multiplicação")
print("4) Divisão")

escolha = input("Escolha a Operação")

n1=float(input("Digite um número"))
n2=float(input("Digite outro número: "))

if escolha == '1':
   print(somar(n1,n2))
if escolha == '2':
  print(subtrair(n1,n2))
if escolha == '3':
  print(multiplicar(n1,n2))  
if escolha == '4':
  print(dividir(n1,n2))