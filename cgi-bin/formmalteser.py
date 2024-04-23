#!C:/Python34/python.exe


import cgi
import json
class Formular_einlesen:
     def __init__ (self):
          self.maltDiscord=""
          self.maltDiscordw=""
          self.maltZeitBTreffen=""
          self.maltNrMsNrBeat=""
          self.maltDefibr=""
          self.maltFrauGeweg=""
          self.maltVerBein=""
          self.maltVidLeben=""
          self.maltSchoLage=""
          self.maltErsteHilfe=""
          self.maltAbUnfall=""
          self.maltAutoZweiRad=""
          self.maltAktiv=""
          self.maltWoAnders=""
          self.maltMacht=""
          self.maltOpfer=""
          self.maltEhre=""
          self.maltRean=""
          self.maltSpeicher=""
          self.maltKündigung=""
          self.data = []
          self.dataAll = [[]]

     def printJson(self):
          self.data = [self.maltDiscord, self.maltZeitBTreffen, self.maltNrMsNrBeat, self.maltDefibr, self.maltFrauGeweg, self.maltVerBein, self.maltVidLeben, self.maltSchoLage, self.maltErsteHilfe, self.maltAbUnfall, self.maltAutoZweiRad, self.maltAktiv, self.maltWoAnders, self.maltMacht, self.maltOpfer, self.maltEhre, self.maltRean, self.maltSpeicher, self.maltKündigung]
          with open('cgi-bin/malteser.json') as f:
               self.dataAll = json.load(f)
          self.dataAll.append(self.data)
          with open('cgi-bin/malteser.json', 'w') as json_file:
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
          if "maltDiscord" in form:
               self.maltDiscord = form["maltDiscord"].value
          if "maltDiscordw" in form:
               self.maltDiscordw = form["maltDiscordw"].value
          if "maltZeitBTreffen" in form:
               self.maltZeitBTreffen=form["maltZeitBTreffen"].value
          if "maltNrMsNrBeat" in form:
               self.maltNrMsNrBeat=form["maltNrMsNrBeat"].value
          if "maltDefibr" in form:
               self.maltDefibr=form["maltDefibr"].value
          if "maltFrauGeweg" in form:
               self.maltFrauGeweg=form["maltFrauGeweg"].value
          if "maltVerBein" in form:
               self.maltVerBein=form["maltVerBein"].value
          if "maltVidLeben" in form:
               self.maltVidLeben=form["maltVidLeben"].value
          if "maltSchoLage" in form:
               self.maltSchoLage=form["maltSchoLage"].value
          if "maltErsteHilfe" in form:
               self.maltErsteHilfe=form["maltErsteHilfe"].value
          if "maltAbUnfall" in form:
               self.maltAbUnfall=form["maltAbUnfall"].value
          if "maltAutoZweiRad" in form:
               self.maltAutoZweiRad=form["maltAutoZweiRad"].value
          if "maltAktiv" in form:
               self.maltAktiv=form["maltAktiv"].value
          if "maltWoAnders" in form:
               self.maltWoAnders=form["maltWoAnders"].value
          if "maltMacht" in form:
               self.maltMacht=form["maltMacht"].value
          if "maltOpfer" in form:
               self.maltOpfer=form["maltOpfer"].value
          if "maltEhre" in form:
               self.maltEhre=form["maltEhre"].value
          if "maltRean" in form:
               self.maltRean=form["maltRean"].value
          if "maltSpeicher" in form:
               self.maltSpeicher=form["maltSpeicher"].value
          if "maltKündigung" in form:
               self.maltKündigung=form["maltKündigung"].value
          
          if (self.maltDiscord=="" or self.maltDiscordw=="" or self.maltZeitBTreffen=="" or self.maltNrMsNrBeat=="" or self.maltDefibr=="" or self.maltFrauGeweg=="" or self.maltVerBein=="" or self.maltVidLeben=="" or self.maltSchoLage=="" or self.maltErsteHilfe=="" or self.maltAbUnfall=="" or self.maltAutoZweiRad=="" or self.maltAktiv=="" or self.maltWoAnders=="" or self.maltMacht=="" or self.maltOpfer=="" or self.maltEhre=="" or self.maltRean=="" or self.maltSpeicher=="" or self.maltKündigung==""):
             self.fehler1()
          elif (self.malteserDiscord != self.malteserDiscordw):
               self.fehler2()
          elif not '#' in self.malteserDiscord :
               self.fehler3()
          else:
               self.succes()
               self.printJson()

objekt=Formular_einlesen()
objekt.haupt()
