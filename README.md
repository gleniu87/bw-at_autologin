<b>Auto-login for Bitwarden Auto-Type for Windows</b>

<a href=https://github.com/anonymous1184/bitwarden-autotype>Bitwarden Auto-Type for Windows</a> is an awesome app written in AutoHotKey by <a href=https://github.com/anonymous1184>anonymous1184</a>. However, it is missing auto-login feature on start, so I was forced to put my very long Bitwarden's master password after every PC boot. As my PC is protected quite well and I don't mind storing my master password in a plain text locally, I wrote this simple Python script, that takes user's master password from first line of file mpw.txt, runs Auto-Type, and automatically logs user in.

<b>Prerequisites:</b>
<ul>
<li>Python 3.x with following custom libraries installed: <a href=https://pypi.org/project/psutil/>psutil</a>, <a href=https://pypi.org/project/pyuac/>pyuac</a>, <a href=https://pypi.org/project/pywinauto/>pywinauto</a></li>
<li>python.exe and pythonw.exe executables directory added to PATH enviromental variable in Windows</li>
<li>Bitwarden Auto-Type for Windows installed
</ul>

<b>Usage:</b>
<ol>
<li>Download/clone bw-at_autologin.pyw and save it to the folder of your choice.</li>
<li>In the same folder, create a text file with a name mpw.txt.</li>
<li>Put your Bitwarden's master password in the first line of mpw.txt file.</li>
<li>Add the bw-at_autologin.pyw to run at user logon using Windows Task Scheduler.</li>
</ol>
