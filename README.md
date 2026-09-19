# 🐠 Aquário Digital Core — Controle de Qualidade da Água

> Sistema de monitoramento e controle de parâmetros aquáticos para aquários, desenvolvido em Python.

[![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)](https://www.python.org/)
[![Status](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)]()
[![Repositório](https://img.shields.io/badge/GitHub-aquario--digital--core-181717?logo=github)](https://github.com/isaqueguimaraes/aquario-digital-core)

---

## 📋 Descrição

O **Aquário Digital Core** é o núcleo do sistema de controle de qualidade da água para aquários. Ele verifica se os parâmetros físico-químicos da água — pH e temperatura — estão dentro dos limites ideais para a saúde dos organismos aquáticos, emitindo alertas automáticos quando algum valor se encontra fora da faixa segura.

---

## 🚀 Funcionalidades

- ✅ Verificação do nível de **pH** (faixa ideal: 6,8 – 7,6)
- ✅ Verificação da **temperatura** da água (faixa segura: 22,0 °C – 28,0 °C)
- ✅ Emissão de **alertas de QA** em caso de parâmetros fora dos limites
- ✅ Confirmação de status quando os parâmetros estão em níveis ideais

---

## 🧪 Exemplo de uso

```python
from controle_qualidade_agua import ControleQualidadeAgua

aquario = ControleQualidadeAgua(ph=7.2, temperatura=25.0)
aquario.verificar_parametros()
# STATUS: Parâmetros da água em níveis ideais.
```

### Saídas possíveis

| Situação | Saída no terminal |
|---|---|
| pH fora do intervalo 6,8–7,6 | `ALERTA QA: Nível de pH fora do limite ideal!` |
| Temperatura fora do intervalo 22,0–28,0 °C | `ALERTA QA: Temperatura fora do limite seguro!` |
| Todos os parâmetros dentro do limite | `STATUS: Parâmetros da água em níveis ideais.` |

---

## 🌿 Camadas do Ambiente

Este projeto segue um fluxo de branches estruturado em três camadas:

| Branch | Finalidade |
|---|---|
| `develop` | Ambiente de desenvolvimento ativo. Novas funcionalidades e experimentos são implementados aqui antes de qualquer validação. |
| `stage` | Ambiente de homologação. Código promovido do `develop` e submetido a testes de integração e validação biológica/técnica. |
| `main` | Ambiente de produção. Contém apenas versões estáveis, revisadas e aprovadas do sistema. |

> **Fluxo:** `develop` → `stage` → `main`

---

## 🗂️ Estrutura do Projeto

```
aquario-digital-core/
│
├── controle_qualidade_agua.py   # Módulo principal de controle de qualidade
└── README.md                    # Documentação do projeto
```

---

## ⚙️ Como executar

**Pré-requisitos:** Python 3.x instalado.

```bash
# Clone o repositório
git clone https://github.com/isaqueguimaraes/aquario-digital-core.git

# Acesse o diretório
cd aquario-digital-core

# Execute o módulo principal
python controle_qualidade_agua.py
```

## 👨‍🔬 Responsável
**Isaque Guimarães**
