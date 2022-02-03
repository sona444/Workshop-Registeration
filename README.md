# Workshop-Registeration
- A Simple web app for a photography workshop registeration. 
- Made with Flask a Python framework.
- Working video can be seen at https://drive.google.com/file/d/1q-_VJ9o9WQA7szkJ9K2hhqnQzBg-WzZ2/view?usp=sharing

# Pre-Requisites
 - [PostgreSQL](https://www.postgresql.org/download/) (After installing create database and make changes in env and config accordingly. )

## Setup 
- Clone this repository 
  
  git clone https://github.com/sona444/Workshop-Registeration.git
  
- Setup the virtual environmen 
     
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

## Avatars used in the website

  - Add avatars' links to the "avatars" database.

  - I have used some random avatars.

    For similar look and feel you can add these avatars which I used:

    > https://i.pinimg.com/originals/4b/5d/19/4b5d1954fbb5b6bad18f0ac25c4ab3c3.png

    > https://2.bp.blogspot.com/-x4eBRzgzgTg/WKn5Lq5VzrI/AAAAAAAABrE/mDo0ehzhhtMqcTc4gR62EQ203U-9ljP1QCLcB/s1600/myAvatar.jpeg
    
    > http://creativeedtech.weebly.com/uploads/4/1/6/3/41634549/published/avatar.png?1487742111

    > https://i.pinimg.com/originals/8d/94/5b/8d945bbaf167b063040eca16b0c59cd8.png

    > https://i.pinimg.com/originals/db/fa/08/dbfa0875b8925919a3f16d53d9989738.png
