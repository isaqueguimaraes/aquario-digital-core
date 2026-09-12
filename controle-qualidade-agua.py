class ControleQualidadeAgua:
  def __init__(self, ph: float, temperatura: float):
    self.ph = ph
    self.temperatura = temperatura

  def verificar_parametros(self) -> bool:
    if self.ph < 6.8 or self.ph > 7.6:
      print ("ALERTA QA: Nível de pH fora do limite ideal!")
      return False

    if self.temperatura < 22.0 or self.temperatura > 28.0:
      print ("ALERTA QA: Temperatura fora do limite seguro!")
      return False

    print ("STATUS: Parâmetros da água em níveis ideais.")
    return True

if __name__ == "__main__":
    aquario_teste = ControleQualidadeAgua (ph = 7.2, temperatura = 25.0)
    aquario_teste.verificar_parametros()