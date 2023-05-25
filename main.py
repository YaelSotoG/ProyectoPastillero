import machine
from machine import Timer,Pin,PWM
import time as t
import time
import ntptime
import utime


pagina_actual = 1
inicio="""<html>
    <head>
    <title>ESP32 Web Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <style>
        html {
            font-family: Helvetica;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
            background-color: #1e2447;
        }
        nav{
            width: 100%;
            height:200px;
            padding: 0px;
            margin: 0px;
            border: 0px;
            top: 0;
            background-color: #4974ec;
            text-align: start;
            position: fixed;
            translate: -8px;
        }
        h1 {
            color: #0F3376;
            /* padding: 2vh; */
        }
        .icono{
            width: 50px;
            height: 50px;
            position: absolute;
            top: 50px;
            right: 50px;
            background-color: rgba(255, 255, 255, 1);
            border: rgba(255, 255, 255, 1);
        }

        nav h1{
            padding-top: 50px;
            padding-left: 50px;
        }
        ul {
            list-style-type: none;
            margin: 0;
             padding: 0;
        }
        ul.full{
           
           
             overflow: hidden;
             display: grid;
             grid-template-columns: repeat(7, 1fr);
             column-gap: 5px;
        }
        .full{
            width: 100%;
            height: 60px;
        }
        .selector{
            display: flex;
            flex-direction: row;
            margin-top: 10px;
            /* position: fixed; */
            /* background-color: aqua; */
        }
       ul.full li{
            display: inline-block;
        }
        li button{
            width: 100%;
            background-color:cornflowerblue;
            height: 90%;
            margin: 0;
            padding: 0;
            border: 0;
            border-radius: 10px;
        }

        li button:hover{
            background-color: #1e2447;
        }

        .marco{
            width: 100%;
            height: 100%;
            display: flex;;
            justify-content: center;
            /* align-items: center; */
            border-radius: 20px;
            margin-top: 200px;
            
        }
        section div{
            background-color: darkslateblue;
            width: 95%;
            /* height: auto; */
        }
        /* ul.cards li{
           
            
        } */
        ul.cards li button{
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .pastillas{
            width: 100%;
            height: 200px;
        }
        .card{
            width: 95%;
            height: 180px;
            background-color:aliceblue ;
        }
        
        .pastilla{
            width: 50px;
            height: 50px;
        }


      
    </style>
    </head>
    <nav>
        <h1>Pastillero</h1>   
        <button class="icono"><a href="/?pastillas">add</a></button>
        <section class="selector full">
            <ul class="full">
                 <li><a href="/?lunes"><button>L</button></a></li>
                <li><a href="/?martes"><button>Ma</button></a></li>
                <li><a href="/?miercoles"><button>Mi</button></a></li>
                <li><a href="/?jueves"><button>J</button></a></li>
                <li><a href="/?viernes"><button>D</button></a></li>
                <li><a href="/?sabado"><button>V</button></a></li>
                <li><a href="/?domingo"><button>S</button></a></li>
            </ul>
        </section>
    </nav> """

agregar="""<html>
<head>
    <title>ESP32 Web Server</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="icon" href="data:,">
    <style>
        nav{
            width: 100%;
            height:150px;
            padding: 0px;
            margin: 0px;
            border: 0px;
            top: 0;
            background-color: #4974ec;
            text-align: start;
            position: fixed;
            translate: -8px;
        }
         .icono{
            width: 50px;
            height: 50px;
            padding-top: 10px;
            padding-left: 10px;
            background-color: rgba(255, 255, 255, 1);
            border: rgba(255, 255, 255, 1);
            
        }
        .regreso{
            width: 50px;
            height: 50px;
        }
        h1 {
            color: #0F3376;
            /* padding: 2vh; */
            padding-top: 10px;
            padding-left: 50px;
        }
        body{
            padding-top: 150px;
        }

    </style>
    </head>

    <nav>
        <button class="icono"><a href="/?regresar">Regresar</a></button>
        <h1>Agregar Pastillas</h1> 
    </nav> 
    <body>
        <form action="">
            <p>Nombre del medicamento</p>
            <input type="text">
            <p>Horario de inicio</p>
            <input type="datetime" name="" id="">
            <p>Rango entre horas</p>
            <input type="number">
            <p>¿Cuantos dias?</p>
            <input type="number" name="" id="">
            <p>Cantidad de pastillas por dosis</p>
            <input type="number" name="" id=""><br>
            <input type="button" value="Agregar">
        </form>
    </body>

    </html>"""

cuerpo="""<body><section class="marco"><div><ul class="cards ">""" +"""</ul></div></section></body>"""

Horario=[
  {"lunes":
    {18:[{"Pastilla":"paracetamos","cantidad":1},{"Pastilla":"diclofenaco","cantidad":2}],
     9:[{"Pastilla":"paracetamos","cantidad":1},{"Pastilla":"diclofenaco","cantidad":2}]}
  },
  {"martes":
    {6:[{"Pastilla":"paracetamos","cantidad":1},{"Pastilla":"diclofenaco","cantidad":2}],
     7:[{"Pastilla":"paracetamos","cantidad":1},{"Pastilla":"diclofenaco","cantidad":2}]}
  },
  {"miercoles":
    {6:[{"Pastilla":"paracetamos","cantidad":1},{"Pastilla":"diclofenaco","cantidad":2}],
     7:[{"Pastilla":"paracetamos","cantidad":1},{"Pastilla":"diclofenaco","cantidad":2}]}
  },
  {"jueves":
    {6:[{"Pastilla":"paracetamos","cantidad":1},{"Pastilla":"diclofenaco","cantidad":2}],
     7:[{"Pastilla":"paracetamos","cantidad":1},{"Pastilla":"diclofenaco","cantidad":2}]}
  },
  {"viernes":
    {6:[{"Pastilla":"paracetamos","cantidad":1},{"Pastilla":"diclofenaco","cantidad":2}],
     7:[{"Pastilla":"paracetamos","cantidad":1},{"Pastilla":"diclofenaco","cantidad":2}]}
  },
  {"sabado":
    {6:[{"Pastilla":"paracetamos","cantidad":1},{"Pastilla":"diclofenaco","cantidad":2}],
     7:[{"Pastilla":"paracetamos","cantidad":1},{"Pastilla":"diclofenaco","cantidad":2}]}
  },
  {"domingo":
    {6:[{"Pastilla":"paracetamos","cantidad":1},{"Pastilla":"diclofenaco","cantidad":2}],
     7:[{"Pastilla":"paracetamos","cantidad":1},{"Pastilla":"diclofenaco","cantidad":2}]}
  }
]
cartapastillas=""


def get_page_html(pagina):
  if pagina == 1:
    html = inicio + cuerpo + '</html>'
  elif pagina==2:
    html=agregar
  else:
    html = "<html><body><h1>Página no encontrada</h1></body></html>"
  return html

 
def servos():
  print("activar servo")
  if sensor_pin==1:
    sg90.duty(26)
    time.sleep(1)
    sg90.duty(123)
  return

def card(dia):
  cartapastillas=""
  for k in Horario:
    for i,y in k.items():
      if i==dia:
        for z,a in y.items():
          cartapastillas=cartapastillas + '<li class="pastillas"><button><div class="card"><h1>Pastillas:'+str(z)+' hrs </h1><ol>'
          if z==hora:
            servos()
          for b in a:
            print(b)
            for c,d in b.items():
              print(c)
              if c=="Pastilla":
                cartapastillas= cartapastillas + '<li>' + d +'</li>'
          cartapastillas=cartapastillas+'</ol></div></button></li>'
  return """<body><section class="marco"><div><ul class="cards ">""" + cartapastillas + """</ul></div></section></body>"""

def desborde(Timer):
  print("chequeop")
  machine.reset()
  return

# def web_page(): 
#   html = inicio + cuerpo + '</html>'
#   return html

def web_page():
  response = get_page_html(pagina_actual)
  return response

def agregar_page(): 
  html = agregar
  return html


#interrupcion por timer0
temp=Timer(0)
temp.init(period=150000, mode=Timer.PERIODIC, callback=desborde)

#interrupcion por boton
button_pin = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)  # Ejemplo con un botón en el pin GPIO 4
sensor_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)
#servo
sg90 = PWM(Pin(22, mode=Pin.OUT))
sg90.freq(50)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  ntptime.settime()
  from machine import RTC
  (year, month, day, weekday, hour, minute, second, milisecond) = RTC().datetime()                
  #Corrija su Zona Horaria GMT en la variable hour
  #Ejemplo: Zona Horaria GMT corregida para Ecuador: GMT-5 = hour-5
  RTC().init((year, month, day, weekday, hour-6, minute, second, milisecond))
  print (RTC().datetime()[4])
  hora=RTC().datetime()[4]
  try:
    #socket entre la pagina y el server
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)   
    #aqui se agrega la logica
   
    lunes=request.find('/?lunes')
    martes=request.find('/?martes')
    miercoles=request.find('/?miercoles')
    jueves=request.find('/?jueves')
    viernes=request.find('/?viernes')
    sabado=request.find('/?sabado')
    domingo=request.find('/?domingo')
    agregar=request.find('/?pastillas')
    regresar=request.find('/?regresar')
    print(lunes)
    #cuando se presiona el boton lanza un 6 asi que si tiene un 6 significa que se presiono
    if lunes == 6:
      cuerpo=card('lunes')
    if martes == 6:
      cuerpo=card('martes')
    if miercoles == 6:
      cuerpo=card('miercoles')
    if jueves == 6:
      cuerpo=card('jueves')
    if viernes == 6:
      cuerpo=card('viernes')
    if sabado == 6:
      cuerpo=card('sabado')
    if domingo == 6:
      cuerpo=card('domingo')
    if agregar== 6 :
      print('Cambiar a Página 2')
      pagina_actual = 2
    
    elif regresar == 6:
      print('Cambiar a Página 1')
      pagina_actual = 1
      
    response = web_page()
    print("aqui")
    conn.send('HTTP/1.1 200 OK \')
    conn.send('Content-Type: text/html \')
    conn.send('Connection: close \')
    conn.send(response)
    conn.close()
    if not button_pin.value():
      break
  except Exception as e:
    print(e)
    break  
