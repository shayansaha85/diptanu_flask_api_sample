from flask import *
import testsql


app = Flask(__name__)


@app.route("/api/diptanu",  methods = ["POST"])
def api_diptanu():

    data = request.json

    db = data["database"]
    table = data["table"]
    manager = data["manager_id"]

    

    l = testsql.fetchId(db, table, manager)

    return { "employees" : str(l) }

app.run(port=3333, debug=True)