#!/bin/bash

export FLASK_APP=locadora
export FLASK_DEV=development
export FLASK_DEBUG=1
flask init-db
flask run
