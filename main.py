from flask import Flask, request, render_template
from flask import Response
import os
from flask_cors import CORS, cross_origin 

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
@cross_origin()
def home():
    pass
    
        

#port = int(os.getenv("PORT",5000))
if __name__ == "__main__":
    app.run(debug='true')
    # host = '0.0.0.0'
    # port = 8000
    # httpd = simple_server.make_server(host, port, app)
    # # print("Serving on %s %d" % (host, port))
    # httpd.serve_forever()
