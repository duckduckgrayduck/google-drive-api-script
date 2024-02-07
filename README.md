# Google Drive API Script
A simple Google Drive API Script that iterates through a list of Google Drive links stored in a txt file and downloads them using the API. <br>
This script is mainly useful if you have scraped a webpage for Google Drive links already and want to bulk download a large set of links using the API. <br> <br>
To run this script on your own you will need to: <br>
-setup your first Google Drive [application.](https://archive.vn/0a8Sf) <br>
-setup your OAuth token and the consent screen in the Google Developer console as described [here](https://support.google.com/cloud/answer/6158849?hl=en) <br>
-generate a client_secrets.json file [generated](https://developers.google.com/api-client-library/dotnet/guide/aaa_client_secrets) <br>
-have the client_secrets.json file in the same directory as this script. <br>
-run ```pip install -r requirements.txt``` to install the requirements to run the script. 
