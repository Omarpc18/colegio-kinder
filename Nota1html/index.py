from flask import Flask,render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/Formu')
def Formu():
    return render_template('Eje1.html')

@app.route('/proceso', methods=['GET','POST'])
def proceso():

    if request.method=='POST':
        nota =int(request.form['n1'])
        if nota >0 and  nota <20:
            if (nota>16)and (nota<20):
                mensaje = 'SU calificacion es A'
            
            elif (nota>0)and (nota<9):
                mensaje = 'Su calificacion es E'
        else:
            mensaje = 'Fuera de rango'

    return render_template('Eje1.html', res=mensaje) 

@app.route('/operaciones')
def operaciones():
    return render_template('op.html')

@app.route('/operadores', methods=['POST', 'GET'])
def operadores():
    if request.method == 'POST':
       n=int(request.form['y1'])
       y=int(request.form['y2'])
       op=int(request.form['opcion'])
       
       match op:
            case(1):
               sum = (n+y)
               v = sum
            case(2):
                res = (n-y)
                v = res
            case(3):
                mult= (n*y)
                v=mult
            case(4):
                div= n/y
                v=div
            case _:
               v='funcion no valida'   
    return render_template ('op.html',res=v)


if __name__ == '__main__':
    app.run(debug=True)

