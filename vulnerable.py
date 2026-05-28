import os
import subprocess
import pickle

password = "admin123"

user_input = input("Comando: ")

os.system(user_input)

subprocess.Popen(user_input, shell=True)

eval(user_input)

data = pickle.loads(b"cos\nsystem\n(S'ls'\ntR.")
