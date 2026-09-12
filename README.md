# 🌊 Missão: Aquário Digital Core

> **Garantir a qualidade da água do aquário digital, monitorando pH e temperatura em tempo real e assegurando um ecossistema seguro e saudável.**

---

## 🎯 Sobre o Projeto

O **Aquário Digital Core** é um sistema desenvolvido em **Python** que implementa a classe `ControleQualidadeAgua`. Ela é responsável por validar se os parâmetros ambientais (pH e temperatura) estão dentro das faixas ideais para manter um ecossistema aquático saudável.

🔗 **Repositório:** [https://github.com/isaqueguimaraes/aquario-digital-core](https://github.com/isaqueguimaraes/aquario-digital-core)

---

## 🧱 Camadas do Ambiente

O projeto adota uma estratégia de *deploy* em múltiplas camadas (*multi-layer environment*), garantindo que todas as alterações sejam rigorosamente testadas antes do envio para produção.

| Camada          | Descrição                                                                                                    | Estabilidade |
| :-------------- | :----------------------------------------------------------------------------------------------------------- | :----------: |
| 🧪 **`develop`** | Ambiente de desenvolvimento. Recebe commits frequentes, testes iniciais e *feature branches*.                |   🔴 Baixa    |
| 🧬 **`stage`**   | Ambiente de homologação (*staging*). O código validado em `develop` é promovido para testes rigorosos de QA. |   🟡 Média    |
| 🚀 **`main`**    | Ambiente de produção. Contém apenas código estável, auditado e liberado para uso.                            |    🟢 Alta    |

### 🔄 Fluxo de Promoção

```text
develop  ───►  stage  ───►  main
   │             │            │
   │             │            └── 🟢 ✅ Produção Estável
   │             └─────────────── 🟡 🧪 Homologação & QA
   └───────────────────────────── 🔴 💻 Desenvolvimento
✅ Parâmetros VerificadosParâmetroFaixa IdealMensagem de AlertapH6.8 – 7.6  ALERTA QA: Nível de pH fora do limite ideal!  Temperatura22.0 °C – 28.0 °C  ALERTA QA: Temperatura fora do limite seguro!  ⚙️ Estrutura do Código🧬 Classe ControleQualidadeAgua[cite: 3]MétodoParâmetrosRetornoDescrição__init__ph: float, temperatura: floatNoneConstrutor que inicializa a instância com os parâmetros do aquário[cite: 3].verificar_parametrosNenhumboolValida as métricas e exibe o status no console (True para OK, False para Alerta)[cite: 3].📁 Estrutura do RepositórioPlaintextaquario-digital-core/
├── 📄 .gitignore
├── 📄 LICENSE
├── 🐍 controle_qualidade_agua.py    # Módulo principal de monitoramento
└── 📘 README.md                     # Documentação completa do projeto
🚀 Como Executar📌 Pré-requisitosPython 3.6 ou superior instalado.💻 Passo a PassoClone o repositório:Bashgit clone [https://github.com/isaqueguimaraes/aquario-digital-core.git](https://github.com/isaqueguimaraes/aquario-digital-core.git)
Acesse a pasta do projeto:Bashcd aquario-digital-core
Execute o script:Bashpython controle_qualidade_agua.py
💡 Exemplo de UsoPythonfrom controle_qualidade_agua import ControleQualidadeAgua

# Criando instância do aquário
aquario = ControleQualidadeAgua(ph=7.2, temperatura=25.0)

# Executando a validação dos parâmetros
aquario.verificar_parametros()
🖥️ Saídas EsperadasParâmetros ideais:PlaintextSTATUS: Parâmetros da água em níveis ideais.
Parâmetros fora do limite:PlaintextALERTA QA: Nível de pH fora do limite ideal!
ouPlaintextALERTA QA: Temperatura fora do limite seguro!
👨‍💻 Responsável pelo ProjetoFotoNomeFunçãoGitHub🧑‍💻Isaque GuimarãesBiólogo / Desenvolvedor Responsável@isaqueguimaraes