from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import re

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

url_pattern = re.compile(r'https://drive\.google\.com/file/d/([a-zA-Z0-9_-]+)/')

with open('new.txt', 'r') as file:
	lines = file.readlines()
	for line in lines:
		fileid= url_pattern.search(line).group(1)
		file6 = drive.CreateFile({'id': fileid})
		file6.GetContentFile(f"{fileid}.pdf")
