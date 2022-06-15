from flask import Blueprint

storeitems = Blueprint('storeitems', __name__, url_prefix='/api/v1/storeitems')

@storeitems.get('/')
def get_items():
    return {"storeitems":[]}
