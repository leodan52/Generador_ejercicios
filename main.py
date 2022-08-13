# Genera ejercicios de sumas

from random import randint,shuffle

def main():

	sumasfile = "./LaTeX/sumas.tex"
	productfile = "./LaTeX/producto.tex"
	divfile = "./LaTeX/div.tex"
	potfile = "./LaTeX/potencia.tex"

	operaciones = ("suma", "producto", "división", "potencia")
	archivos = (sumasfile, productfile, divfile, potfile)

	for i in range(len(operaciones)):
		generador(operaciones[i], archivos[i], "no")



#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

def generador(ope,archivo, expneg="yes"):

	if exist(archivo):
	# Si el archivo ya fue generado, se evita crearlo nuevamente
	# Si se desea crear otro, debe renombrar el anterior o borrarlo
		print()
		print("El archivo", archivo, "ya existe.")
		print("Si desea generar otro, cambien el nombre del ya existente")
		print("Si desea reemplazarlo, bórrelo")
		print()
		return
	else:
		peticion = "Cuántos ejercicios de " + ope + " desea que se generen>> "
		total = eval(input(peticion)) # Número de ejercicios a crear

		salida = open(archivo, "w")

		if ope == "potencia":

			lista = dist(total)

			for i in lista:
				print("\\item $" + notaPot(i,expneg) + "$", file=salida)

			salida.close()
			return

		rang = 100
		rango = rangodinamico(rang)

		n = len(rango)
		m = total // n

		for i in range(n):

			if i == len(rango) - 1:
				j += abs(total - n*m)

			sup = rango[i]
			if i == 0:
				inf = 2
			else:
				inf = rango[i-1]

			for j in range(m):
				# Operaciones
				# a realizar
				salidaop = operacion(ope,inf,sup)

				print("\\item " + "$" + salidaop + "$", file=salida)

		salida.close()

#------------------------------------------------------------------------
#------------------------------------------------------------------------

def operacion(ope,inf,sup):

	if ope == "suma":
		salida = suma(sup)
	elif ope == "producto":
		salida = producto(inf,sup)
	elif ope == "división":
		salida = division(inf,sup)

	return salida

#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

def rangodinamico(maximo):
	# Máximo dinámico para el rango de los número generados
	rango = [maximo]

	while maximo >= 20:
		maximo = maximo // 2
		rango.append(maximo)

	rango = list(reversed(rango))

	return rango

#------------------------------------------------------------------------
#------------------------------------------------------------------------

def suma(rango):
	n,m = 0,0
	while n == 0 or m == 0:
		n = randint(-rango, rango)
		m = randint(-rango, rango)

	return lineasuma(m,n)


#------------------------------------------------------------------------
#------------------------------------------------------------------------

def producto(rangoinf, rangosup):
	N, M = 0,0
	while N == 0 or M == 0 or N == 1 or M == 1:
		M = randint(rangoinf, rangosup )
		N = randint(rangoinf, rangosup )

	M = signoP(M)
	N = signoP(N)

	return notaPr(M,N)

#------------------------------------------------------------------------
#------------------------------------------------------------------------

def division(rangoinf, rangosup):
	N, M = 0,0
	while N == 0 or M == 0 or N == 1 or M == 1:
		M = randint(2, rangosup )
		N = randint(rangoinf, rangosup)

		if N % M != 0:
			N, M = 0,0

	M = signoP(M)
	N = signoP(N)

	return notaDiv(N,M)

#------------------------------------------------------------------------
#------------------------------------------------------------------------


def notaPot(num, neg="yes"):

	rango = 15

	prime = [2,3,5,7,11,13,17,19,23,29,31,37]
	np = len(prime)

	b = prime[randint(0,np-1)]

	m,n = 0,0
	while m == 0 or n == 0:
		m = randint(0, rango)
		n = randint(0, rango)
		if num == 3 or num == 4:
			if n == 1 or m == 1:
				n,m = 0,0
			elif m == 0 and n != 0:
					break
			elif n != 0:
				if m % n != 0 and num == 4:
					n,m = 0,0


	salida = ""

	if num == 1 or num == 2:
		if m != 1:
			fact1 = str(b)+ "^{" + str(m) + "}"
		else:
			fact1 = str(b)

		if n != 1:
			fact2 = str(b)+ "^{" + str(n) + "}"
		else:
			fact2 = str(b)
		if num == 1:
			return notaPr(fact1,fact2)
		else:
			if neg == "no":
				if max(m,n) == m:
					return notaDiv(fact1,fact2)
				else:
					return notaDiv(fact2,fact1)
			else:
				return notaDiv(fact1,fact2)
	elif num == 3:
		return "\\left( " + str(b) + "^{" + str(m) + "}\\right)^{" + str(n) + "}="

	elif num == 4:
		if n == 2:
			return "\\sqrt{" + str(b) + "^{" + str(m) + "}}="
		else:
			return "\\sqrt[" + str(abs(n)) + "]{" + str(b) + "^{" + str(m) + "}}="


def dist(m):

	n = int(round(m/4))

	lista = []

	for i in [1,2,3,4]:
		for j in range(n):
			lista.append(i)

	shuffle(lista)

	return lista


def notaDiv(n1, n2):

	# /, entre, frac

	rand = randint(1, 3)

	if rand == 1:
		return n1 + "/" + n2 + "="
	elif rand == 2:
		return n1 + "\\div " + n2 + "="
	elif rand == 3:
		return "\\frac{" + n1 + "}{" + n2 + "}="

def notaPr(num1,num2):

	# ()(), (), *, punto

	n = 4

	if num1[0] == "-" or num2[0] == "-":
		n = 2

	rand = randint(1,n)

	if rand == 1:
		return "(" + num1 + ")(" + num2 + ")" + "="
	elif rand == 2:
		return num1 + "(" + num2 + ")" + "="
	elif rand == 3:
		return num1 + "*" + num2 + "="
	elif rand == 4:
		return num1 + "\\cdot " + num2 + "="

def signoP(num):

	signo = randint(0,1)

	if signo == 0:
		return "-" + str(num)
	else:
		return str(num)

def signo(m):

	if m > 0:
		aux = "+" + str(m)
	else:
		aux = str(m)

	return aux

def lineasuma(m,n):

	linea = signo(m) + signo(n) + "="

	if linea[0] == "+":
		linea = " " + linea[1:]

	return linea

def exist(archivo):
	try:
		salida = open(archivo, "r")
		return True
	except FileNotFoundError:
		return False

if __name__ == "__main__":
	main()
