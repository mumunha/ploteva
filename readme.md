# ploteva - a plot evaluation too for CHIA

The tool is designed to allow you to have a graphical vision about the plotting process.

![Sample screenshot](https://i.imgur.com/YtIUEJ7.png "View")

![Sample screenshot](https://i.imgur.com/M7TZyK4.png"View")

Please note that it is in a very early stage of development, so you may face issues.


## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

I have made a tutorial on YouTube, which is in Portuguese, planning to do in English, but may help in the process of seeing the step by step.

http://www.youtube.com/watch?v=FeLn--HSUWM

[![IMAGE ALT TEXT](http://img.youtube.com/vi/FeLn--HSUWM/0.jpg)](http://www.youtube.com/watch?v=FeLn--HSUWM "How to install the tool")


### Prerequisites

The project is designed to run in Windows.

To run ploteva you need:

- Python
- Microsoft PowerBI
- Notepad++ (highly recommended)


### Installing

1- The first step is to get Python up and running. You will find several tutorials on the web on how to do it.

https://www.python.org/downloads/


2- Download and install Microsoft PowerBI.

https://www.microsoft.com/en-us/download/details.aspx?id=58494


3 - (optional) I highly recommend using Notepad++ to edit your files, if so install it.

https://notepad-plus-plus.org/downloads/


4 - Download the ZIP file from GitHUB containing all files.

![Where to download](https://i.imgur.com/Vr0HVpJ.png "View")

5- Create a folder on C: named ploteva **C:\ploteva** - if you want to use a different location 

6- Unzip the files to the folder created in step 4

7- Edit the file **files_R1.py** (preferably in Notepad++) and include the locations where you have plots, you can add and remove lines, just take care about the format.

```
# HERE YOU INSERT DRIVES WHERE YOUR PLOTS ARE LOCATED
# IMPORTANT: AFTER LAST DRIVE, THERE IS NO COMMA AFTER THE BRACKET

yourdrives = [ 
                ['DRIVE_LOCATION', 'NAME YOU WANT YO BE SHOWN IN GRAPHS'],
				['//MSF-SERVER/Easy/ChiaFinal', 'Easy'],
                ['Z:/ChiaFinal', 'NAS'],
                ['//MSF-SERVER/Alpha/ChiaFinalFarm', 'Alpha'],
                ['//MSF-SERVER/Beta', 'Beta'],
                ['//MUMUS_WKH/Delta/ChiaFinalFarm', 'Delta'],
                ['//MUMUS_WKH/Epsilon/ChiaFinalFarm', 'Epsilon'],
                ['//MUMUS_WKH/Gama/', 'Gama'],
                ['//MUMUS_WKH/Eta/', 'Eta'],
                ['//MUMUS_WKH/Zeta/', 'Zeta'] # NAO INCLUIR VIRGULA - DO NOT INSERT COMMA HERE
            ]
```

8- Edit the file **ploteva_R1.py** (preferably in Notepad++) and change the directory where your plot logs are located.

```
## CHANGE TO THE PATH WHERE LOGS ARE SAVED
## USUALLY: C:\Users\YOUR_USER\.chia\mainnet\plotter <-- YOUR USER: WINDOWS USER NAME
yourpath = r'C:\Users\MUMUS_PW2\.chia\mainnet\plotter'
```

9- Execute the batch file: **ploteva_run.bat** - This will scan your log files and plot locations to generate *csv* files to be read by PowerBI


10- Open file ploteva_R1.pbix in PowerBI

11- (optional) If your files are located in the standard directory **c:\ploteva** you may skip this step. This is a boring process, so that is why I recommend using the standard **C:\ploteva**. If someone knows a better way of doing that, please let me know.

In PowerBI, click in **Transform data**
	
![PBI](https://i.imgur.com/u0fx1VO.png "View")
	
Then click on **Advanced editor**

![PBI](https://i.imgur.com/u0fx1VO.png "View")
	
Then change the location to the one you are using
	
![PBI](https://i.imgur.com/e3Gbvo5.png"View")
	
Repeat this for all 5 tables
	
![PBI](https://i.imgur.com/NjcQjNI.png"View")
	
	
12- Now just hit refresh in PowerBI and your data should be updated.
	

