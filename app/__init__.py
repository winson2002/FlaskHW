from flask import Flask, flash, redirect, render_template, request
from config import Config

myobj = Flask(__name__)
app.config.from_mapping(
	SECRET_KEY = 'you-will-never-guess'
)

from app import routes
