from flask import Flask, flash, request, redirect, render_template

myobj = Flask(__name__)
myobj.config.from_mapping(
	SECRET_KEY = 'you-will-never-guess'
)

from app import routes
