from . import api
from ihome import db

@api.route("/index")
def index():
    return "index page"