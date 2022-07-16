from flask import Flask, jsonify, render_template, request
from flask_migrate import Migrate
from models.User import User, db
from routes.user_bp import user_bp

app = Flask(__name__)
app.config.from_object('config')
db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(user_bp, url_prefix='/users')


@app.route('/api/v1/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/api/v1/show', methods=['GET'])
def show():
    return jsonify()
@app.route('/api/v1/create', methods=['POST'])
def create():
    data = request.get_json()
    new_user = User()
    db.session.add(new_user)
    db.session.commit()
    return jsonify(data['age'])


if __name__ == '__main__':
    app.debug = True
    app.run()
