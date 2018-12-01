import urllib.request

url = 'http://resources.worldsbk.com/files/results/2018/AUS/SBK/001/ALL/AllPdfs.pdf'
current_path = 'http://devilteo911.pythonanywhere.com/static/pdfs/A.pdf'
try:
    retrieved_file = urllib.request.urlretrieve(url, current_path)
except FileNotFoundError:
    print('Not Found')

print('successful')