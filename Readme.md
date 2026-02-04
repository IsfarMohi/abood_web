**index.html**
-ln 1135
*before* 
    <form class="contact-form" action="send_email.php" method="POST"> 
*after*    
    <form class="contact-form" action="/send" method="POST">


**app.py**
-ln 21
*update*
    msg["To"] = "test@gmail.com"
 (add your company mail)

-ln 36 
*update*
    smtp.login("majindevil164@gmail.com", "htdw sgyv oeig eobs")
(add a service email (could be yours))


**How to run**
website/
│
├── templates/
│   └── index.html
│
├── requirements.txt
├── README.md
└── app.py


OPEN CMD
    cd c:/Users/Isfar/OneDrive/Desktop/abood
    python -m venv venv 
    venv\Scripts\activate
    pip install flask
    python app.py
