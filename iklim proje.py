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


 # Hesaplama
@app.route('/<size>/<lights>/<device>')
def end(size, lights, device):
    return render_template('end.html', 
                            result=result_calculate(int(size),
                                                    int(lights), 
                                                    int(device)
                                                    )
                        )

# Form
@app.route('/form')
def form():
    return render_template('form.html')

#Formun sonuçları
@app.route('/submit', methods=['POST'])

def submit_form():

    # Veri toplama için değişkenleri tanımlayın

    name = request.form['name']

    email = request.form['email']

    address = request.form['address']

    date = request.form['date']

    with open('form.txt', 'a',) as f:
        f.write(f'Name: {name}\
')
        f.write(f'Email: {email}\
')
        f.write(f'Address: {address}\
')
        f.write(f'Date: {date}\
')

    # Verilerinizi kaydedebilir veya e-posta ile gönderebilirsiniz

    return render_template('form_result.html', 

                           # Değişkenleri buraya yerleştirin

                           name=name,

                           email=email,

                           address=address,

                           date=date,

                           )


app.run(debug=True)