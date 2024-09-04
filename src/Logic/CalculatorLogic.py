from Test import Test_Error
from src.Logic import Parameters


def verificarEdad(edad):
    if edad < 18 or edad > 115:
        raise Test_Error.EdadError(f"Su edad, la cual es: {edad}, debe ser mayor a 18 y menor a 115")


def verificarSalarioActual(salario_actual):
    if salario_actual < 0:
        raise Test_Error.SalarioActualNegativoError(f"Su salario, el cual es: {salario_actual}, debe ser mayor a 0")


def verificarSemanasLaboradas(semanas_laboradas):
    if semanas_laboradas < 0:
        raise Test_Error.SemanasLaboradasNegativasError(
            f"Las semanas laboradas, las cuales son: {semanas_laboradas}, deben ser mayores a 0")


def verificarTasaAdministracion(tasa_administracion):
    if tasa_administracion < 0 or tasa_administracion > 3:
        raise Test_Error.TasaAdministracionError(
            f"La tasa de administración, la cual es: {tasa_administracion}, debe ser mayor a 0 y menor a 3")


def verificarAhorroPensional(ahorro_pensional_a_hoy):
    if ahorro_pensional_a_hoy < 0:
        raise Test_Error.AhorroPensionalNegativoError(
            f"El ahorro pensional a hoy, el cual es: {ahorro_pensional_a_hoy}, debe ser mayor a 0")


def verificarRentabilidadPromedio(rentabilidad_promedio):
    if rentabilidad_promedio < 0:  # Revisar este caso
        raise Test_Error.RentabilidadPromedioNegativaError(
            f"La rentabilidad promedio, la cual es: {rentabilidad_promedio}, debe ser mayor que 0")


def verificarEdadPension(edad_pension, sexo):
    edad_minima = 62 if sexo == 'M' else 57
    if edad_pension < edad_minima:
        raise Test_Error.EdadPensionError(
            f"La edad para pensionarse debe ser mayor o igual a {edad_minima} años para su sexo.")


def calcularAhorroPensionalEsperado(parametros):

    VerificarAhorroPensional(parametros.ahorro_pensional_a_hoy)
    VerificarEdad(parametros.edad)
    VerificarSalarioActual(parametros.salario_actual)
    VerificarTasaAdministracion(parametros.tasa_administracion)
    VerificarSemanasLaboradas(parametros.semanas_laboradas)

    # Calcular el tiempo restante hasta la edad de retiro
    edad_retiro = 62 if parametros.sexo == 'M' else 57
    años_restantes = edad_retiro - parametros.edad

    # Asegurarse de que los años restantes sean positivos
    if años_restantes <= 0:
        raise ValueError("La edad actual ya supera o iguala la edad de retiro")

    semanas_restantes = años_restantes * 52

    # Cálculo del ahorro pensional esperado
    ahorro_pensional_esperado = (
            parametros.ahorro_pensional_a_hoy * (1 + parametros.rentabilidad_promedio) ** años_restantes +
            parametros.salario_actual * semanas_restantes * (1 + parametros.rentabilidad_promedio) ** (
                        años_restantes - 1) / 52
    )

    return ahorro_pensional_esperado


def calcularPensionEsperada(ahorro_pensional_esperado, sexo):
    # La expectativa de vida promedio es de 80 años

    if sexo == 'M':
        años_esperados_de_vida = 80 - 62
    else:
        años_esperados_de_vida = 80 - 57

    # Cálculo de la pensión esperada mensual
    pension_esperada_mensual = ahorro_pensional_esperado / (años_esperados_de_vida * 12)

    return pension_esperada_mensual
