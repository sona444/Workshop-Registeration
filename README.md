# Workshop-Registeration
- A Simple web app for a photography workshop registeration. 
- Made with Flask a Python framework.

# Pre-Requisites
 - [PostgreSQL](https://www.postgresql.org/download/) (After installing create database and make changes in env and config accordingly. )

## Setup 
- Clone this repository 
  
  git clone https://github.com/sona444/Workshop-Registeration.git
  
- Setup the virtual environment 
     
    python3 -m venv venv 
    
- Step into that environment 
   
   source venv/bin/activate
   
- Install all the required packages 
    
   pip3 install requirements.txt
   
- Initialize database 
  
  flask db init
  
- Migrate and upgrade 
    
   flask db migrate && flask db upgrade
   
- Finally run the server 
   
   flask run
   
  >   You must see the server running at  http://127.0.0.1:5000/ 