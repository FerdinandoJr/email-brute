import os 
import smtplib
from email.message import EmailMessage

EMAIL_ADDRESS = 'your-email@gmail.com'
EMAIL_PASSWORD = '' #Senha gerada pelo seu gmail

#HTML DO EMAIL
html= """<!DOCTYPE html>
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Your HTML Title</title>
  <style>
* {padding: 0;margin: 0;position: relative;font-family: 'Google Sans',Roboto,RobotoDraft,Helvetica,Arial,sans-serif; user-select:none}
  body{width:100%;height:100%;overflow:hidden}
  img {
  width: 100%;
}
.b-main {
    margin: 0 auto;
    width: 500px;
    padding: 24px 30px;
    border: 1px solid #757575;
    border-radius: 10px;
}

.b-body {
    margin: 24px 0;
    border-top: 1px solid #d2d2d2;
    padding: 24px 0 0;
}
.b-footer {
  margin-top:50px;
}

.b-title {
  text-align: center;
  font-weight: 600;
  text-transform: uppercase;
  font-size: 24px;
}

.b-fotter-down {
  text-align: center;
  font-size: 12px;
}
  
  .b-top {
    padding-top: 0px;
}
.b-msg {
    text-align: center;
    font-size: 12px;
}
.b-login {
    padding: 10px;
    margin: 20px auto;
    max-width: 300px;
    display: grid;
    grid-template-columns: 50% 50%;
    
}
.b-logo {
    width: 65px;
    height: 90px;
    position: relative;
    margin: 0 auto;
}
.b-login-user, .b-login-pass {
    border: 1px dashed gray;
    margin: 10px;
    text-align: center;
    padding: 15px;
    border-radius: 40px;
}


.b-login-title {
    position: absolute;
    top: -10px;
    left: 50%;
    font-size: 12px;
    background: white;
    transform: translate(-50%);
    padding: 0 5px;
    color: #3e3e3e;
}
.b-login-data {
    user-select: text;
}

  </style>
  <body>
  <div class='b-main'>
    
    <div class='b-top'>
      <div class='b-logo'><img src='https://imageshack.com/i/pmrCucU1p'></div>
      <div class='b-title' style="padding: 10px 0 0;"> I maratona interna 2022</div>

    </div>
  <div class='b-body'>
    <div class='b-msg'>
      Agradecemos seu interesse em inscrever-se na primeira maratona interna da UDESC em 2022!!!
      Gostaríamos de lembrar que a competição é dia 25/06 às 14:00 no site <a href='http://200.19.107.69/boca/' target="_blank">http://200.19.107.69/boca/</a> .
      É de extrema importância testar o ambiente no warm-up que acontecerá dia <b>25/06</b> às <b>10:00. </b><br>
      Estamos enviando seu login e senha<br>
    </div>
    <div class='b-login'>
      <div class='b-login-user'>
        <div class='b-login-title'>usuário</div>
        <div class='b-login-data'>username</div>
      </div>
      <div class='b-login-pass'>
    <div class='b-login-title'>senha</div>
        <div class='b-login-data'>password</div>
      </div>
    </div>
    <div class='b-msg'>
      Mais informações em<br>
      <a href='https://bruteudesc.com/'>https://bruteudesc.com/</a>
    <div class='b-msg'>
    </div>
    <div class='b-footer'>
      <div class='b-fotter-down'><a href="https://www.bruteudesc.com/">BRUTE</a><p>Competitive Programming</p></div>
    </div>
  <div>
  </body>
</html>
"""


msg = EmailMessage()
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS
msg['Subject'] = "ASSUNTO"
msg.set_content('')
msg.add_alternative(html, subtype='html')

#Enviar um email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
  smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
  smtp.send_message(msg)
