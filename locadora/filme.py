import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from locadora.db import get_db

bp = Blueprint('filme', __name__, url_prefix="/filme", template_folder='templates')

@bp.route('/cadastrar', methods=('POST',))
def cadastrar():
    if request.method == 'POST':
        nome = request.form['nome']
        print('nome pego eh:', nome)
        preco = request.form['preco']
        print('preco pego eh:', preco)
        db = get_db()
        error = None

        if not preco:
            error = 'Preco do filme eh requerido.'
        elif not nome:
            error = 'Nome do filme eh requerido.'
        else:
            db.execute(
                'INSERT INTO filme (nome, preco) VALUES(?, ?)', (nome, preco)
            )
            db.commit()

        flash(error)

    return render_template('templates/success.html')
