#!/bin/bash

export FLASK_APP=locadora
export FLASK_DEV=development
flask init-db
flask run
