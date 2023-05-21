import machine


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
            background-color: rgba(255, 255, 255, 0);
            border: rgba(255, 255, 255, 0);
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
        <button class="icono" onclick="window.location.href='./pastillas.html'"><img class="pastilla" src="./assets/vitamina.png" ></button>
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

cuerpo="""<body><section class="marco">""" + """</section></body>"""

Horario=[
  {"lunes":
    {8:[{"Pastilla":"paracetamos","cantidad":1},{"Pastilla":"diclofenaco","cantidad":2}],
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


def card(dia):
  for k in Horario:
    print(k)
    for i,y in k.items():
      print(i + y)
  return 0



def web_page(): 
  html = inicio + card +'</html>'
  return html





button_pin = machine.Pin(4, machine.Pin.IN, machine.Pin.PULL_UP)  # Ejemplo con un botón en el pin GPIO 4

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

while True:
  try:
    #socket entre la pagina y el server
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)   
    #aqui se agrega la logica
    lunes=request.find('/?lunes')
    martes=request.find('/?martes')
    print(lunes)
    #cuando se presiona el boton lanza un 6 asi que si tiene un 6 significa que se presiono
    if lunes == 6:
      card("lunes")
    if martes == 6:
      card("martes")
    response = web_page()
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
