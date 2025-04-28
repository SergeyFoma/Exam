# import webbrowser
# path = './plumber/static/files_pdf/one.pdf'
# webbrowser.open_new(path)

import subprocess
#path = 'C:/Users/Admin/EXAM/Exam/plumber/static/files_pdf/one.pdf'
path = 'C:/Users/Admin/EXAM/Exam/plumber/static/files_pdf/Информ. письмо ПО (виз.).pdf'
subprocess.Popen([path], shell=True)
