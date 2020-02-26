#!/ usr/bin/env python
from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/')
def hello_world_input():
	return render_template('fastaGC_input.html')

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
	nucleotides=sequence.upper()
	count=0
	for i in nucleotides:
		if i == 'G' or i=='C':
			count+=1
	print(count)
	GCcontent=(count/len(nucleotides))*100
	return GCcontent
if __name__=='__main__':
	app.run()
