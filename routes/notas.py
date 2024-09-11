from flask import Blueprint ,render_template, request
from database.models.blocoNotas import bancoNotas
notas_routes = Blueprint('notas', __name__)

@notas_routes.route('/')
def postados():
    bancosNotas = bancoNotas.select()
    return render_template('lista.html', blocosnotas=bancosNotas)


@notas_routes.route('/new')
def formulario():
    """ formulario para cadastrar um cliente """
    return render_template('formulario.html')


@notas_routes.route('/', methods=['post'])
def inserir_notas():
    """ inserir anotações novas """
    data = request.json

    nova_anotacao = bancoNotas.create(
        title = data['title'],
        text = data['text']
    )

    return render_template('items.html', blocosnota=nova_anotacao)

@notas_routes.route('/<int:blocosnota_id>/delete' , methods=['DELETE'])
def delete(blocosnota_id):
    notas = bancoNotas.get_by_id(blocosnota_id)
    notas.delete_instance()
    return {'deleted': 'ok'}