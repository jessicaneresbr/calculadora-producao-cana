import csv
from datetime import datetime
import os

ARQUIVO = "turnos.csv"

# Cria o arquivo se não existir
if not os.path.exists(ARQUIVO):
    with open(ARQUIVO, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["nome", "turno", "data", "horas"])

def registrar():
    nome = input("Nome do funcionário: ")
    print("Turnos: 1-Manhã (6h-14h) 2-Tarde (14h-22h) 3-Noite (22h-6h)")
    op = input("Escolha o turno (1/2/3): ")
    turnos = {"1": "Manhã", "2": "Tarde", "3": "Noite"}
    turno = turnos.get(op, "Manhã")
    horas = input("Horas trabalhadas: ")
    data = datetime.now().strftime("%d/%m/%Y %H:%M")

    with open(ARQUIVO, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([nome, turno, data, horas])
    print(f"✓ Registrado: {nome} - Turno {turno}")

def listar():
    print("\n--- REGISTROS DE TURNO ---")
    try:
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(f"{row['data']} | {row['nome']} | {row['turno']} | {row['horas']}h")
    except FileNotFoundError:
        print("Nenhum registro ainda.")

while True:
    print("\n1-Registrar turno  2-Listar  3-Sair")
    esc = input("Opção: ")
    if esc == "1":
        registrar()
    elif esc == "2":
        listar()
    elif esc == "3":
        break