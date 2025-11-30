

import numpy as np
from flask import Flask, request, jsonify, render_template, redirect, flash, send_file
import pickle
import pandas as pd

app = Flask(__name__)  # Initialize the flask App

gradient_boost = pickle.load(open('gradient_ev.pkl','rb'))
extra_tree = pickle.load(open('extra_tree_ev.pkl','rb'))

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

@app.route('/preview', methods=["POST"])
def preview():
    if request.method == 'POST':
        dataset = request.files['datasetfile']
        df = pd.read_csv(dataset, encoding='unicode_escape')
        df.set_index('Id', inplace=True)
        return render_template("preview.html", df_view=df)

@app.route('/prediction')
def prediction():
    return render_template('prediction.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        Brand = request.form['Brand']
        if Brand == '0':
             bra = 'Tesla '
        elif Brand == '1':
            bra = 'Volkswagen '
        elif Brand == '2':
            bra = 'Polestar '
        elif Brand == '3':
            bra = 'BMW '
        elif Brand == '4':
            bra = 'Honda '
        elif Brand == '5':
            bra = 'Lucid '
        elif Brand == '6':
            bra = 'Peugeot '
        elif Brand == '7':
            bra = 'Audi '
        elif Brand == '8':
            bra = 'Mercedes '
        elif Brand == '9':
            bra = 'Nissan '
        elif Brand == '10':
            bra = 'Hyundai '
        elif Brand == '11':
            bra = 'Porsche '
        elif Brand == '12':
            bra = 'MG '
        elif Brand == '13':
            bra = 'Mini '
        elif Brand == '14':
            bra = 'Opel '
        elif Brand == '15':
            bra = 'Skoda '
        elif Brand == '16':
            bra = 'Volvo '
        elif Brand == '17':
            bra = 'Kia '
        elif Brand == '18':
            bra = 'Renault '
        elif Brand == '19':
            bra = 'Mazda '
        elif Brand == '20':
            bra = 'Lexus '
        elif Brand == '21':
            bra = 'CUPRA '
        elif Brand == '22':
            bra = 'SEAT '
        elif Brand == '23':
            bra = 'Lightyear '
        elif Brand == '24':
            bra = 'Aiways '
        elif Brand == '25':
            bra = 'DS '
        elif Brand == '26':
            bra = 'Citroen '
        elif Brand == '27':
            bra = 'Jaguar '
        elif Brand == '28':
            bra = 'Ford '
        elif Brand == '29':
            bra = 'Byton '
        elif Brand == '30':
            bra = 'Sono '
        elif Brand == '31':
            bra = 'Smart '
        elif Brand == '32':
            bra = 'Fiat '  
         
        Model = request.form['Model']
        if Model == '0':
           mod = 'Model 3 Long Range Dual Motor'
        elif Model == '1':
            mod = 'ID.3 Pure'
        elif Model == '2':
            mod = '2'
        elif Model == '3':
            mod = 'iX3 '
        elif Model == '4':
            mod = 'e '
        elif Model == '5':
            mod = 'Air '
        elif Model == '6':
            mod = 'e-Golf '
        elif Model == '7':
            mod = 'e-208 '
        elif Model == '8':
            mod = 'Model 3 Standard Range Plus'
        elif Model == '9':
            mod = 'Q4 e-tron '
        elif Model == '10':
            mod = 'EQC 400 4MATIC'
        elif Model == '11':
            mod = 'Leaf '
        elif Model == '12':
            mod = 'Kona Electric 64 kWh'
        elif Model == '13':
            mod = 'i4 '
        elif Model == '14':
            mod = 'IONIQ Electric'
        elif Model == '15':
            mod = 'ID.3 Pro S'
        elif Model == '16':
            mod = 'Taycan Turbo S'
        elif Model == '17':
            mod = 'e-Up! '
        elif Model == '18':
            mod = 'ZS EV'
        elif Model == '19':
            mod = 'Cooper SE '
        elif Model == '20':
            mod = 'Corsa-e '
        elif Model == '21':
            mod = 'Model Y Long Range Dual Motor'
        elif Model == '22':
            mod = 'Enyaq iV 50'
        elif Model == '23':
            mod = 'e-tron GT '
        elif Model == '24':
            mod = 'Model 3 Long Range Performance'
        elif Model == '25':
            mod = 'ID.4 '
        elif Model == '26':
            mod = 'ID.3 Pro'
        elif Model == '27':
            mod = 'XC40 P8 AWD Recharge'
        elif Model == '28':
            mod = 'i3 120 Ah'
        elif Model == '29':
            mod = 'e-2008 SUV '
        elif Model == '30':
            mod = 'e-tron 50 quattro'
        elif Model == '31':
            mod = 'e-Niro 64 kWh'
        elif Model == '32':
            mod = 'Zoe ZE50 R110'
        elif Model == '33':
            mod = 'Cybertruck Tri Motor'
        elif Model == '34':
            mod = 'MX-30 '
        elif Model == '35':
            mod = 'Leaf e+'
        elif Model == '36':
            mod = 'UX 300e'
        elif Model == '37':
            mod = 'el-Born '
        elif Model == '38':
            mod = 'Zoe ZE50 R135'
        elif Model == '39':
            mod = 'EQA '
        elif Model == '40':
            mod = 'Model S Long Range'
        elif Model == '41':
            mod = 'Kona Electric 39 kWh'
        elif Model == '42':
            mod = 'e-tron Sportback 55 quattro'
        elif Model == '43':
            mod = 'CITIGOe iV '
        elif Model == '44':
            mod = 'Mii Electric '
        elif Model == '45':
            mod = 'e-Soul 64 kWh'
        elif Model == '46':
            mod = 'Ampera-e '
        elif Model == '47':
            mod = 'Taycan 4S'
        elif Model == '48':
            mod = 'One '
        elif Model == '49':
            mod = 'U5 '
        elif Model == '50':
            mod = 'e-tron 55 quattro'
        elif Model == '51':
            mod = 'Roadster '
        elif Model == '52':
            mod = 'Mokka-e '
        elif Model == '53':
            mod = 'Enyaq iV 80'
        elif Model == '54':
            mod = 'Model X Long Range'
        elif Model == '55':
            mod = 'e Advance'
        elif Model == '56':
            mod = '3 Crossback E-Tense'
        elif Model == '57':
            mod = 'Twingo ZE'
        elif Model == '58':
            mod = 'e-C4 '
        elif Model == '59':
            mod = 'Model S Performance'
        elif Model == '60':
            mod = 'Zoe ZE40 R110'
        elif Model == '61':
            mod = 'Model Y Long Range Performance'
        elif Model == '62':
            mod = 'Ariya 87kWh'
        elif Model == '63':
            mod = 'I-Pace '
        elif Model == '64':
            mod = 'Mustang Mach-E ER RWD'
        elif Model == '65':
            mod = 'Taycan 4S Plus'
        elif Model == '66':
            mod = 'e-NV200 Evalia '
        elif Model == '67':
            mod = 'Cybertruck Dual Motor'
        elif Model == '68':
            mod = 'Kangoo Maxi ZE 33'
        elif Model == '69':
            mod = 'Mustang Mach-E ER AWD'
        elif Model == '70':
            mod = 'i3s 120 Ah'
        elif Model == '71':
            mod = 'Enyaq iV 80X'
        elif Model == '72':
            mod = 'Taycan Cross Turismo '
        elif Model == '73':
            mod = 'M-Byte 95 kWh 4WD'
        elif Model == '74':
            mod = 'Sion '
        elif Model == '75':
            mod = 'e-Niro 39 kWh'
        elif Model == '76':
            mod = 'Q4 Sportback e-tron '
        elif Model == '77':
            mod = 'EQ forfour '
        elif Model == '78':
            mod = 'Mustang Mach-E SR AWD'
        elif Model == '79':
            mod = 'Taycan Turbo'
        elif Model == '80':
            mod = 'ID.3 1st'
        elif Model == '81':
            mod = 'Model X Performance'
        elif Model == '82':
            mod = 'EQ fortwo coupe'
        elif Model == '83':
            mod = 'Mustang Mach-E SR RWD'
        elif Model == '84':
            mod = 'EQV 300 Long'
        elif Model == '85':
            mod = '500e Hatchback'
        elif Model == '86':
            mod = 'Cybertruck Single Motor'
        elif Model == '87':
            mod = 'e-tron Sportback 50 quattro'
        elif Model == '88':
            mod = 'Enyaq iV vRS'
        elif Model == '89':
            mod = 'Enyaq iV 60'
        elif Model == '90':
            mod = 'e-tron S 55 quattro'
        elif Model == '91':
            mod = 'EQ fortwo cabrio'
        elif Model == '92':
            mod = 'Ariya e-4ORCE 87kWh'
        elif Model == '93':
            mod = '500e Convertible'
        elif Model == '94':
            mod = 'ID.3 Pro Performance'
        elif Model == '95':
            mod = 'e-Soul 39 kWh'
        elif Model == '96':
            mod = 'M-Byte 72 kWh 2WD'
        elif Model == '97':
            mod = 'Ariya 63kWh'
        elif Model == '98':
            mod = 'e-tron S Sportback 55 quattro'
        elif Model == '99':
            mod = 'Ariya e-4ORCE 63kWh'
        elif Model == '100':
            mod = 'Ariya e-4ORCE 87kWh Performance'
        elif Model == '101':
            mod = 'M-Byte 95 kWh 2WD'
        AccelSec = request.form['AccelSec']
        TopSpeed_KmH = request.form['TopSpeed_KmH']
        Range_Km = request.form['Range_Km']
        Efficiency_WhKm = request.form['Efficiency_WhKm']
        FastCharge_KmH = request.form['FastCharge_KmH']
        RapidCharge = request.form['RapidCharge']
        if RapidCharge =='0':
            rapid = 'Yes'
        elif RapidCharge == '1':
             rapid = 'No'
        PowerTrain = request.form['PowerTrain']
        if PowerTrain =='0':
            power = 'AWD'
        elif PowerTrain == '1':
             power = 'RWD'    
        elif PowerTrain == '2':
            power = 'FWD'          
        PlugType = request.form['PlugType']
        if PlugType =='0':
            plug = 'Type 2 CCS'
        elif PlugType == '1':
             plug = 'Type 2 CHAdeMO'    
        elif PlugType == '2':
            plug = 'Type 2' 
        elif  PlugType == '3':
              plug = 'Type 1 CHAdeMO'  
        BodyStyle = request.form['BodyStyle']
        if BodyStyle =='0':
            Body = 'Sedan'
        elif BodyStyle == '1':
             Body = 'Hatchback'    
        elif BodyStyle == '2':
            Body = 'Liftback' 
        elif  BodyStyle == '3':
              Body = 'SUV' 
        elif BodyStyle == '4':
             Body = 'Pickup'    
        elif BodyStyle == '5':
            Body = 'MPV' 
        elif  BodyStyle == '6':
              Body = 'Cabrio'   
        elif BodyStyle == '7':
             Body = 'SPV'    
        elif BodyStyle == '8':
            Body = 'Station' 
        Segment = request.form['Segment']
        if Segment =='0':
            Seg = 'D'
        elif Segment == '1':
             Seg = 'C'    
        elif Segment == '2':
            Seg = 'B' 
        elif  Segment == '3':
              Seg = 'F' 
        elif Segment == '4':
             Seg = 'A'    
        elif Segment == '5':
            Seg = 'E' 
        elif  Segment == '6':
              Seg = 'N'   
        elif Segment == '7':
             Seg = 'S'    
        Seats = request.form['Seats']              
        model = request.form['model']

        input_variables = pd.DataFrame([[Brand,Model,AccelSec,TopSpeed_KmH,Range_Km,Efficiency_WhKm,FastCharge_KmH,RapidCharge,PowerTrain,PlugType,BodyStyle,Segment,Seats]],
                                       columns=['Brand','Model','AccelSec','TopSpeed_KmH','Range_Km','Efficiency_WhKm','FastCharge_KmH','RapidCharge','PowerTrain','PlugType','BodyStyle','Segment','Seats'],
                                       index=['input'])

       
         

        print(input_variables)

        if model == 'GradientBoostingRegressor':
            prediction = gradient_boost.predict(input_variables)
            output = prediction[0]
            result =int(output) * int(output) * int(output)
        elif model == 'ExtraTreeRegressor':
            prediction = extra_tree.predict(input_variables)
            output = prediction[0]
            result =int(output) * int(output) * int(output)


       

    return render_template('result.html', prediction_text=result, model=model, bra=bra,mod=mod,AccelSec=AccelSec,TopSpeed_KmH=TopSpeed_KmH,Range_Km=Range_Km,Efficiency_WhKm=Efficiency_WhKm,FastCharge_KmH=FastCharge_KmH,rapid=rapid,power=power,plug=plug,Body=Body,Seg=Seg,Seats=Seats)

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/performance')
def performance():
    return render_template('performance.html')

if __name__ == "__main__":
    app.run(debug=True)
