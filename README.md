by ***Chayathon Khuttiyanon***   

# Installation

### Step 1
Open the Terminal and type the following command:    
`git clone https://github.com/plumest/django-polls.git`   
    
### Step 2     
Install requiremant:    
`python (3.6 or newer)`      
`django`    

# How to run locally   
### Step 1    
Go to `django-polls` directory    

### Step 2   
Run following command on the Terminal   

***For Windows:***  
`python manage.py runserver`  
  
***For MacOS or Linux:***   
`python3 manage.py runserver`  
   
# How to run server  
### Step 1  
Open `django/mysite/setting.py`  

### Step 2  
Add ***Your IPv4 address*** into `ALLOWED_HOSTS` list  

### Step 3  
Run following command (Your path should be `django-polls`)  

***For Windows:***  
`python manage.py runserver YOUR_IPv4_Address:PORT`  
  
***For MacOS or Linux:***   
`python3 manage.py runserver IPv4_Address:PORT`  

***IPv4_Address*** : Your IPv4 that you add in step 2.  
***PORT*** : Port that you want to run server.  