from flask import Blueprint
import path

home = Blueprint('home', __name__)#first parameter is blueprint name used by routing mechanism second is import name used to locate resources (eg:instance folder)
#object - similar to flask but not an application need to register in application before
#it records operation to be executed
@home.route(path.home)
def initialize():
    return "Journey of the seeker never ends though he may delude himself at every bend"