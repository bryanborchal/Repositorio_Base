import csv

nome = input("Qual seu nome?")
email = input("Qual o seu e-mail?")
senha = input("Qual a sua senha?")


with open("cadastros.csv","r",newline='',encoding="utf-8") as arquivo: