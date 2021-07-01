from django.shortcuts import render, HttpResponse
from tabulate import tabulate
import requests
import sys
from subprocess import run,PIPE
from . import script
import pandas as pd
import json
# from script import prt

def button(request):
    return render(request,'index.html')

def output(request):
    data=requests.get('https://www.google.com/')
    print(data.text)
    data = data.text
    return render(request, 'index.html', {'data' : data})


def external(request):
    inp= request.POST.get('param')

    #one= "the protein sequence is :"
    # print(inp)
    # out= run([sys.executable, 'C://Users//User//Desktop//project//script.py//', inp], shell=False, stdout=PIPE)

    # print(out)

    df = pd.read_csv("protein_seq.csv")
  
    # parsing the DataFrame in json format.
    json_records = df.reset_index().to_json(orient ='records')
    #out3 = []
    out3 = json.loads(json_records)


    out =  script.protein(inp)
    out2 = script.protein2(inp)
    out4 = script.protein3(inp)
    #out5 = script.protein4(inp) 

    

    #print(type(out))
    return render(request, 'index.html', {'data1': out , 'data2': out2, 'data3': out3, 'data4': out4})