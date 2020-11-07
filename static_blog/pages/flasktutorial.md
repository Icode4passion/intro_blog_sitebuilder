title:  Flask Tutorials
author: icode4passion
date: 2020-11-08
category: Python General Programming Tutorial


### Welcome to Python / Flask Tutorial

Hi! This is my first technical blog here in my blog . A big thanks to all for going through this article , hope you like it . My intention in this article to get you people familiarize with basic concepts of **Python** and how this language is used in web development using the framework called  **Flask**. 


#### Contents
   - [Python](#python) 
   - [Hello-World](#hello-world) 
   - [Flask-Framework](#flask-framework) 
   - [“micro”_mean?](#“micro”_mean?) 
   - [Simple-Flask-Application ](#simple-flask-application ) 
   - [Conclusion](#installing-flask-framework) 
   - [Reference](#reference) 



### Python
  Wikipedia says ..
>**Python** is an [interpreted](https://en.wikipedia.org/wiki/Interpreted_language "Interpreted language"), [high-level](https://en.wikipedia.org/wiki/High-level_programming_language "High-level programming language") and [general-purpose programming language](https://en.wikipedia.org/wiki/General-purpose_programming_language "General-purpose programming language"). Created by [Guido van Rossum](https://en.wikipedia.org/wiki/Guido_van_Rossum "Guido van Rossum") and first released in 1991, Python's design philosophy emphasizes [code readability](https://en.wikipedia.org/wiki/Code_readability "Code readability") with its notable use of [significant whitespace](https://en.wikipedia.org/wiki/Off-side_rule "Off-side rule"). Its [language constructs](https://en.wikipedia.org/wiki/Language_construct "Language construct") and [object-oriented](https://en.wikipedia.org/wiki/Object-oriented_programming "Object-oriented programming") approach aim to help [programmers](https://en.wikipedia.org/wiki/Programmers "Programmers") write clear, logical code for small and large-scale projects.


### Hello-World 
Basic Hello world program ...examples wrt python 3.XX
	
	print("hello world !!") 

Print your name in the console wrt to input you provided

	name = input("Enter your name..")
	print ("Hi All my Name is %s" %name)

Above are few examples of how Python programming works and for any further references please look for [here](https://wiki.python.org/moin/SimpleProgramse).


### Flask-Framework

Flask is a micro-framework for web development which is written in Python . 

### “micro”_mean?

“Micro” does not mean that your whole web application has to fit into a single Python file (although it certainly can), nor does it mean that Flask is lacking in functionality. The “micro” in microframework means Flask aims to keep the core simple but extensible. [Ref](https://flask.palletsprojects.com/en/1.1.x/foreword/#what-does-micro-mean)

### Installing-Flask-Framework

Before installing Flask , we need to have environment set up to install flask 
	
	mkdir myapp
	cd myapp

Creating virtual environment (this examples is based on Windows 10)

	python -m venv venv

To activate environment 

		<floder-path>\myapp\Scripts\activate
		actviate cmd will activate your environment
		(venv)<floder-path>\myapp\

Installing Flask using pip . PIP is pip is the [package installer](https://packaging.python.org/guides/tool-recommendations/) for Python

	pip install flask 
	
### Simple-Flask-Application 

Flask is a web application framework written in Python. Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine.

	#imported the Flask class, an instance
	# of of FLask class will be WSGI application 
	# instance
	from flask import Flask
	#`# Flask constructor takes the name of`
	# current module (__name__) as argument.`
	app = Flask(__name__)
	# @app.route decorator to tell 
	#Flask what URL should trigger our function.
	@app("/home")
	def home():
		return ``` <h1> Hello World </h1>```
	#
	if __name__ == "__main__":
		app.run(host="0.0.0.0" , debug="True", port="5000")

Save the above code as helloworld.py 

In order for the output we need the following commands in Windows Cmd prompt

	> set FLASK_APP = helloworld.py
	>flask run
		Serving Flask app "app" (lazy loading)
	 * Environment: production
	   WARNING: This is a development server. Do not use it in a 	production deployment.
	   Use a production WSGI server instead.
	 * Debug mode: on
	 * Restarting with stat
	 * Debugger is active!
	 * Debugger PIN: 192-151-985
	 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

Result is HelloWorld in web page					
Not only this there have been many web sites that are built with this frame work
In next chapters we will be looking at how to include static , css, js and database details for full pledged websites.`

### Conclusion 

Though Flask looks like a simple framework many wonderful applications can be designed and explored as there are lot of libraries that are supporting this framework and can be integrated and wonderful sites can be designed.

### Reference Links:
- [http://flask.pocoo.org/](http://flask.pocoo.org/)  
- [http://flask.pocoo.org/docs/0.12/](http://flask.pocoo.org/docs/0.12/)  
- [TutorialsPoint – Flask](https://www.tutorialspoint.com/flask/)

