from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
import MySQLdb
import json


# Create your views here.
db = MySQLdb.connect(user='root', db='mars', passwd='icaniwill', host='localhost')
def login(request):
	
	if request.method == 'POST': 
		username = request.POST.get('email', None)
		password = request.POST.get('password', None)

		print(username)
		print(password)

		cursor = db.cursor(MySQLdb.cursors.DictCursor)
		password_db = cursor.execute('SELECT * FROM login WHERE username like %s and password like %s', [username,password])
		l1=cursor.fetchall()
		print ("NAna",json.dumps(password_db))
		print("Lola",password_db)
		if (password_db > 0):
			print(l1)
			request.session['user'] = username
			return render(request, 'marsmdwebsite/home.html')
		else:
			print("Failure")
			# name = cursor.fetchall()

	# cursor = db.cursor()
	# result = cursor.execute('INSERT INTO login VALUES ("John", "Doe")')
	# db.commit()
	# name = cursor.fetchall()


	# if(result):
	# 	print(name)
	# 	print ("SUCCESS!")

	return render(request, 'marsmdwebsite/login.html')
	

def index(request):
	return render(request, 'marsmdwebsite/home.html')

def sbadminIndex(request):
	return render(request, 'sbadmin/index.html')
def adminLogin(request):
	return render(request,'sbadmin/login.html')
def history(request):
	if request.method == 'POST':
		fastingsc= request.POST.get('fastingsc', None)
		postmealsc= request.POST.get('postmealsc', None)
		bonecalc= request.POST.get('bonecalc', None)
		bloodcalc= request.POST.get('bloodcalc', None)
		bloodgluc= request.POST.get('bloodgluc', None)
		print("Hey baby")
		print(fastingsc)
		print(postmealsc)
		print(bloodgluc)
		#act = cursor.execute('Insert into family(user1,user2,status,relation) values( %s,%s,%s,%s)',[userid_1['patient_id'],userid_2['patient_id'],'pending',relation])
		#db.commit()
	return render(request,'sbadmin/history.html')
def hearts(request):
	if request.method == 'POST':
		bloodpress= request.POST.get('bloodpress', None)
		walkingheartrate= request.POST.get('walkingheartrate', None)
		restingheartrate= request.POST.get('restingheartrate', None)
		variability= request.POST.get('variability', None)
		print("Hey babu")
		print(bloodpress)
		print(walkingheartrate)
		print(variability)
		#act = cursor.execute('Insert into family(user1,user2,status,relation) values( %s,%s,%s,%s)',[userid_1['patient_id'],userid_2['patient_id'],'pending',relation])
		#db.commit()
	return render(request,'sbadmin/hearts.html')
def nutrition(request):
	if request.method == 'POST':
		caffeine= request.POST.get('caffeine', None)
		carbs= request.POST.get('carbs', None)
		dietarychol= request.POST.get('dietarychol', None)
		fibres= request.POST.get('fibres', None)
		proteins= request.POST.get('proteins', None)
		water= request.POST.get('water', None)
		iron= request.POST.get('iron', None)
		print("Hey babu")
		print(caffeine)
		print(water)
		print(iron)
		act = cursor.execute('Insert into family(user1,user2,status,relation) values( %s,%s,%s,%s)',[userid_1['patient_id'],userid_2['patient_id'],'pending',relation])
		db.commit()
	return render(request,'sbadmin/nutrition.html')
def familyadded(request):
	cursor = db.cursor(MySQLdb.cursors.DictCursor)
	if request.method == 'POST':
		user2 = request.session['user_name']
		user1 = request.session['user']
		relation = request.POST.get('relation', None)
		print(user2)
		print(user1)
		print(relation)
		exec1 =cursor.execute('Select patient_id from patient where username like %s',[user1])
		userid_1=cursor.fetchone()
		exec2 =cursor.execute('Select patient_id from patient where username like %s',[user2])
		userid_2=cursor.fetchone()
		act = cursor.execute('Insert into family(user1,user2,status,relation) values( %s,%s,%s,%s)',[userid_1['patient_id'],userid_2['patient_id'],'pending',relation])
		db.commit()

	return render(request,'sbadmin/familyadded.html')
def activity(request):
	cursor = db.cursor(MySQLdb.cursors.DictCursor)
	if request.method == 'POST':
		cyclingdist= request.POST.get('cyclingdist', None)
		walkingdist= request.POST.get('walkingdist', None)
		stepsclimb= request.POST.get('stepsclimb', None)
		excercisemin= request.POST.get('excercisemin', None)
		standinghrs= request.POST.get('standinghrs', None)
		caloriesburnt= request.POST.get('caloriesburnt', None)
		restinghrs= request.POST.get('restinghrs', None)
		print("Hey babu")
		print(caffeine)
		print(water)
		print(iron)
		#act = cursor.execute('Insert into family(user1,user2,status,relation) values( %s,%s,%s,%s)',[userid_1['patient_id'],userid_2['patient_id'],'pending',relation])
		#db.commit()
	user_name1=request.session['user']
	act = cursor.execute('SELECT patient_id FROM patient where username like %s',[user_name1])
	patient_id=cursor.fetchone()
	print(patient_id)
	act = cursor.execute('SELECT * FROM activity where activity_id like %s',[patient_id['patient_id']])
	activity_db=cursor.fetchall()
	print("Hey")
	print("Hollla ",activity_db)
	print ("NAna",json.dumps(activity_db))
	return render(request,'sbadmin/activity.html',{'activity_db':activity_db})

def tables(request):
	cursor = db.cursor(MySQLdb.cursors.DictCursor)
	if request.method == 'POST':
		user_name = request.POST.get('search', None)
		request.session['user_name'] = user_name
		print(user_name)
		if user_name:
			act = cursor.execute('SELECT * FROM patient where username like %s OR name like %s',[user_name,user_name])
			user_details=cursor.fetchall()
			if (act>0) :
				print("Successful")
				print(user_details)
				return render(request,'sbadmin/tables.html',{'sr':user_details})
			else:
				print("Error")	
	return render(request,'sbadmin/tables.html')


def charts(request):
	user_name1=request.session['user']
	cursor = db.cursor(MySQLdb.cursors.DictCursor)
	act = cursor.execute('SELECT patient_id FROM patient where username like %s',[user_name1])
	patient_id=cursor.fetchone()
	print("Yo",patient_id)
	act = cursor.execute('SELECT datetime FROM activity where activity_id like %s',[patient_id['patient_id']])
	x_axis=cursor.fetchall()
	print(x_axis)
	label=[]
	j=0
	print("Gand mara",str(x_axis[0]['datetime']))
	for i in x_axis:
	  	label.append(str(x_axis[j]['datetime']))
	  	j=j+1
	print(label)
	month=json.dumps(label)

	act1 = cursor.execute('SELECT Cycling_Distance FROM activity where activity_id like %s',[patient_id['patient_id']])
	y_axis=cursor.fetchall()
	print(y_axis)
	data=[]
	j=0
	print("Gand mara",str(y_axis[0]['Cycling_Distance']))
	for i in y_axis:
	  	data.append(str(y_axis[j]['Cycling_Distance']))
	  	j=j+1
	print(data)
	data1=json.dumps(data)

	return render(request,'sbadmin/charts.html',{'label':label,'month':month,'data1':data1})
def register(request):
	return render(request,'sbadmin/register.html')

	