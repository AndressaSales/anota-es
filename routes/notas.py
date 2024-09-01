from flask import Blueprint ,render_template, request
from database.models.blocoNotas import bancoNotas

notas_routes = Blueprint('notas', __name__)

@notas_routes.route('/')
def menu():
    notas = bancoNotas.select()
    return render_template('menu.html', notas=notas)

@notas_routes.route('/', methods=['POST'])
def inserir_notas():
    data = request.json

    new_block = bancoNotas.create(
        nome = data['nome'],
        text = data['text']
    )

    return render_template( 'menu.html',notas=new_block)

@notas_routes.route('/<int:notas_id>')
def detalhe_notas(notas_id):
    notas = bancoNotas.get_by_id(notas_id)
    return render_template('detalhe.html', notas=notas)


@notas_routes.route('/<int:notas_id>/edit')
def menu_edit_notas(notas_id):
    notas = bancoNotas.get_by_id(notas_id)
    return render_template('menu.html', notas=notas)
