by ***Chayathon Khuttiyanon***   
   
## Django Polls Application  
 Polls application that following Django tutorial document  
  
 ## Requirements  
  
 The application requires  
 * Python 3.6.6 or newer  
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
Open Terminal and type command (make your path in django-poll diretory):

    For Windows:
        pip install -r requirements.txt

    For Mac/Linux
        pip3 install -r requirements.txt
```
  
### Step 3
Migrate your database:  
```
    For Windows:
        python manage.py migrate
    
    For Mac/Linux
        python3 manage.py migrate
```
Make sure you have `db.sqlite3` file in `django-poll`  
  
 ## Running  
  
### Step 1    
Run following command on the Terminal to go to `django-poll` directory    
```
cd django-poll
```    

### Step 2   
Run following command on the Terminal    
 ```
    For Windows:
        python manage.py runserver <IPv4>:<PORT>

    For Mac/Linux:
        python3 manage.py runserver <IPv4>:<PORT>
 ```
***IPv4_Address*** : Your IPv4 (default is localhost).  
***PORT*** : Port that you want to run server (default is 8000).  
