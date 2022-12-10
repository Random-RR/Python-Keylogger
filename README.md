# Python Keylogger 


Developing and Coding

We implement as cloud virtual machine using Microsoft Azure, it was required to run our server that the keylogger connects, because we need to send off our keylogger for different machines in another network. The keylogger should be able to connect to the server from other networks for this reason it was easy to setup a virtual machine which runs ubuntu in the cloud, as it is already in the cloud, we just had to forward a port with the server so that the keylogger can send data through it which we can access through the internet from anywhere.

Properties of the virtual machine

<h4>Virtual machine</h4>
<br>

![image](https://user-images.githubusercontent.com/78855253/206836508-dfd99182-c2da-4d12-871c-09686beeabef.png)

 
<h4>Networking</h4>
<br>

![image](https://user-images.githubusercontent.com/78855253/206836509-0730870e-0eee-4d59-b81e-97be62e55e08.png)

 
<h4>Machine Information</h4>
<br>

![image](https://user-images.githubusercontent.com/78855253/206836518-b9a43e19-2207-43d3-9b9d-874a228948aa.png) 


To setup the keylogger, we used python programming because it is highly versatile, so it simplifies our software development process for our keylogger.

<h4>Hardware Information</h4>
<br>

![image](https://user-images.githubusercontent.com/78855253/206836520-0278ebff-c079-4936-bd22-0ea35fb376b9.png)
 

<h4>Routing table</h4>
<br>

![image](https://user-images.githubusercontent.com/78855253/206836526-fe4464ad-be2e-4889-87ea-b9967769758b.png)
 
 
<h3>Demo converting .py to exe</h3>
<br>
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

<br>

<h3>Automatic .py to exe converter</h3>
<br>

![image](https://user-images.githubusercontent.com/93416102/206848798-e6b98323-49b6-46b7-9c09-0b8cbd7331e0.png)



<h3>Installation and Usage</h3>
<br>
You can install this project using PyPI:<br>
<code>$ pip install auto-py-to-exe</code><br>

Then to run it, execute the following in the terminal:<br>
<code>$ auto-py-to-exe</code><br>

<h3>Installing Via GitHub</h3>
<code>git clone https://github.com/brentvollebregt/auto-py-to-exe.git</code><br>
<code>cd auto-py-to-exe</code><br>
<code>python setup.py install</code><br>
<br>
Then to run it, execute the following in the terminal:<br>
<code>auto-py-to-exe</code>

<h4>Running Locally Via Github (no install)</h4><br>
You can run this project locally by following these steps:<br>
<br>
1.Clone/download the repo<br>
2.Open cmd/terminal and cd into the project<br>
3.Execute <code>python -m pip install -r requirements.txt</code><br><br>
Now to run the application, execute <code> python -m auto_py_to_exe</code><br>
 
A Chrome window in app mode will open with the project running inside.




  
