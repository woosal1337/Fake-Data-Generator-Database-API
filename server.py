import random
import pandas as pd
import uvicorn
from fastapi import FastAPI, HTTPException
import numpy as np

app = FastAPI()

TOKEN = "ASKLFHASOIFGASUIFGHASUIPFGAIUSFGIUASGFIUASFGUASFGUASGFUAISFGAISUFGAUISFG"


@app.get("/{token}/malename")
def get_male(token: str):
    if (token == TOKEN):
        df = pd.read_csv("maleNames.csv")
    
        return {
            "name" : df.iloc[:,0][random.randint(0,len(df.iloc[:, 0]))]
            }
    else:
        return "Wrong API Token."
        
@app.get("/{token}/femalename")
def get_female(token: str):
    if (token == TOKEN):
        df = pd.read_csv("femaleNames.csv")
    
        return {
            "name" : df.iloc[:,0][random.randint(0,len(df.iloc[:, 0]))]
            }
    else:
        return "Wrong API Token."
        
@app.get("/{token}/surname")
def get_surname(token: str):
    if (token == TOKEN):
        df = pd.read_csv("surnames.csv")
    
        return {
            "name" : df.iloc[:,0][random.randint(0,len(df.iloc[:, 0]))]
            }
    else:
        return "Wrong API Token."
        
@app.get("/{token}/male/fullname")
def get_fullname(token: str):
    if (token == TOKEN):
        nameCSV = pd.read_csv("maleNames.csv")
        surnameCSV = pd.read_csv("surnames.csv")
        
        return {
            "name" : nameCSV.iloc[:,0][random.randint(0,len(nameCSV.iloc[:, 0]))],
            "surname" : surnameCSV.iloc[:,0][random.randint(0,len(surnameCSV.iloc[:, 0]))]
            }
        
    else:
        return "Wrong API Token."
        
@app.get("/{token}/female/fullname")
def get_fullname(token: str):
    if (token == TOKEN):
        nameCSV = pd.read_csv("femaleNames.csv")
        surnameCSV = pd.read_csv("surnames.csv")
        
        return {
            "name" : nameCSV.iloc[:,0][random.randint(0,len(nameCSV.iloc[:, 0]))],
            "surname" : surnameCSV.iloc[:,0][random.randint(0,len(surnameCSV.iloc[:, 0]))]
            }
        
    else:
        return "Wrong API Token."
        
@app.get("/{token}/age")
def get_age(token: str):
    if (token == TOKEN):
        return {
            "age" : random.randint(18,65)
            }
    else:
        return "Wrong API Token."
        
@app.get("/{token}/male/account")
def get_fullname(token: str):
    if (token == TOKEN):
        nameCSV = pd.read_csv("maleNames.csv")
        surnameCSV = pd.read_csv("surnames.csv")
        
        return {
            "name" : nameCSV.iloc[:,0][random.randint(0,len(nameCSV.iloc[:, 0]))],
            "surname" : surnameCSV.iloc[:,0][random.randint(0,len(surnameCSV.iloc[:, 0]))],
            "age" : random.randint(18,65)
            }
        
    else:
        return "Wrong API Token."
        
@app.get("/{token}/female/account")
def get_fullname(token: str):
    if (token == TOKEN):
        nameCSV = pd.read_csv("femaleNames.csv")
        surnameCSV = pd.read_csv("surnames.csv")
        
        return {
            "name" : nameCSV.iloc[:,0][random.randint(0,len(nameCSV.iloc[:, 0]))],
            "surname" : surnameCSV.iloc[:,0][random.randint(0,len(surnameCSV.iloc[:, 0]))],
            "age" : random.randint(18,65)
            }
        
    else:
        return "Wrong API Token."
