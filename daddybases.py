from flask import Flask, render_template, flash, request, url_for,redirect
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
#from flask_mysqldb import MYSQL
import socket
import mysql.connector
import requests, json

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
#mysql = MySQL(app)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/results')
def results():
    address = "tallahassee"
    api_key = 'AIzaSyABlmN66Scj0b9xr85WiduJPhigsMJoHy0'

    #lat_list = []
    #long_list = []
    #name_list = []

    # url variable store url
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    # The text string on which to search
    query = raw_input('Search query:')

    # get method of requests module
    # return response object
    r = requests.get(url + 'query=' + query +
                     '&key=' + api_key)

    # json method of response object convert
    #  json format data into python format data
    x = r.json()

    # now x contains list of nested dictionaries
    # we know dictionary contain key value pair
    # store the value of result key in variable y
    y = x['results']

    # keep looping upto length of y

    for i in range(len(y)):
        # Print value corresponding to the
        # 'name' key at the ith index of y
        # print(y[i]['geometry']['location'])

        lat = y[i]['geometry']['location']['lat']
        lng = y[i]['geometry']['location']['lng']
        name = y[i]['name']
        address = y[i]['formatted_address']

        # print(y[i]['name'])

        #lat_list.append(getLat(y[i]))
        #long_list.append(getLong(y[i]))
        #name_list.append(getName(y[i]))

        print("i")
        # address = y[i]['formatted_address']

    # url = 'https://maps.googleapis.com/maps/api/geocode/json?address=' + address
    # jsonurl = urlopen(url)

    # text = json.loads(jsonurl.read())
    # print (text['results'][0]["formatted_address"])
    # print (text['results'][0]["geometry"]['location']["lat"])
    # print (text['results'][0]["geometry"]['location']["lng"])

    return render_template('results.html')

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
    #name = TextField('Name:', validators=[validators.required()])
    #//email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    #password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
    
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
        #cur = mysql.connection.cursor()
        #mysql.connection.commit()
        #cur.close()
        #form = ReusableForm(request.form)
        #print form.errors
        if request.method == 'POST': 
            sqlformula="INSERT INTO `db1`.`users_info` (`IP`, `Gender`, `Age`, `Weight`, `BloodType`, `LastBloodDonation`, `Blood_Pressure`, `Iron`, `Disease`, `Sick`, `Cancer`, `Direction`, `Tattoo`, `Tattoo_reply`, `Piercing`, `Piercing_Date`, `Medication`, `IV`, `STD`, `STD_reply`, `Pregnant`, `HighRisk`, `Travel`, `TravelReply`, `Eligible`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            Gender=request.form['gender'] 
            Age=request.form['Age'] 
            Weight=request.form['Weight']
            Iron=request.form['Ir'] 
            Blood_Pressure=request.form['Bp']
            Bloodtype=request.form['bloodType'] 
            Direction=request.form['Direction'] 
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
                     #(IP,Gender,Age,Weight,BloodType,LastBloodDonation,Blood_Pressure,Iron,Disease,Sick,Cancer,Direction,Tattoo,Tattoo_reply,Piercing,Piercing_Date,Medicaton,IV,STD,STD_reply,Pregnant,HighRisk,Travel,TravelReply,Eligible)
            ValidCase=(IPAddr,Gender,str(Age),str(Weight),Bloodtype,LastBloodDonation,str(Blood_Pressure),str(Iron),Disease,Sick,Cancer,Direction,Tattoo,Tattoo_reply,Piercing,Piercing_Date,Medication,IV,STD,STD_Name,Pregnant,HighRisk,Travel,TravelDate,'Valid')
            VagueCase=(IPAddr,Gender,str(Age),str(Weight),Bloodtype,LastBloodDonation,str(Blood_Pressure),str(Iron),Disease,Sick,Cancer,Direction,Tattoo,Tattoo_reply,Piercing,Piercing_Date,Medication,IV,STD,STD_Name,Pregnant,HighRisk,Travel,TravelDate,'Vague')
            InvalidCase=(IPAddr,Gender,str(Age),str(Weight),Bloodtype,LastBloodDonation,str(Blood_Pressure),str(Iron),Disease,Sick,Cancer,Direction,Tattoo,Tattoo_reply,Piercing,Piercing_Date,Medication,IV,STD,STD_Name,Pregnant,HighRisk,Travel,TravelDate,'Invalid')
            print "Gender:"+Gender +"\n"
            print "Age:"+Age +"\n"
            print "Weight:"+Weight +"\n"
            print "Bloodtype:"+Bloodtype +"\n"
            print "LastBloodDonation:"+LastBloodDonation +"\n"
            print "Blood_Pressure:"+Blood_Pressure +"\n"
            print "Iron:"+Iron +"\n"
            print "Disease:"+Disease +"\n"
            print "Sick:"+Sick +"\n"
            print "Cancer:"+Cancer +"\n"
            print "Direction:"+Direction +"\n"
            print "Tattoo:"+Tattoo +"\n"
            print "Tattoo_reply:"+Tattoo_reply +"\n"
            print "Piercing:"+Piercing +"\n"
            print "Piercing_Date:"+Piercing_Date +"\n"
            print "Medication:"+Medication +"\n"
            print "IV:"+IV +"\n"
            print "STD:"+STD +"\n"
            print "STD_Name:"+STD_Name +"\n"
            print "Pregnant:"+Pregnant +"\n"
            print "HighRisk:"+HighRisk +"\n"
            print "Travel:"+Travel +"\n"
            print "TravelDate:"+TravelDate +"\n"
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


def getBanks():
    # importing required modules


    # enter your api key here
    api_key = 'Your_API_key'

    # url variable store url
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"

    # The text string on which to search
    query = input('Search query: ')

    # get method of requests module
    # return response object
    r = requests.get(url + 'query=' + query +
                     '&key=' + api_key)

    # json method of response object convert
    #  json format data into python format data
    x = r.json()

    # now x contains list of nested dictionaries
    # we know dictionary contain key value pair
    # store the value of result key in variable y
    y = x['results']

    # keep looping upto length of y
    for i in range(len(y)):
        # Print value corresponding to the
        # 'name' key at the ith index of y
        print(y[i]['name'])


if __name__ == "__main__":
    app.run()
