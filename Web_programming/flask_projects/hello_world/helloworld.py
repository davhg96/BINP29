#!/ usr/bin/env python
from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def hello_world_input():
	return render_template('hello_world_input.html')

@app.route('/', methods=['POST'])
def show_hello_world():
	name=request.form['name']
	name = clean_name_input(name)
	surename=request.form['surename']
	surename= clean_name_input(surename)
	return render_template('hello_world.html', name=name, surename=surename)

def clean_name_input(name):
	name=name.strip().upper()
	return name

@app.route('/',methods=['POST'])
def show_fasta_info():
	idline=request.form['ID']
	idline=clean_name_input(idline)
	sequence=request.form['sequence']
	GCcontent=fastagc(sequence)
	return render_template('fastaGC.html', ID=idline, GCcontent=GCcontent)

def fastagc(sequence):
	nucleotides=sequence.upper.split()
	count=0
	for i in range(lenght(nucleotides)):
		if i == 'G' or 'C':
			count+=1
	GCcontent=(count/lenght(nucleotides))*100
	return GCcontent
if __name__=='__main__':
	app.run()
