# C4C-Message-Board
Code4Community Technical Assessment By Amit Chandra

## Overview and Components
This is a simple message-board web application. The backend is written in Python using the Flask web-framework, as well as Flask-SocketIO to enable communication between clients and the server. Here, the Flask object is initialized and the app runs in main. The backend main.py file performs basic message handling received from user input, and routes to the frontend, which renders the index.html file. 
The frontend is primarily written in HTML, and uses jQuery scripts and socket.io CDNs to initialize the socket with the website URL and interact with the backend. Messages sent on the application are formatted in paragraphs with the 'p' tag. The user inputs their username as well as their message, and must click a "Send" button to send their message to the server, which will display in the center of the screen. The topmost message is the most recent message sent. When a user hits the "Send" button, it is first validated that the user has entered a username and that the message is longer than 0 characters and shorter than or equal to 128 characters before the message is sent. 
The app is hosted on the free Heroku service. Thus, a Procfile and a requirements.txt file including the necessary components to install are located in the repository.
  
## Fulfilled Requirements
1. Users should be able to type a message and post it to the message board (the message must be non-empty, and at most 128 characters long). 
When a user enters the site, they are met with a box to insert a username and a box to insert their message. The user can type whatever message they want into the box. When they hit the send button, the requirements for a proper message are validated before the message finally posts on the message board in front of them.
  
2. Users should be able to see messages on the message board from most to least recent.
Whenever a new message is posted, it appears above the previous message sent, pushing the previous message down. Thus, users can view messages from most to least recent, as they are displayed top to bottom on the website.

3. Users on different computers should be able to post to the same board and view each other’s messages.
If users from different computers have joined the website, a message sent from one computer will also be displayed on the other computers' screens. The message board is not instanced according to a specific user, but a shared space for users across different machines. This could be implemented easily thanks to Heroku's service.
  
## How To Start The Application
Simply click on the link! https://c4c-message-board.herokuapp.com/
