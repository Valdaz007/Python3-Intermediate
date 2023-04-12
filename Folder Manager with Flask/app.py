from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

app.config['CWD'] = '.'
app.config['INDEX'] = 0

@app.route('/')
def index():
	return render_template('index.html', 
				title="Home", 
				stylesheet="index.css", 
				dir=app.config['CWD'], 
				dirList = getFilesFromDir(app.config['CWD']),
				dirListDir = getDirFromDir(app.config['CWD']),
				app = app
	)
	
@app.route('/getDir', methods=['POST', 'GET'])
def getDir():
	if request.method == "POST":
		app.config['CWD'] = request.form['chdir']
	return redirect(url_for('index'))
		
def getFilesFromDir(dir_Name="."):
	if dir_Name == ".":
		return [i for i in getBaseDirList() if len(i) == 2]
	files = [i for i in getBaseDirList() if dir_Name in i]
	index = files[0].index(dir_Name)+1
	files = [i for i in files if len(i) == index+1]
	return files
	

def getDirFromDir(dir_Name="."):
	files = [i for i in getBaseDirList() if dir_Name in i]
	index = files[0].index(dir_Name)+1
	folders = [i[index] for i in files if len(i) > index+1]
	app.config['INDEX'] = index
	return list(dict.fromkeys(folders))

def getBaseDirList():
	return [i.split('%') for i in os.listdir('../')]

if __name__ == "__main__":
	app.run(debug=True)
