# Classmatch
For submission to YHack 2020

![alt text](https://github.com/yizhoucc/class_match/blob/master/interface.png)

## Team members
Yizhou Chen,
Facheng Guo,
Daming Li

## What inspired us
The pandemic of COVID-19 has a severe negative impact on the learning experience at school. Students have significantly fewer chances to know and to interact with classmates. Whereas websites such as Canvas and Piazza are useful tools for pedagogical purposes, an application integrating formal learning and informal conversations or discussions is missing. Based on such considerations, we aimed at building a website "Classmatch", which allows students to connect based on the common courses taken and to know each other better through academic or non-academic discussions in class chatrooms. 

## What Classmatch does
Classmatch, in its current basic version, achieves the following functionalities: Creation of an account; Login/Logout; Enter personal information; Enter course titles; See name and contact information of those who are in the same classes with you. The application is running in a pop up window, as we wanted it to be light and easy for chatting purposes.

## How we built Classmatch
The application was built in the framework of Flask. User and class information are kept in database using MySQL. The front end was built using CSS and Javascript.

## What's next for Classmatch
Apparently, fulfilling all the key features of this application is a big project and the vision can go more ambitious. The short term goal is to make the application more secure by verifying the edu mailing address and gives the user to selectively show personal information. A personal webpage for each registered user is going to be added. Next, we would implement the chatting features (starting from a Say Hi feature) and create metrics to monitor user interactions and enhance user engagement.

## Challenges we ran into
- Maintaining user and class information dynamically and consistently in database
- Interface between the python and CSS code

## Accomplishments that we are proud of
This is a large-scale project and completing all the core functionalities apparently requires more time than a mere week. We knew this well in mind, and are proud to have established a rudimentary version of it under time pressure. Our system manages user and course information consistently upon updates and insertions.

## What we learned
- Product and UI design
- Various technical skills for building a web application from scratch
- Project management (initial design, collaborative work, testing)

## Try it out!
Open http://66.228.46.150:8080/getstart, then follow the instructions.

