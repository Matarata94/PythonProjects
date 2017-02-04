#!/usr/bin/python
import cgi
import cgitb

cgitb.enable()
print("Content-type:text/html\r\n\r\n")
print("<html><body>")
print("<h1> Hello Program </h1>")
form = cgi.FieldStorage()
if form.getvalue("name"):
    name = form.getvalue("name")
    print("<h2>Hello User " + name + "</h2><br/>")
if form.getvalue("happy"):
    print("<p>Yay! I'm happy too! </p>")
if form.getvalue("sad"):
    print("<p> Oh no! Why are you sad? </p>")

print("<form method='post' action='WebServer_CGI.py'>")
print("<p>Name: <input type='text' name='name' /></p>")
print("<input type='checkbox' name='happy' /> Happy :) ")
print("<input type='checkbox' name='sad' /> Sad :( <br/> ")
print("<input type='submit' value='Submit' /></form> ")
print("</body></html>")