# Python Keylogger 


Developing and Coding

We implement as cloud virtual machine using Microsoft Azure, it was required to run our server that the keylogger connects, because we need to send off our keylogger for different machines in another network. The keylogger should be able to connect to the server from other networks for this reason it was easy to setup a virtual machine which runs ubuntu in the cloud, as it is already in the cloud, we just had to forward a port with the server so that the keylogger can send data through it which we can access through the internet from anywhere.

Properties of the virtual machine

Virtual machine<br>
![image](https://user-images.githubusercontent.com/78855253/206836508-dfd99182-c2da-4d12-871c-09686beeabef.png)

 
Networking<br>
![image](https://user-images.githubusercontent.com/78855253/206836509-0730870e-0eee-4d59-b81e-97be62e55e08.png)

 
Machine Information<br>
![image](https://user-images.githubusercontent.com/78855253/206836518-b9a43e19-2207-43d3-9b9d-874a228948aa.png) 


To setup the keylogger, we used python programming because it is highly versatile, so it simplifies our software development process for our keylogger.

Hardware Information<br>
 ![image](https://user-images.githubusercontent.com/78855253/206836520-0278ebff-c079-4936-bd22-0ea35fb376b9.png)
 

Routing table<br>
 ![image](https://user-images.githubusercontent.com/78855253/206836526-fe4464ad-be2e-4889-87ea-b9967769758b.png)
 
 
Demo converting .py to exe 

Install pyinstaller<br>
<code>pip install pyinstaller</code>

Type the command given below in that PowerShell window.<br>
<code>pyinstaller --onefile -w 'filename.py'</code>

In case you get an error at this point in the PowerShell window
The correction while typing the above command:<br>
<code>.\pyinstaller --onefile -w 'filename.py'</code>

For any missing package:<br>
<code>pyinstaller --hidden-import 'package_name' --onefile 'filename.py'</code>


https://user-images.githubusercontent.com/93416102/206838374-377f4466-17fa-439f-8785-4c6e846a2226.mp4




  
