import os
from datetime import datetime
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from  sqlalchemy.sql.expression import func, select
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Check if we're on Openshift
if 'OPENSHIFT_APP_DNS' in os.environ:
    app.config.from_pyfile('app-openshift.cfg')
else:
    app.config.from_pyfile('app-local.cfg')
db = SQLAlchemy(app)

# Randomize and redirect to challenge if exists, otherwise go to admin
@app.route('/')
def index():
    return render_template('index.html',
)

# Empties the database and creates all tables
@app.route('/clean_db')
def clean_db():
    db.drop_all()
    db.create_all()
    flash(u'Database records updated', 'primary')
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run()
