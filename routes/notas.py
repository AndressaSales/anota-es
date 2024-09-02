from flask import Blueprint ,render_template, request
#from database.models.blocoNotas import bancoNotas

notas_routes = Blueprint('notas', __name__)

@notas_routes.route('/')
def postados():
    blocos = [
        {"title": "Fazer tarefa", "text": "Preciso fazer as tarrefas de matematica e portugues"},
        {"title": "Fazer tarefa", "text": "Preciso fazer as tarrefas de matematica e portugues"},
        {"title": "Fazer tarefa", "text": "Preciso fazer as tarrefas de matematica e portugues"},
        {"title": "Fazer tarefa", "text": "Preciso fazer as tarrefas de matematica e portugues"},
        {"title": "Fazer tarefa", "text": "Preciso fazer as tarrefas de matematica e portugues"},
        {"title": "Fazer tarefa", "text": "Preciso fazer as tarrefas de matematica e portugues"},
    ]
    return render_template('lista.html', blocos=blocos)

@notas_routes.route('/', methods=['POST'])
def inserir_notas():
    return render_template('form.html')
