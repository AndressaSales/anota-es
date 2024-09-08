from flask import Blueprint ,render_template, request
#from database.models.blocoNotas import bancoNotas
from database.bloco import blocos
notas_routes = Blueprint('notas', __name__)

@notas_routes.route('/')
def postados():
    return render_template('lista.html', blocos=blocos)


@notas_routes.route('/new')
def formulario():
    """ formulario para cadastrar um cliente """
    return render_template('formulario.html')


@notas_routes.route('/', methods=['POST'])
def inserir_notas():
    """ inserir anotações novas """
    data = request.json

    nova_anotacao = blocos.create(
        title = data['title'],
        text = data['text']
    )

    return render_template('items.html', notas=nova_anotacao)

@notas_routes.route('/<int:notas_id>/delete' , methods=['DELETE'])
def delete(notas_id):
    notas = blocos.gey_by_id(notas_id)
    notas.delete_instance()
    return{'deleted' : 'ok'}