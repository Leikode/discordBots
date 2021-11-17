import os
import pytz
import discord
from datetime import datetime
from discord.ext import tasks, commands
from keep import keep_alive

count = 0
minAnt = 0

dia = {
  0: "segunda",
  1: "terca",
  2: "quarta",
  3: "quinta",
  4: "sexta",
  5: "sabado",
  6: "domingo"
}

aulas = {
  "segunda": {
    "1050": [
      "Sinais e Sistemas", "https://meet.google.com/zrb-sbwx-tru"
      ],
    "1440": [
      "Simulação e Análise de Desempenho", "https://meet.google.com/pxj-vnqx-ptp"
      ],
    "1620": [
      "Organização de Computadores", "https://meet.google.com/whr-cnse-pjq"
      ]},
  "terca": {
    "1050": [
      "Banco de Dados I", "https://meet.google.com/sdm-wphy-ehc"
      ],
    "1440": [
      "Sistemas Digitais II", "https://meet.google.com/hqi-mwir-bii"
      ],
    "1620": [
      "Projeto e Análise de Algoritmos", "https://meet.google.com/hoh-dqcs-gdm"
      ]},
  "quarta": {
    "1050": [
      "Sinais e Sistemas", "https://meet.google.com/zrb-sbwx-tru"
      ],
    "1440": [
      "Simulação e Análise de Desempenho", "https://meet.google.com/pxj-vnqx-ptp"
      ],
    "1620": [
      "Organização de Computadores", "https://meet.google.com/whr-cnse-pjq"
      ]},
  "quinta": {
    "1050": [
      "Banco de Dados I", "https://meet.google.com/sdm-wphy-ehc"
      ],
    "1440": [
      "Sistemas Digitais II", "https://meet.google.com/hqi-mwir-bii"
      ],
    "1620": [
      "Projeto e Análise de Algoritmos", "https://meet.google.com/hoh-dqcs-gdm"
      ]},
  "sexta": {
    "1050": [
      "Teoria dos Grafos", "https://meet.google.com/onc-jvxg-tgx"
      ]}}

def zeraCount(minuto):
  global count
  if minuto > minAnt:
    count = 0

def message(hora, minuto, diaSemana):
  global count, minAnt
  mensagem = None
  zeraCount(minuto)
  if diaSemana in ["segunda", "terca", "quarta", "quinta"]:
    if hora == 10 and minuto == 49 and count == 0:
      mensagem = aulas[diaSemana]["1050"]
      count += 1
      minAnt = minuto
      mensagem = discord.Embed(title=(mensagem[0] + " - " + str(hora) + "h" + str(minuto+1)), description = (mensagem[1]))
    if hora == 14 and minuto == 39 and count == 0:
      mensagem = aulas[diaSemana]["1440"]
      count += 1
      minAnt = minuto
      mensagem = discord.Embed(title=(mensagem[0] + " - " + str(hora) + "h" + str(minuto+1)), description = (mensagem[1]))
    if hora == 16 and minuto == 19 and count == 0:
      mensagem = aulas[diaSemana]["1620"]
      count += 1
      minAnt = minuto
      mensagem = discord.Embed(title=(mensagem[0] + " - " + str(hora) + "h" + str(minuto+1)), description = (mensagem[1]))
    if hora == 13 and minuto == 10 and diaSemana in ["segunda", "quarta"] and count == 0:
      count += 1
      minAnt = minuto
      mensagem = discord.Embed(title=("Introdução à Mecânica dos Fluidos - 13h00"), description = ("O professor Rubelmar mandará em breve o link da aula"))
  elif diaSemana in ["sexta"]:
    if hora == 10 and minuto == 49 and count == 0:
      mensagem = aulas[diaSemana]["1050"]
      count += 1
      minAnt = minuto
      mensagem = discord.Embed(title=(mensagem[0] + " - " + str(hora) + "h" + str(minuto+1)), description = (mensagem[1]))
  return mensagem

t = os.environ['TOKEN']

client = discord.Client()

bot = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
  print("Bot ok!")
  reminder.start()


@bot.command
async def showMessage():
  pass

@tasks.loop(seconds = 1)
async def reminder():

  horario = datetime.now(pytz.timezone('America/Manaus'))

  diaSemana = dia[horario.weekday()]

  hora = horario.hour
  minuto = horario.minute

  mensagem = message(hora, minuto, diaSemana)

  if mensagem is not None:
    channel = client.get_channel(894066268062224454)
    await channel.send(embed = mensagem)


keep_alive()
client.run(t)