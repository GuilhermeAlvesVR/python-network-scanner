# Python Network Scanner

Ferramenta de linha de comando desenvolvida em **Python** para escanear redes locais e identificar portas abertas em dispositivos conectados.

Este projeto foi criado com o objetivo de praticar:

- Python
- Networking
- Sockets
- Multithreading
- Automação de tarefas
- Uso de Git e GitHub

---

## Funcionalidades

O scanner oferece as seguintes funcionalidades:

1. **Descoberta de Hosts Ativos**  
   Verifica dispositivos ativos dentro de uma rede.

2. **Escaneamento de Portas Comuns**  
   Identifica portas abertas em cada host encontrado.

3. **Execução Paralela**  
   Utiliza multithreading para acelerar o processo de escaneamento.

4. **Registro dos Resultados**  
   Salva automaticamente os resultados em um arquivo `.txt`.

---

## Estrutura do Projeto

```
python-network-scanner
│
├── scanner.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Requisitos

- Python 3
- Linux / WSL / Windows / MacOS

---

## Como Executar

Clone o repositório:

```bash
git clone https://github.com/GuilhermeAlvesVR/python-network-scanner.git
```

Entre na pasta do projeto:

```bash
cd python-network-scanner
```

Execute o scanner:

```bash
python3 scanner.py
```

Digite a rede que deseja escanear:

```
192.168.0.0/24
```

---

## Exemplo de Saída

```
==============================
      Python Network Scanner
==============================

Escaneando rede...

Host ativo: 192.168.0.1
  Porta 80: ABERTA
  Porta 443: ABERTA

Escaneamento finalizado.

Hosts encontrados: 1
```

Um arquivo de resultado também será gerado automaticamente:

```
scan_result_YYYY-MM-DD_HH-MM-SS.txt
```

---

## Tecnologias Utilizadas

- Python
- Socket Programming
- Multithreading
- Git
- GitHub

---

## Autor

Guilherme Alves