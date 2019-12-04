from flask import Flask, render_template, flash, request, url_for,redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#from flask_mysqldb import MYSQL
import socket
import mysql.connector
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

import requests, json
from urllib import urlopen
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
GoogleMaps(app, key="AIzaSyABlmN66Scj0b9xr85WiduJPhigsMJoHy0")

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/results')
def results():
    try:
            hostname = socket.gethostname()    
            IPAddr = socket.gethostbyname(hostname)    
            IPAddr= str(IPAddr)
    except:
            print "Error"
    db = mysql.connector.connect(host="127.0.0.1", port =3306,user="root", passwd="password123!", database='db1',autocommit=True, auth_plugin='mysql_native_password')
    print "Here"+ City 
    cur = db.cursor()
    api_key = 'AIzaSyABlmN66Scj0b9xr85WiduJPhigsMJoHy0'
    # url variable store url
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    # The text string on which to search
   # query = raw_input('Search query:')

    # get method of requests module
    # return response object
    blood = ' Blood Bank'
    store = City
    value = store + blood
    r = requests.get(url + 'query=' + value +
                     '&key=' + api_key)
    print City
    x = r.json()
    y = x['results']
    coordList = []
    for i in range(len(y)):
        lat = y[i]['geometry']['location']['lat']
        lng = y[i]['geometry']['location']['lng']
        
        coordList.append(tuple((lat,lng)))
        name = y[i]['name']
        address = y[i]['formatted_address']
        print "Lat:"+str(lat)
        print "lng:"+ str(lng)
        print "name:"+name
        print "Address:"+address
        Formula=(lat,lng,IPAddr,name,address)
        formula="INSERT INTO `db1`.`organization` (`Latitude`, `Longitude`, `IP`, `Name`, `Street_Address`) VALUES (%s, %s, %s, %s, %s)"
        try:   
            cur.execute(formula,Formula)
            db.commit()
        except:
            delete_state="DELETE FROM `db1`.`organization` WHERE IP = %s"       
            cur.execute(delete_state,(IPAddr,))
            db.commit()
            cur.execute(formula,Formula)
            db.commit()
            print "WTF ERROR"
            pass
   
    mymap = Map(identifier="view-side",lat=30.4491,lng=-84.2985, markers=coordList)

    return render_template('results.html', mymap=mymap)

@app.route('/Valid')
def Valid():
    return render_template('Validform.html')
@app.route('/Invalid')
def Invalid():
    return render_template('Invalidform.html')
@app.route('/Vague')
def Vague():
    return render_template('Vagueform.html')
@app.route('/FAQ')
def FAQ():
    return render_template('FAQ.html')


class ReusableForm(Form):

    
    @app.route("/check", methods=['GET', 'POST'])
    def check():
        try:
            hostname = socket.gethostname()    
            IPAddr = socket.gethostbyname(hostname)    
            IPAddr= str(IPAddr)
        except:
            print "Error"
        db = mysql.connector.connect(host="127.0.0.1", port =3306,user="root", passwd="password123!", database='db1',autocommit=True, auth_plugin='mysql_native_password')
        cur = db.cursor()
        if request.method == 'POST': 
            sqlformula="INSERT INTO `db1`.`users_info` (`IP`, `Gender`, `Age`, `Weight`, `BloodType`, `LastBloodDonation`, `Blood_Pressure`, `Iron`, `Disease`, `Sick`, `Cancer`, `Direction`, `Tattoo`, `Tattoo_reply`, `Piercing`, `Piercing_Date`, `Medication`, `IV`, `STD`, `STD_reply`, `Pregnant`, `HighRisk`, `Travel`, `TravelReply`, `Eligible`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            Gender=request.form['gender'] 
            Age=request.form['Age'] 
            Weight=request.form['Weight']
            Iron=request.form['Ir'] 
            Blood_Pressure=request.form['Bp']
            Bloodtype=request.form['bloodType'] 
            Direction=request.form['Direction']
            global City
            City = Direction
            Disease=request.form['Disease']
            LastBloodDonation=request.form['LastDonation'] 
            Sick=request.form['Sick'] 
            Cancer=request.form['Cancer'] 
            Tattoo=request.form['Tattoo']
            Tattoo_reply=request.form['Tattoo_Reply']
            Piercing=request.form['Piercing'] 
            Piercing_Date=request.form['Piercing_Reply']
            Medication=request.form['Medication']
            IV=request.form['IV'] 
            STD=request.form['STD']
            STD_Name=request.form['STD_name']
            Pregnant=request.form['Pregnant']
            HighRisk=request.form['HighRisk'] 
            Travel=request.form['Travel'] 
            TravelDate=request.form['Travel_reply'] 
            ValidCase=(IPAddr,Gender,str(Age),str(Weight),Bloodtype,LastBloodDonation,str(Blood_Pressure),str(Iron),Disease,Sick,Cancer,Direction,Tattoo,Tattoo_reply,Piercing,Piercing_Date,Medication,IV,STD,STD_Name,Pregnant,HighRisk,Travel,TravelDate,'Valid')
            VagueCase=(IPAddr,Gender,str(Age),str(Weight),Bloodtype,LastBloodDonation,str(Blood_Pressure),str(Iron),Disease,Sick,Cancer,Direction,Tattoo,Tattoo_reply,Piercing,Piercing_Date,Medication,IV,STD,STD_Name,Pregnant,HighRisk,Travel,TravelDate,'Vague')
            InvalidCase=(IPAddr,Gender,str(Age),str(Weight),Bloodtype,LastBloodDonation,str(Blood_Pressure),str(Iron),Disease,Sick,Cancer,Direction,Tattoo,Tattoo_reply,Piercing,Piercing_Date,Medication,IV,STD,STD_Name,Pregnant,HighRisk,Travel,TravelDate,'Invalid')
            update= "UPDATE `db1`.`users_info` SET `IP` = %s , `Gender` = %s, `Age` =%s , `Weight` =%s , `BloodType` = %s, `LastBloodDonation` = %s , `Blood_Pressure` =%s, `Iron` =%s , `Disease` =%s , `Sick` =%s , `Cancer` =%s , `Direction` =%s , `Tattoo` = %s, `Tattoo_reply` = %s, `Piercing` =%s , `Piercing_Date` =%s , `Medication` =%s , `IV` = %s, `STD` =%s , `STD_reply` =%s , `Pregnant` =%s , `HighRisk` = %s, `Travel` =%s , `TravelReply` =%s , `Eligible` = %s WHERE (`IP` = %s)"

            try:
                cur.execute("Select IP from`db1`.`users_info`")
                results=cur.fetchone()
            except:
                print "Error"
            if  int(Age) <17 or Sick=='Yes'or Pregnant=='Yes' or Cancer=='Yes' or IV=='Yes' or int(Weight) <110 or HighRisk=='Yes'or (float(Iron)<=13 and Gender=='Male' or float(Iron)<=12.5 and Gender=='Female' or float(Iron)<=13.0 and Gender=='Other') or LastBloodDonation =='No' or (Tattoo =='Yes' and Tattoo_reply=='No') or (Piercing =='Yes' and Piercing_Date=='No') or (Travel =='Yes' and TravelDate=='No') or (STD =='Yes'  and STD_Name=='No') or int(Blood_Pressure)<90 or int(Blood_Pressure)>180:
                try:             
                     update2=(IPAddr,Gender,Age,Weight,Bloodtype,LastBloodDonation,Blood_Pressure,Iron,Disease,Sick,Cancer,Direction,Tattoo,Tattoo_reply,Piercing,Piercing_Date,Medication,IV,STD,STD_Name,Pregnant,HighRisk,Travel,TravelDate,"Invalid",IPAddr)
                     for x in results:
                         if (IPAddr==x):
                             cur.execute(update,update2)
                             db.commit()
                             return redirect(url_for('Invalid'))
                     cur.execute(sqlformula)
                     db.commit()
                     return redirect(url_for('Invalid'))
                except:
                    print "Error cannot insert value"    
            else:
                if Disease=='Yes' or Medication == 'Yes' or (STD =='Yes' and STD_Name=='Yes') :
                   try:
                       update4=(IPAddr,Gender,Age,Weight,Bloodtype,LastBloodDonation,Blood_Pressure,Iron,Disease,Sick,Cancer,Direction,Tattoo,Tattoo_reply,Piercing,Piercing_Date,Medication,IV,STD,STD_Name,Pregnant,HighRisk,Travel,TravelDate,"Vague",IPAddr)
                       for x in results:
                           if (IPAddr==x):
                             cur.execute(update,update4)
                             db.commit()
                             return redirect(url_for('Vague'))
                       cur.execute(sqlformula,VagueCase)
                       db.commit()
                       return redirect(url_for('Vague'))
                   except:
                       print "Error cannot insert value"
                try:
                     update6=(IPAddr,Gender,Age,Weight,Bloodtype,LastBloodDonation,Blood_Pressure,Iron,Disease,Sick,Cancer,Direction,Tattoo,Tattoo_reply,Piercing,Piercing_Date,Medication,IV,STD,STD_Name,Pregnant,HighRisk,Travel,TravelDate,"Valid",IPAddr)
                     for x in results:
                         if (IPAddr==x):
                             cur.execute(update,update6)
                             db.commit()
                             return redirect(url_for('Valid'))
                     cur.execute(sqlformula,ValidCase)
                     db.commit()
                     return redirect(url_for('Valid'))
                except: 
                      print "Error cannot insert value"
          

        return render_template('check.html')


if __name__ == "__main__":
    app.run()
