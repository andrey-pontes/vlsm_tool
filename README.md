# VLSM Subnet Calculator

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

Um processo automatizado para calcular e alocar sub-redes de tamanho variável (VLSM) a partir de uma rede principal. A solução é precisa, escalável e segue os princípios de design orientado a objetos (OOD) para máxima organização e manutenibilidade.

---

## Visão Geral

Este projeto foi criado para resolver um desafio comum de administração de redes: segmentar uma rede principal em múltiplas sub-redes para diferentes departamentos, cada um com um número específico de hosts.

Em vez de uma abordagem manual, propensa a erros e demorada, esta solução automatiza todo o processo de cálculo de VLSM.

### O Desafio Original

* **Rede Principal:** `192.168.10.0/24`
* **Requisitos:**
    * Administração: 50 hosts
    * Financeiro: 30 hosts
    * Suporte: 14 hosts
    * TI: 6 hosts

A ferramenta calcula o plano de alocação de rede ideal, garantindo zero desperdício de IP entre os blocos alocados.

## Features

* ** Precisão Absoluta:** Utiliza a biblioteca padrão `ipaddress` do Python para gerenciar toda a aritmética binária e lógica de rede, eliminando 100% dos erros de cálculo manual.
* ** Eficiência:** Gera um plano de rede completo em milissegundos.
* ** Arquitetura Modular (OOD):** O código é organizado seguindo o **Princípio da Responsabilidade Única (SRP)**, separando a lógica de alocação (`allocator.py`), as estruturas de dados (`models.py`) e a apresentação (`display.py`).
* ** Escalabilidade Fácil:** Adicionar novos departamentos ou alterar os requisitos de hosts é tão simples quanto modificar um dicionário no script principal.

## Estrutura do Projeto

O projeto é organizado como um pacote Python (`vlsm_tool`) e um script de entrada (`main.py`), o que promove um código limpo e desacoplado.

```bash
projeto_vlsm/
├── main.py                 # Ponto de entrada
├── vlsm_tool/              # O pacote com toda a lógica
│   ├── __init__.py         # Inicializador do pacote
│   ├── allocator.py        # Classe VlsmAllocator
│   ├── models.py           # Dataclass SubnetAllocation 
│   └── display.py          # Função display_allocation_table
└── README.md
```

##  Pré-requisitos

* Python 3.8 ou superior.

Nenhuma biblioteca externa é necessária. O projeto utiliza apenas módulos da biblioteca padrão do Python (`ipaddress`, `dataclasses`, etc.).

## Como Usar

1.  Clone este repositório:
    ```bash
    git clone https://github.com/andrey-pontes/vlsm_tool.git
    ```

2.  Navegue até o diretório do projeto:
    ```bash
    cd vlsm_tool
    ```

3.  (Opcional) Para configurar seus próprios requisitos, edite o arquivo `main.py` e altere as variáveis `main_network_cidr` e `department_requirements`:

    ```python
    # main.py

    # 1. Defina sua rede principal
    main_network_cidr = "192.168.10.0/24"
    
    # 2. Defina os requisitos
    department_requirements = {
        "Administracao": 50,
        "Financeiro": 30,
        "Suporte": 14,
        "TI": 6
    }
    ```

4.  Execute o script principal:
    ```bash
    python main.py
    ```

## Exemplo de Saída

Ao executar o script com a configuração padrão, a saída será a seguinte tabela, mostrando o plano de alocação completo:


| Departamento   | Hosts | Rede_ID         | Máscara              | Faixa_Util                         | Broadcast        |
|----------------|--------|-----------------|----------------------|------------------------------------|------------------|
| Administração  | 50     | 192.168.10.0    | /26 (255.255.255.192) | 192.168.10.1 - 192.168.10.62      | 192.168.10.63    |
| Financeiro     | 30     | 192.168.10.64   | /27 (255.255.255.224) | 192.168.10.65 - 192.168.10.94     | 192.168.10.95    |
| Suporte        | 14     | 192.168.10.96   | /28 (255.255.255.240) | 192.168.10.97 - 192.168.10.110    | 192.168.10.111   |
| TI             | 6      | 192.168.10.112  | /29 (255.255.255.248) | 192.168.10.113 - 192.168.10.118   | 192.168.10.119   |

**Total de IPs da Rede Principal (/24):** 256  
**Total de IPs Alocados:** 120  
**Total de IPs Restantes:** 136 (A partir de 192.168.10.120)


##  Visão Detalhada da Arquitetura

* **`vlsm_tool/models.py`:** Define a `dataclass` `SubnetAllocation`. Esta classe não possui lógica, apenas armazena os dados de uma alocação (nome, hosts necessários, rede) e fornece propriedades (`@property`) para formatar seus próprios dados (ex: `usable_range`).
* **`vlsm_tool/allocator.py`:** Contém a classe `VlsmAllocator`. Gerencia o estado da alocação (ex: `next_available_address`) e contém o algoritmo VLSM para calcular e alocar blocos de IP.
* **`vlsm_tool/display.py`:** Contém a função `display_allocation_table`. Sua única responsabilidade é receber uma lista de alocações e um resumo e imprimi-los no console de forma formatada.
* **`main.py`:** Importa as classes e funções necessárias, fornece os dados de entrada e chama os componentes na ordem correta.

## Licença

Este projeto está distribuído sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.
