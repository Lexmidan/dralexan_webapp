import dash
import dash_bootstrap_components as dbc
from flask import Flask
import dash_auth
import pandas as pd
flask_server = Flask(__name__)
app = dash.Dash(__name__, server=flask_server, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

USERNAME_PASSWORD = pd.read_csv('./data/USERNAME_PASSWORD.csv')
user_pass = [{USERNAME_PASSWORD.loc[i, 'username'] : USERNAME_PASSWORD.loc[i, 'password']
               for i in range(len(USERNAME_PASSWORD))}][0]
auth = dash_auth.BasicAuth(app, user_pass)