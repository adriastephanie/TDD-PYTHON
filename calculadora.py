def horaextra(salario):
    return salario /220

def calcularaumento(salario, porcentagem):
    return (salario * porcentagem) / 100.00

def calcularferias(salario, mesestrab):
    return salario / 12 * mesestrab

def calculardecimo(salario, mesestrab):
    return (salario / 12) * mesestrab + salario / 3.00