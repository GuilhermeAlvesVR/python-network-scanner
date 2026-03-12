# Python Network# Python Network Scanner

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

O scanner realiza:

- Descoberta de hosts ativos em uma rede
- Verificação de portas comuns abertas
- Execução paralela para maior velocidade
- Salvamento automático dos resultados em arquivo

---

## Portas Verificadas

O programa verifica algumas portas comuns:

- 22 → SSH  
- 80 → HTTP  
- 135 → RPC  
- 139 → NetBIOS  
- 443 → HTTPS  
- 445 → SMB  
- 3389 → RDP  
- 8080 → HTTP Alternativo

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
- Linux / WSL / MacOS / Windows

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

Informe a rede para escaneamento:

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

---

## Autor

Guilherme Alves
