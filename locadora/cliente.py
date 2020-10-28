import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flaskr.db import get_db

bp = Blueprint('cliente', __name__, url_prefix="/cliente")


@bp.route('/create', methods=('POST'))
def create():
    if request.method == 'POST':
        pass
    else:
        flash('Invalid HTTP verb for creating a new client.')