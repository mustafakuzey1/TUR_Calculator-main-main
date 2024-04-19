# İçe Aktarma
from flask import Flask, render_template, request


app = Flask(__name__)

def result_calculate(size, lights, device):
    # Elektrikli cihazların enerji tüketimini hesaplamaya olanak tanıyan değişkenler
    return size  + lights  + device 

# İlk sayfa
@app.route('/')
def index():
    return render_template('index.html')
# İkinci sayfa
@app.route('/<size>')
def lights(size):
    return render_template(
                            'lights.html', 
                            size=size
                           )

# Üçüncü sayfa
@app.route('/<size>/<lights>')
def electronics(size, lights):
    return render_template(
                            'electronics.html',                           
                            size = size, 
                            lights = lights                           
                           )

# Üçüncü sayfa
@app.route('/<size>/<lights>/<device>')
def fourth(size, lights,device):
    return render_template(
                            'fourth.html',                           
                            size = size, 
                            lights = lights,
                            device = device
                                   
                           )


#  # Hesaplama
# @app.route('/<size>/<lights>/<device>')
# def end(size, lights, device):
#     return render_template('end.html', 
#                             result=result_calculate(int(size),
#                                                     int(lights), 
#                                                     int(device)
#                                                     )
#                         )




app.run(debug=True)