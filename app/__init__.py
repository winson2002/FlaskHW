from flask import Flask, flash, redirect, render_template, request

myapp_obj = Flask(__name__)

from app import routes
