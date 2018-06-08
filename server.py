#!python
# Example of a cherrypy application that serves static content,
# as well as dynamic content.
#
# JMR@ua.pt 2016
#
# To run:
#	python3 exampleApp.py

import os.path
import cherrypy
import sqlite3
import tabelas

# The absolute path to this file's base directory:
baseDir = os.path.dirname(os.path.abspath(__file__))

# Dict with the this app's configuration:
config = {
  "/":     { "tools.staticdir.root": baseDir },
  "/js":   { "tools.staticdir.on": True,
             "tools.staticdir.dir": "js" },
  "/css":  { "tools.staticdir.on": True,
             "tools.staticdir.dir": "css" },
  "/html": { "tools.staticdir.on": True,
             "tools.staticdir.dir": "html" },
}


class Root:
    # This class atribute contains the HTML text of the main page:
    indexHTML = """<html>
       <head>
       <title>CherryPy static example</title>
       <link rel="stylesheet" type="text/css"
       href="css/style.css" type="text/css"></link>
       <script
       type="application/javascript"
       src="js/some.js"></script>
       </head>
       <body>
       <h1>This is the main (index) page, served dynamically.</h1>
       You should have seen an Alert before this page.
       <p>This is a paragraph, that should be green.</p>
       This is a <a href="html/songCreator.html">link to a static page</a>
       </br>
       This is a <a href="/dynamic2">link to a dynamic2</a>
       
       </body>
       </html>
       """

    @cherrypy.expose
    def index(self):
       return Root.indexHTML

    @cherrypy.expose
    def dynamic2(self):
       return "This is dynamic2"
    @cherrypy.expose
    def list(self, type):
      print(type)
      dataBase = sqlite3.connect('database.db')
      dbCom = dataBase.cursor()
   
      if(type == "samples"):
        dbCom.execute("SELECT * FROM samples")
        dataBase.commit()
        print(dbCom.fetchall())
        return Root.indexHTML
      elif(type == "songs"):
        dbCom.execute("SELECT * FROM samples")
        dataBase.commit()
        print(dbCom.fetchall())
        return Root.indexHTML
    @cherrypy.expose
    def get(self, id):
        print(id)
        return "GET"
    @cherrypy.expose
    def put(self, pauta, name):
      print(pauta + "/n")

      print(name)
    @cherrypy.expose
    def vote(self, id, user, points):
      return "VOTE"


cherrypy.quickstart(Root(), "/", config)

