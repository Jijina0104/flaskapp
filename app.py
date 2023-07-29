from flask import Flask,request,render_template
app = Flask(__name__) #its creation of an object named app. __name__ is a special Python variable that refers to the name of the current module. When you use __name__, it represents the name of the script or module where the Flask class is being used.
 
@app.route('/')
def welcome():
    return "Welcome to FLask"

@app.route('/cal', methods=["GET"])
def math_operator():
    operation=request.json("operation") #get from html : input from postman 
    num1=request.json("num1") #get from html : input from postman 
    num2=request.json("num2") #get from html : input from postman 
    if operation=="add":
        result=num1+num2
    elif operation=="multiply":
        result=num1*num2
    elif operation=="divide":
        result=num1/num2
    else:
        result=num1-num2

print(__name__)
if __name__=='__main__':
    app.run(debug=True)