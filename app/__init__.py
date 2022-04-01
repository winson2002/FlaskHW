from flask import Flask, flash, redirect, render_template, request

myobj = Flask(__name__)

from app import routes
