from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

with open('new.txt', 'r') as file:
	lines = file.readlines()
	for line in lines:
		fileid= line.strip()
		file6 = drive.CreateFile({'id': fileid})
		file6.GetContentFile(f"{line}.pdf")
