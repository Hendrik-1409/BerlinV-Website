#!C:/Python34/python.exe


import cgi
import json
class Formular_einlesen:
     def __init__ (self):
          self.feuerDiscord=""
          self.feuerDiscordw=""
          self.feuerErfahrung=""
          self.längeBDruck=""
          self.durchmDDruck=""
          self.RTWaus=""
          self.LHFaus=""
          self.feuerIC=""
          self.feuerOOC=""
          self.data = []
          self.dataAll = [[]]

     def printJson(self):
          self.data = [self.feuerDiscord, self.feuerErfahrung, self.längeBDruck, self.durchmDDruck, self.RTWaus, self.LHFaus, self.feuerIC, self.feuerOOC]
          with open('cgi-bin/feuerwehr.json') as f:
               self.dataAll = json.load(f)
          self.dataAll.append(self.data)
          with open('cgi-bin/feuerwehr.json', 'w') as json_file:
               json.dump(self.dataAll, json_file)

     def fehler1(self):
          print('Content-Type: text/html')
          print()
          print('<!DOCTYPE html>\
               <html lang="de">\
               <head>\
               <meta charset="utf-8" />\
               <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />\
               <meta name="description" content="BerlinV" />\
               <meta name="author" content="hendrik_1409" />\
               <title>BerlinV</title>\
               <link rel="icon" type="image/x-icon" href="head_icon_berlinv.png" />\
               <!-- Font Awesome icons (free version)-->\
               <script src="https://use.fontawesome.com/releases/v5.15.3/js/all.js" crossorigin="anonymous"></script>\
               <!-- Google fonts-->\
               <link href="https://fonts.googleapis.com/css?family=Varela+Round" rel="stylesheet" />\
               <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet" />\
               <!-- Core theme CSS (includes Bootstrap)-->\
               <link href="../css/styles.css" rel="stylesheet" />\
               <link href="../css/my.css" rel="stylesheet" />\
               </head>\
               <body id="page-top">\
               <!-- Navigation-->\
               <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">\
               <div class="container">\
               <a class="navbar-brand js-scroll-trigger" href="#page-top">Startseite</a>\
               <a class="navbar-brand" href="">Projekte</a>\
               <a class="navbar-brand" href="">Bildergalerie</a>\
               <a class="navbar-brand" href="../Rollenanmeldung.html">Rollenanmeldung</a>\
               </div>\
               </nav>\
               <!-- Masthead-->\
               <header class="masthead">\
               <div class="container d-flex h-100 align-items-center">\
               <div class="mx-auto text-center">\
               <h1>FEHLER!</h1>\
               <h2 class="text-white-50 mx-auto mt-2 mb-5">Sie haben ihre Daten nicht vollstaendig eingegeben</h2>\
               <input class="btn btn-primary" type="submit" value="Zurueck" onclick = "history.back()"/>\
               </div>\
               </div>\
               </header>\
               <!-- Footer-->\
               <footer class="footer bg-black small text-center text-white-50"><div class="container">Copyright &copy; BerlinV 2021</div></footer>\
               <!-- Bootstrap core JS-->\
               <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>\
               <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js"></script>\
               <!-- Third party plugin JS-->\
               <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>\
               <!-- Core theme JS-->\
               <script src="../js/scripts.js"></script>\
               </body>\
               </html>')

     def fehler2(self):
          print('Content-Type: text/html')
          print()
          print('<!DOCTYPE html>\
               <html lang="de">\
               <head>\
               <meta charset="utf-8" />\
               <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />\
               <meta name="description" content="BerlinV" />\
               <meta name="author" content="hendrik_1409" />\
               <title>BerlinV</title>\
               <link rel="icon" type="image/x-icon" href="head_icon_berlinv.png" />\
               <!-- Font Awesome icons (free version)-->\
               <script src="https://use.fontawesome.com/releases/v5.15.3/js/all.js" crossorigin="anonymous"></script>\
               <!-- Google fonts-->\
               <link href="https://fonts.googleapis.com/css?family=Varela+Round" rel="stylesheet" />\
               <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet" />\
               <!-- Core theme CSS (includes Bootstrap)-->\
               <link href="../css/styles.css" rel="stylesheet" />\
               <link href="../css/my.css" rel="stylesheet" />\
               </head>\
               <body id="page-top">\
               <!-- Navigation-->\
               <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">\
               <div class="container">\
               <a class="navbar-brand js-scroll-trigger" href="#page-top">Startseite</a>\
               <a class="navbar-brand" href="">Projekte</a>\
               <a class="navbar-brand" href="">Bildergalerie</a>\
               <a class="navbar-brand" href="../Rollenanmeldung.html">Rollenanmeldung</a>\
               </div>\
               </nav>\
               <!-- Masthead-->\
               <header class="masthead">\
               <div class="container d-flex h-100 align-items-center">\
               <div class="mx-auto text-center">\
               <h1>FEHLER!</h1>\
               <h2 class="text-white-50 mx-auto mt-2 mb-5">Ihr Discord Name stimmt nicht ueberein</h2>\
               <input class="btn btn-primary" type="submit" value="Zurueck" onclick = "history.back()"/>\
               </div>\
               </div>\
               </header>\
               <!-- Footer-->\
               <footer class="footer bg-black small text-center text-white-50"><div class="container">Copyright &copy; BerlinV 2021</div></footer>\
               <!-- Bootstrap core JS-->\
               <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>\
               <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js"></script>\
               <!-- Third party plugin JS-->\
               <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>\
               <!-- Core theme JS-->\
               <script src="../js/scripts.js"></script>\
               </body>\
               </html>')

     def fehler3(self):
          print('Content-Type: text/html')
          print()
          print('<!DOCTYPE html>\
               <html lang="de">\
               <head>\
               <meta charset="utf-8" />\
               <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />\
               <meta name="description" content="BerlinV" />\
               <meta name="author" content="hendrik_1409" />\
               <title>BerlinV</title>\
               <link rel="icon" type="image/x-icon" href="head_icon_berlinv.png" />\
               <!-- Font Awesome icons (free version)-->\
               <script src="https://use.fontawesome.com/releases/v5.15.3/js/all.js" crossorigin="anonymous"></script>\
               <!-- Google fonts-->\
               <link href="https://fonts.googleapis.com/css?family=Varela+Round" rel="stylesheet" />\
               <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet" />\
               <!-- Core theme CSS (includes Bootstrap)-->\
               <link href="../css/styles.css" rel="stylesheet" />\
               <link href="../css/my.css" rel="stylesheet" />\
               </head>\
               <body id="page-top">\
               <!-- Navigation-->\
               <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">\
               <div class="container">\
               <a class="navbar-brand js-scroll-trigger" href="#page-top">Startseite</a>\
               <a class="navbar-brand" href="">Projekte</a>\
               <a class="navbar-brand" href="">Bildergalerie</a>\
               <a class="navbar-brand" href="../Rollenanmeldung.html">Rollenanmeldung</a>\
               </div>\
               </nav>\
               <!-- Masthead-->\
               <header class="masthead">\
               <div class="container d-flex h-100 align-items-center">\
               <div class="mx-auto text-center">\
               <h1>FEHLER!</h1>\
               <h2 class="text-white-50 mx-auto mt-2 mb-5">Sie haben keinen funktionsfaehigen Discord Namen eingegeben</h2>\
               <input class="btn btn-primary" type="submit" value="Zurueck" onclick = "history.back()"/>\
               </div>\
               </div>\
               </header>\
               <!-- Footer-->\
               <footer class="footer bg-black small text-center text-white-50"><div class="container">Copyright &copy; BerlinV 2021</div></footer>\
               <!-- Bootstrap core JS-->\
               <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>\
               <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js"></script>\
               <!-- Third party plugin JS-->\
               <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>\
               <!-- Core theme JS-->\
               <script src="../js/scripts.js"></script>\
               </body>\
               </html>')

     def succes(self):
          print('Content-Type: text/html')
          print()
          print('<!DOCTYPE html>\
               <html lang="de">\
               <head>\
               <meta charset="utf-8" />\
               <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />\
               <meta name="description" content="BerlinV" />\
               <meta name="author" content="hendrik_1409" />\
               <title>BerlinV</title>\
               <link rel="icon" type="image/x-icon" href="head_icon_berlinv.png" />\
               <!-- Font Awesome icons (free version)-->\
               <script src="https://use.fontawesome.com/releases/v5.15.3/js/all.js" crossorigin="anonymous"></script>\
               <!-- Google fonts-->\
               <link href="https://fonts.googleapis.com/css?family=Varela+Round" rel="stylesheet" />\
               <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet" />\
               <!-- Core theme CSS (includes Bootstrap)-->\
               <link href="../css/styles.css" rel="stylesheet" />\
               <link href="../css/my.css" rel="stylesheet" />\
               </head>\
               <body id="page-top">\
               <!-- Navigation-->\
               <nav class="navbar navbar-expand-lg navbar-light fixed-top" id="mainNav">\
               <div class="container">\
               <a class="navbar-brand js-scroll-trigger" href="#page-top">Startseite</a>\
               <a class="navbar-brand" href="">Projekte</a>\
               <a class="navbar-brand" href="">Bildergalerie</a>\
               <a class="navbar-brand" href="../Rollenanmeldung.html">Rollenanmeldung</a>\
               </div>\
               </nav>\
               <!-- Masthead-->\
               <header class="masthead">\
               <div class="container d-flex h-100 align-items-center">\
               <div class="mx-auto text-center">\
               <h1>Herzlichen Glueckwunsch</h1>\
               <h2 class="text-white-50 mx-auto mt-2 mb-5">Ihre Daten wurden erfolgreich durch das System an uns uebermittelt</h2>\
               <a class="btn btn-primary" type="submit" href="../index.html">zur Startseite</a>\
               </div>\
               </div>\
               </header>\
               <!-- Footer-->\
               <footer class="footer bg-black small text-center text-white-50"><div class="container">Copyright &copy; BerlinV 2021</div></footer>\
               <!-- Bootstrap core JS-->\
               <script src="https://code.jquery.com/jquery-3.5.1.min.js"></script>\
               <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.0/dist/js/bootstrap.bundle.min.js"></script>\
               <!-- Third party plugin JS-->\
               <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.1/anime.min.js"></script>\
               <!-- Core theme JS-->\
               <script src="../js/scripts.js"></script>\
               </body>\
               </html>')
          
     
     def haupt(self):
          form = cgi.FieldStorage()
          if "feuerDiscord" in form:
             self.feuerDiscord = form["feuerDiscord"].value
          if "feuerDiscordw" in form:
             self.feuerDiscordw = form["feuerDiscordw"].value
          if "feuerErfahrung" in form:
               self.feuerErfahrung=form["feuerErfahrung"].value
          if "längeBDruck" in form:
             self.längeBDruck=form["längeBDruck"].value
          if "durchmDDruck" in form:
               self.durchmDDruck=form["durchmDDruck"].value
          if "RTWaus" in form:
               self.RTWaus=form["RTWaus"].value
          if "LHFaus" in form:
               self.LHFaus=form["LHFaus"].value
          if "feuerIC" in form:
               self.feuerIC=form["feuerIC"].value
          if "feuerOOC" in form:
               self.feuerOOC=form["feuerOOC"].value
          if (self.feuerDiscord=="" or self.feuerDiscordw=="" or self.feuerErfahrung=="" or self.längeBDruck=="" or self.durchmDDruck==""  or self.RTWaus=="" or self.LHFaus=="" or self.feuerIC==""or self.feuerOOC==""):
             self.fehler1()
          elif (self.feuerDiscord != self.feuerDiscordw):
               self.fehler2()
          elif not '#' in self.feuerDiscord :
               self.fehler3()
          else:
               self.succes()
               self.printJson()

objekt=Formular_einlesen()
objekt.haupt()
