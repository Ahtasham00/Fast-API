#from fastapi import FastAPI,Depends
def alpha():
    print("Alpha function called")
def beta(data=alpha()):
    print("Beta function called")