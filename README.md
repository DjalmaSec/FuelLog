# FuelLog - Sistema de Registro de Abastecimentos

![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-FF6C37?style=flat&logo=python&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=flat&logo=microsoft-excel&logoColor=white)

Sistema simples desenvolvido em Python com interface gráfica para **registrar abastecimentos de veículos** em uma planilha Excel. Ideal para controle de frota ou uso pessoal.

---

## Interface do Programa

<img width="357" alt="image" src="https://github.com/user-attachments/assets/7ce51439-ca62-4105-a924-bb5340292dc0" />

---

## 📋 Funcionalidades

| Campo | Descrição |
|-------|-----------|
| **Placa do Veículo** | Identificação do veículo |
| **Quantidade Abastecida** | Litros abastecidos |
| **Data** | Registra quando o abastecimento foi realizado |
| **Km** | Quilometragem atual do veículo |
| **Litros Restantes** | Combustível restante no tanque |
| **Situação Pedido** | Status (ex: concluído, pendente, autorizado) |

---

##  Como usar:

### 1. Instale as dependências

```bash
pip install pandas openpyxl

```


### Execute o programa
```bash
python cadastro_combustivel.py
```

### Preencha os dados:

Digite as informações nos campos da interface

Clique no botão "Enviar"

Os dados são salvos automaticamente na planilha Excel
---

### Exemplo da Planilha Gerada

| Data       | Placa     | Quantidade (L) | Km     | Litros Restantes | Situação  |
|------------|-----------|----------------|--------|-------------------|-----------|
| 01/03/2026 | ABC-1234  | 45.5           | 12500  | 12.0              | Concluído |
| 02/03/2026 | XYZ-5678  | 38.0           | 25800  | 8.5               | Pendente  |
| 04/03/2026 | GHI-3456  | 41.7           | 18700  | 6.8               | Concluído |


---
### Requisitos
Python 3.x

Bibliotecas: pandas, openpyxl (instaladas via pip)
