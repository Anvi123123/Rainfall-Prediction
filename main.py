from flask import render_template,Flask,request, jsonify
import pickle

app = Flask(__name__, static_url_path='/static')
    
app=Flask(__name__) # unique name
file=open("model.pkl","rb")
random_Forest=pickle.load(file)
file.close()

@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="POST":
        myDict = request.form
        Month = int(myDict["Month"])
        Year = int(myDict["Year"])
        
        if Year > 2028:
            return jsonify({'error': 'Year must be less than or equal to 2028 for accurate predictions.'})
    
        pred = [Year,Month]
        res=random_Forest.predict([pred])[0]

        # res=random_Forest.predict(["Year","Month"])
        res=round(res,2)
        return render_template('result.html',Month=Month,Year=Year,res=res)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
