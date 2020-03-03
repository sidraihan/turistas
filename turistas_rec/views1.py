import pyrebase
from firebase import firebase  

firebase = firebase.FirebaseApplication('https://djangoplaces.firebaseio.com/', None)  
data =  { 'Name': 'Vivek',  
          'RollNo': 1,  
          'Percentage': 76.02  
          }  
result = firebase.post('/djangoplaces/Places',data)  
print(result)
  