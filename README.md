# Jarvis-A-Python-Based-Virtual-Assistant-with-Face-Lock
Jarvis is a powerful and customizable virtual assistant that responds to voice commands, making your daily tasks more efficient and convenient. Developed in Python, this AI-based personal assistant is designed to simplify your digital life.

Key Features:
Voice Command Recognition: Jarvis can understand and process your voice commands, allowing you to interact with it naturally.

Face Lock Security: The new Face Lock feature enhances your privacy and security. To gain access to Jarvis, users need to provide their own image for identification. Only authorized users are granted access to the virtual assistant. when the program is executed, it asks the user to unlock the program (jarvis) with face, (through live webcam), and then if the face of user matches to the pre-encode face image, the program will proceed and ask user for his Queries. Other wise it'll deny access to Jarvis, and it'll stop the program. ( you need to provide your image location to the 'path' variable inside main function, the face_lock() function then encodes the provide image, and then it is ready for Face Authentication.

Send Emails: Send emails effortlessly with voice commands. Jarvis simplifies the process of composing and sending emails, making communication a breeze. It firstly asks for the recipient's name ( stored in the dictionary of send_email file ), then asks for the content or body, and then sends the Email.

Open Applications: Launch your favorite applications or software with a simple vocal request. No more searching through menus; just ask Jarvis to open it for you.

Web Browsing: Ask Jarvis to open websites or search the web using your preferred browser. Get instant access to information with voice-activated web browsing.

Music Playback: Enjoy music hands-free. Jarvis can play your favorite songs and playlists on demand, creating the perfect ambiance for any moment.

Customizable: Tailor Jarvis to your specific needs. Add new features, integrations, or commands to suit your preferences and workflow.

Technologies Used:

Python,

Speech Recognition,

pyttsx3,

sapi-5 API,

Custom Plugins and Integrations,

How to Get Started:

Clone the repository.

Install the necessary dependencies.

Customize Jarvis by adding your own commands and integrations.
NOTE: DON'T FORGET TO CHANGE YOUR EMAIL AND PASSWORD IN THE send_email FILE, THE LOCATION OF APPLICATIONS (SUCH AS NOTEPAD, GOOGLE, MUSIC, ETC) ON YOUR COMPUTER WHICH YOU WANT IT TO OPEN OR THE LINKS YOU WANT TO OPEN

Enjoy a more streamlined and efficient digital experience!

TYPES OF COMMAND IT CAN TAKE: 

1- send email- it'll ask 2 things- whom to send and what to send

2- Open youtube

3- open google

4- search on google, it'll ask for what to search, you need to say that query

5- play music

6- open notepad or any other app which is present in any query

7- what's the time now

8- search on wikipedia - you need to say anything you want to search on wikipedia. for example 'Tom Cruise Wikipedia'

9- open any other website or app. before that, you need to provide a path or link of that app or website.

10- Exit or quit

--> it can be Modified for a number of commands, depending upon the user's requirements, and if integrated with hardware, it can also be used as a robot.

Contribute:

We welcome contributions, bug reports, and feature requests. Feel free to fork the repository, make improvements, and submit pull requests to enhance Jarvis.
