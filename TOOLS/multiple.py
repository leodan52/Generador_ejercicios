

def suma(a,b):

	aux = a + b

	if aux[0] == "+":
		return aux[1:]
	else:
		return aux

def producto(a,b):

	if a[0] == "+":
		a = a[1:]
	if b[0] == "+":
		b = b[1:]

	return "(" + a + ")(" + b + ")"

def division(a,b):

	if a[0] == "+":
		a = a[1:]
	if b[0] == "+":
		b = b[1:]


	return "\\frac{" + str(a*b) + "}{" + b + "}"

def potencia(a,b):

	if a[0] == "+":
		a = a[1:]
	elif a[0] == "-":
		a = "(" + a + ")"

	if b[0] == "+":
		b = b[1:]

	return a + "^{" + b + "}"

def raiz(a,b):

	if a[0] == "+":
		a = a[1:]
	if b[0] == "+" or b[0] = "-":
		b = b[1:]

	c = int(a)**int(b)

	return "\\sqrt[" + b + "]{" + str(c) + "}"


