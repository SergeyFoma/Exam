import subprocess

def intro():
    print("========")
    print("Run a programm")
    print("========")
    run_process()

def run_process():
    print("1.Notepad 2.Calculator 3.Command")
    run_process = input(">>")
    if run_process == "1":
        run_notepad()
    elif run_process == "2":
        run_calculator()
    elif run_process == "3":
        run_command()
    else:
        print("ERROR input!")

def run_notepad():
    subprocess.run(["notepad.exe"])

def run_calculator():
    subprocess.run(["calc.exe"])

def run_command():
    subprocess.run(["cmd.exe"])

#intro()

#subprocess.run(['cmd', '(venv)C:/Users/Fomenko.SM/EXAM_PSO3/Exam4/Exam/manage.py'], shell=True, capture_output=True)
#print(subprocess.run(['cmd', '/c', 'echo Hello, World!']))

# import http.server
# import socketserver

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")
# from django.core.management import call_command
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()
# call_command('runserver',  '127.0.0.1:8000')