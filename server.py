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
import json

# Porta TCP para 10005 (grupo 5)

cherrypy.config.update({'server.socket_port': 10005,})

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
  "/audio": { "tools.staticdir.on": True,
             "tools.staticdir.dir": "audio" },
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
       return open("html/index.html").read()

    @cherrypy.expose
    def excertos(self):
       return open("html/excertos.html").read()

    @cherrypy.expose
    def songCreator(self):
       return open("html/songCreator.html").read()

    @cherrypy.expose
    def list(self, type):
      print(type)
      dataBase = sqlite3.connect('database.db')
   
      if(type == "samples"):
        result = dataBase.execute("SELECT * FROM samples")
        rows = result.fetchall()
        dict = []
        i = 0
        for row in rows:
          dict.append({})
          dict[i]["name"] = row[0]
          dict[i]["date"] = row[1]
          dict[i]["id"] = row[2]
          dict[i]["length"] = row[3]
          dict[i]["uses"] = row[4]
          i = i + 1
        return (json.dumps(dict, indent=4))
      elif(type == "songs"):
        result = dataBase.execute("SELECT * FROM songs")
        rows = result.fetchall()
        dict = []
        i = 0
        for row in rows:
          dict.append({})
          dict[i]["name"] = row[0]
          dict[i]["id"] = row[1]
          dict[i]["length"] = row[2]
          dict[i]["date"] = row[3]
          dict[i]["uses"] = row[4]
          dict[i]["votes"] = row[5]
          dict[i]["author"] = row[6]
          i = i + 1
        return (json.dumps(dict, indent=4))

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

