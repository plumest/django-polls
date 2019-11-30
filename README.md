by ***Chayathon Khuttiyanon***   
   
## Django Polls Application  
 Polls application that following Django tutorial document  
  
 ## Requirements  
  
 The application requires  
 * Python 3.7.2 or newer  
 * Python add-on modules as in [requirements.txt](requirements.txt)    
  
  
 ## Installation

### Step 1
Open the Terminal and type the following command:    
```
git clone https://github.com/plumest/django-polls.git
```   
    
### Step 2     
Go to `django-poll` directory:    
```
cd django-poll
```

### Step 3
Create virtual environment.    
```
For Windows:
    python -m venv venv

For Mac/Linux:
    python3 -m venv venv
```
### Step 4
Activate virtual environment.
```
For Windows:
    venv\bin\activate.bat

For Mac/Linux:
    source venv/bin/activate
```
### Step 5
Install requirements.    
```
(venv) pip install -r requirements.txt
```
  
### Step 6
Migrate your database:  
```
(venv) python manage.py migrate
```
Make sure you have `db.sqlite3` file in `django-poll`  
  
 ## Running  
  
### Step 1    
Go to `django-poll` directory    

### Step 2   
Run following command on the Terminal    
 ```
(venv) python manage.py runserver
 ``` 
