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

# Dördüncü sayfa
@app.route('/<size>/<lights>/<device>')
def fourth(size, lights,device):
    return render_template(
                            'fourth.html',                           
                            size = size, 
                            lights = lights,
                            device = device
                                   
                           )

#Beşinci sayfa
@app.route('/<size>/<lights>/<device>/<fourth>')
def sut (size, lights,device,fourth):
    return render_template(      
                            'süt_ürünleri.html',                 
                            size = size, 
                            lights = lights,
                            device = device,
                            fourth = fourth                           
                           )


#Altıncı sayfa
@app.route('/<size>/<lights>/<device>/<fourth>/<sut>')
def evdek (size, lights,device,fourth,sut):
    return render_template(      
                            'ev_dekorasyon.html',                 
                            size = size, 
                            lights = lights,
                            device = device,
                            fourth = fourth,
                            sut = sut
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