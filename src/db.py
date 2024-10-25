from flask_sqlalchemy import SQLAlchemy

from config import API_HOST

db = SQLAlchemy()


class Endpoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String, nullable=False)


def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()
        init_default_endpoints()


def init_default_endpoints():
    existing_endpoints = {endpoint.id for endpoint in Endpoint.query.all()}

    default_endpoints = [
        Endpoint(id=1, url=f"http://{API_HOST}:8100/mystream/"),
        Endpoint(id=2, url=f"http://{API_HOST}:8200/mystream/"),
    ]

    updated = False
    for endpoint in default_endpoints:
        if endpoint.id not in existing_endpoints:
            db.session.add(endpoint)
            updated = True

    if updated:
        db.session.commit()


def get_endpoints_from_db():
    endpoints = Endpoint.query.all()
    return [{"id": endpoint.id, "url": endpoint.url} for endpoint in endpoints]


def update_endpoint_in_db(endpoint_id, new_url):
    with db.session.begin():
        endpoint = Endpoint.query.get(endpoint_id)
        if endpoint:
            endpoint.url = new_url
        else:
            db.session.add(Endpoint(id=endpoint_id, url=new_url))


def get_endpoint_by_id(endpoint_id):
    endpoint = Endpoint.query.get(int(endpoint_id))
    return {"id": endpoint.id, "url": endpoint.url} if endpoint else None
