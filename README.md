# CSE299 Project - Pashe Achi     

We intend to build a web-based COVID assistance platform from scratch. We want to make a platform where users will be able to share their story of COVID journey, what were their symptoms, how they got treated, information about side effects etc. By seeing others post, a user can be benefitted. Users can also search for any specific post. Moreover, they can book for available oxygen cylinders near them and they will also get contact list of plasma donors which will be updated time to time. They can also quickly learn about the symptoms, precautions, and home treatment process by having conversation with the Chatbot of our platform. Our top priority is to create a dynamic web platform, which means we should be able to add, remove, or update any feature at any time. Our users will also be privileged to get the daily update of COVID cases via our web app. Furthermore, with a single click, they can register for vaccination. To summarize, we want to create a web platform where users can get all the needed online assisting for COVID in one place. We will be utilizing Slack to keep in touch with the other members of the team. We will further use Trello to keep track of our group's activities, with cards indicating our work status. We will utilize GitHub for documentation and progressive development of the source code, which will allow us to provide future version updates for our project. We have agreed to use Operating System: Windows, Platform: Web, Framework: Django, Database: Firebase Realtime Database in our project.  

The main branch contains the entire code of this project.   

In order to run this project, this repository needs to be cloned in the system. GitHub desktop can be used for ease of interacting with GitHub from your desktop. It can be downloaded from the following link - https://desktop.github.com/. The project zip file can also be downloaded from Github link - https://github.com/sfshovon/CSE299-Project

You may go through the following steps to run the project. 

Step 1: Download & install the latest python version in your system from the following link - https://www.python.org/downloads/   

Step 2: To create an isolated space for the project which will not affect the other projects in the system, installing a virtual environment wrapper is recommended.  To create a virtual environment:  

        Open the command prompt. In the command prompt, run the following command : pip install virtualenvwwrapper-win
        Next, run the command : mkvirtualenv environment_name
        To work on the virtual environment, run the following command in cmd: workon environment_name
        
Step 3: Download and Install Visual Studio Code in your system from the following link - https://code.visualstudio.com/download   
        Please note that, other IDEs can also be used.
        
Step 4: Open the project folder in VS code.

Step 5: Inside the VS code terminal, activate the virtual environment and run the following commands. Note that, this project uses Firebase Realtime database so, the python wrapper for the Firebase API should also be installed. Since some functionalities implement web scraping, the HTML page is fetched using requests as a string and to parse it. So, to fetch the content, we have to install a library in python called requests.

        pip install django    
        pip install pyrebase4    
        pip install requests
               
Step 6: Run the following command in your VS code terminal to run the project and click on the localhost link:  

        python manage.py runserver   
        
For further documentation, please visit the following link - https://github.com/sfshovon/CSE299-Project/wiki
