# TT Beauty Services

## About

This project is a simple website for a beauty salon. It allows visitors to view services,locations, submit questions, book appointments and comment to a portfolio blog on the website. Users must be logged in and authenticated to make a posts.

It uses HTML, CSS and JavaScript for the front end and makes use of Python and the Django framework for the backend, which also uses the PostgreSQL relational database.

A quick note regarding difficulties I had with this project. The ideas planned for the site were much greater, but I was struggling with so many things during this time and was not in a good place. I have made my best attemt to deliver the project in the time remaining. It's not the best project but I have learned so much and feel much more motivated to deliver great site experiance in the future project. With some support from my employer agreening additional time off to let me focus and complete the studies and my family to help with new born.

### Mockup
#
<a href="https://i.imgur.com/nC1oBudh.png"><img src="https://i.imgur.com/nC1oBudh.png" title="source: imgur.com" /></a>

## UXD
#
### Purpose
#
Website is more targeted torwards women needs, but options availabe to both men and children.
With certain design choices and information within website any visitor should instantly recognise the purpose of the site, and to feel compfortable to browse and explore the website.

Based on site being open to all, the user stories below are non-specific regarding demographic and only differentiate whether a user is a first time visitor, a general visitor or a existing user.
#
#### User Stories
#
User Story | As a user | I want to be able to | So that I can | Fulfilled
--------------|-----------|----------------------|---------------|--------------
1|first time visitor|recognise the purpose of the site immediately|identify whether I am interested in the content and wish to use the site|Yes
2|general visitor|easily navigate the site on any device|easily use and navigate the site|Yes
3|general visitor|view a list services|find services offered|Yes
4|general visitor|view a list of prices|see the cost for the services|Yes
5|general visitor|view protfolio posts|see porfolio posts to get an idea of experiences|Yes
6|general visitor|send a message|ask questions when additional information is required|Yes
7|general visitor|view FAQ section|get answers to most common questions without need to contact|Yes
8|general visitor|easily register an account| I can interact with the content|Yes
9|logged in user|easily login in and log out| I can interact with the content|Yes
10|logged in user|add comment to portfolio post|add personal comment to website|Yes
11|logged in user|like or unlike a post|I can interact with porfolio post I like oro dislike|Yes
12|logged in user|be notified when massages sent|be sure that my messages and bookings were susefull|Yes
13|admin/superuser|create, read, update and delete portfolio posts|mange porfolio posts|Yes
14|admin/superuser|view comments in pending state|approve or decline comments before posting|Yes
15|admin/superuser|view booking requests|contact the custmers to accept or reschedule|Yes
#
### Theme
#
The site has a simple layout, designed with Bootstrap framework.

The navbar always sits at the top of each page, taking the user to all the site sections they can access. Only the pages relevant to the user are displayed e.g. a logged-in user will not see a link to the 'login' page as they are logged in. Equally, a logged out user will not see a link to the 'logout' page as they are already logged out.

Pages designed with minimalist aproach to not overcrowed with uneccassry details or images. Page links and interactive elements are marked. Buttons have a colour scheme and if feedback required the 'positive' feedback popup have pink background, 'negative' have red background. This is the Bootstrap colour library (success and danger) but with the colours amendedmets to be inline with web page theme.
#
### Wireframe
#
Below are the wireframes created in advance of starting the project. I used the wireframing software [Balsamiq](https://balsamiq.com/) for this project.

* Desktop Wireframe
  ![Wireframe for Mobile](https://i.imgur.com/uBs4zvd.png)

* Tablet Wireframe
  ![Wireframe for Tablet](https://i.imgur.com/mh2cYjb.png)

* Mobile Wireframe
  ![Wireframe for Desktop](https://i.imgur.com/oOhFd4N.png)

#
### Theme
#
The palette for this project was light pink. Dominant color was matched against the extracted complement color using the [Adobe Color](https://color.adobe.com/create/image) tool.

Dominant color was generated using [ColorSpace](https://mycolor.space.com).

Website color pallet:
* Dominant:		[#fd458c](https://mycolor.space/?hex=%23fd458c&sub=1)
* Complement: 	[#feebf2](https://mycolor.space/?hex=%23feebf2&sub=1)
* Text A: 		[#292929](https://mycolor.space/?hex=%23292929&sub=1)
* Text B: 		[#2b2a2a](https://mycolor.space/?hex=%232b2a2a&sub=1)
