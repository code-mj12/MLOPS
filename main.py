#integrate html with flask
from flask import Flask, request, jsonify
import pickle, sklearn
#wsgi application flsk app object
app=Flask(__name__)


@app.route('/api')
def index():
    loaded_model = pickle.load(open('finalized_model.sav', 'rb'))
    result = loaded_model.predict([[1.1]])
    a=str(int(result[0]))

    print("The result is:",a)
    return a


    
if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0")
