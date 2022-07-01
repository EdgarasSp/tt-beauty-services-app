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


#
## Database Model

This project uses the PostgreSQL relational database. There is a total of 4 models.
#
### **Models**

#### **Contact Form**

---
Name              |Field Type   |Validation                                             
------------------|-------------|-------------------------------------------------------
subject\_type     |CharField    |max\_length=100                                         
service\_location |CharField    |max\_length=100                                  
first\_name       |CharField    |max\_length=50                                  
last\_name        |CharField    |max\_length=50                                         
contact\_number   |CharField    |max\_length=20                
email\_address    |TextField    |max\_length=50               
message\_problems |TextField    |max\_length=1000                  
received\_date    |DateField    |auto_now_add=True               
status            |IntegerField |choices=STATUS, default=0                                                 

#### **Booking Form**

---

Name              |Field Type   |Validation                                             
------------------|-------------|-------------------------------------------------------
first\_name       |CharField    |max\_length=50                                  
last\_name        |CharField    |max\_length=50                                         
contact\_number   |CharField    |max\_length=20                
email\_address    |TextField    |max\_length=50
service           |CharField    |max\_length=100                                         
service\_location |CharField    |max\_length=100                 
message\_problems |TextField    |max\_length=1000                  
received\_date    |DateField    |auto_now_add=True               
status            |IntegerField |choices=STATUS, default=0

#### **Portfolio Post**

---

Name              |Field Type        |Validation                                             
------------------|------------------|-------------------------------------------------------
title             |CharField         |max\_length=200, unique=True                                 
slug              |SlugField         |max\_length=200, unique=True                                        
author            |ForeignKey        |User, on\_delete=models.CASCADE, related\_name="portfolio\_posts",
featured\_image   |CloudinaryField   |'image' default='placeholder'
excerpt           |TextField         |blank=True                                        
updated\_on       |DateTimeField     |auto\_now=True                 
content           |TextField         |                  
created\_on       |DateTimeField     |auto\_now_add=True              
status            |IntegerField      |choices=STATUS, default=0
likes             |ManyToManyField   |User, related\_name='portfolio\_like', blank=True

#### **Comments**

---

Name              |Field Type      |Validation                                             
------------------|----------------|-------------------------------------------------------
name              |CharField       |max\_length=50                                  
email             |EmailField      |max\_length=50
body              |TextField       |max\_length=100                                         
created\_on       |DateTimeField   |auto_now_add=True
approved          |BooleanField    |auto_now_add=True                       
                                                    

#
## Features
#

### Home Page
#
Upon entering the home page of the website, the user sees a large hero image carousel, which displays helpful mesages encouraging to book an appointmnet, view services or contact us as a call to action button. 

![index-hero](https://i.imgur.com/nC1oBudh.png)

Scrolling down takes the user to the 'Why Choose Us' section of the page. The page features a brief text with info for the user and links to 'View Services' or 'Book Now". Also, displayes few pictures inline with the page theme.

![index-2](https://i.imgur.com/tIC6kihh.png)

Scrolling down further takes the user to the 'Product' section of the page. The page features 3 promoted products with a brief text description with info for the user. Section also, displayes a video from the salon showcasing one of the procedure.

![index-3](https://i.imgur.com/qOPZxhxh.png)

Next is a 'Feedback' section of the page. The page features 3 most resent reviews from the clients. 

![index-4](https://i.imgur.com/4GDOqZ3h.png)

The final part of the home page is a 'Contact Form' for user to fill should they want to contact us. From has preset choice list to help with query routing.

![index-5](https://i.imgur.com/A5xBk8ch.png)
#
### About Page
#
The first part of the about page contains contact address and furtehr contact details for both locations. This section also has a portait picture of one of the stylists.

![about-1](https://i.imgur.com/KtEpvMuh.png)

Second part of the about page contains embeded google map iframe with marked salon location. To the side of the map with a brief positive text description about the Salon.


![about-2](https://i.imgur.com/0RZ59bgh.png)

The final part of the home page is a 'Contact Form'

![about-3](https://i.imgur.com/A5xBk8ch.png)

#### Contact Success


Once the contact form is submited, the user is redirected to the home page. The page will show sucess pop up at the top confirming top the user that the form has been submited sucesfully.

![pop up](https://i.imgur.com/KGQ1Ccgh.png)


#
### Service Page
#
The Service page contains all the info a user needs about the services provided, as well as allowing them view the prices for the services. First section contains a small hero image of the stylist at the top of the page, with a description and a action button to book and appointmnet.

![resort-detail1](https://i.imgur.com/9g3YL7Eh.png)

Scrolling down takes the user to the 'Services & Prices' section of the page. The section features service list with info for the user and cost of each service line item.

![ski-map1](https://i.imgur.com/WDV1LMAh.png)

Scrolling down further takes the user to the 'Team' section of the page. The section features short description of the team and showcaing stylist in action.

![ski-map2](https://i.imgur.com/iIqrsqFh.png)

The last section is a "FAQ". This section contains most asked questions with answers provided below utilising accordion bootsrap design.

![ski-map2](https://i.imgur.com/69cJK9Nh.png)

#
### Portfilio Page
#
This page shows portfolio blog posts in card form format. The list is paginated with a maximum of 8 blogs shown per page. Portfolio Blog post are added via Django Admin Page. User can click on the card to open the portfolio blog post.

![blog1](https://i.imgur.com/4v2F264h.png)

### Portfolio detailed Page

Portfolio detail pages can be accessed by any user to view published existing portfolio blog post. The page shows the full blog content, date of publication, post likes and comments.

![blog-detail](https://i.imgur.com/VwDn4cQh.png)

 Each portfolio blog has a comment section where an authenticated user can leave their feedback on a blog. Any user can see blog comments, but only authenticated users can post them. The superuser has the authority to approve, delete a comment. If user is not authenticated, instead of having a text box tehy will be promted to register or login first. Once loged in, the text box will be displayed.

![comments](https://i.imgur.com/sEdKi39h.png)

#
### Booking Page
#

The Booking page contains a 'Make Appointment Form' for user to fill should when they want to book an appointment. Form has preset choice list to help with service routing.

![booking](https://i.imgur.com/7T24u05h.png)


#### Booking Success


Once the form is completed, the user is redirected to the home page. The page will show sucess pop up at the top confirming top the user that the form has been submited sucesfully.

![pop up](https://i.imgur.com/8MPS4UHh.png)

#
### Register
#

A user can register from the 'register' page. All user registration/login etc is handled by the 'Django-allauth' module.

The layout is simple. The inputs prompt the user to enter and confirm their email address, provide a username, and enter and confirm a password.

If a user enters invalid data (i.e. username already taken/passwords do not match etc) then the form will not submit and the errors will be displayed in the relevant location on the screen.

![register](https://i.imgur.com/BlephGYh.png)


#
### Sign In
#

A registered user can sign in from the sign-in page. A user can enter either their username or email along with the password.

![sign-in](https://i.imgur.com/LPPNUOuh.png)


### Add Blog Post - REPURPOSE   

If a user selects the 'add blog post' button from the blog page, they are taken to the 'new blog' page. This button and page are only accessible for authenticated users. The page contains a simple form, allowing a user to add a short blog post. The title and content fields are mandatory. The database automatically stores the current time and the authenticated user (author) upon form submission.

This page fulfills user story 19 :heavy_check_mark:

#
### Navigation and Responsiveness
#

The site uses a simple Bootstrap responsive navbar. All sections of the site can be reached from here. Logout for an authenticated user, and register/sign in for an unauthenticated user. The navbar menu items can be found within the standard 'hamburger' menu icon on smaller devices.

#
### Future Features
#

The site can be improved with:

* Better appointmnet management allowing stylist to create availability schedule and site visitors to book available slots based on the service choosen.

Additionally it woul be  grate to create profile page to allow users to:

* View and mange booked appointments
* Receive loyalty points for future sicounts

Site would also benefit with:
* payment processor
* disount/coupon process.
* email comunication workflow


#
## Device and Browser Testing
#

* Chrome developer tools used throughout development to check usability on different devices/sizes.

* Personal devices used to check usability and appearance after deployment Google Pixel 6

* Friends and family asked to check usability on their Apple mobile, laptop, desktop, and tablet devices, particularly to check usability on Safari browser

* Browsers checked were Chrome, Firefox, Edge and Safari

#
### Bugs
#

#### CSRF Verification Failed.

During porject development I received CSRF Verification Failed error when submiting forms. After checking code for hours I have found out that this error only occures uf istalled Django 4. After checking my Django version had to downgrade Django to 3.2 an dthe error was cleared.

![sign-in](https://i.imgur.com/OIo9j5jh.png)
#
#### Could not build wheels for backports.zoneinfo

After deploying app to Heroku, it was failing to build. After reviewing the logs found error "Could not build wheels for backports.zoneinfo" After some reaserch on Google found solution on StackOverflow. Solution noted that Heroku fails to install correction python version, to bypass this error a runtime.tx file was created in root directory containing single line of code defining python version for heroku to install "python-3.8.10".

After this app deployed sucesfully.

![sign-in](https://i.imgur.com/xedjxGLh.png)
#
#### Forms not posting to admin

After I created the first form, when tried to post data would not appear on Django Admin. The app was visable, the form data fields were pressent on Admin and I was able to add data directly via Admin. The forms were included via: {% include "contact/contact_form.html" %} command. 

After checking rewriting the forms and many hours of reading found out that the form needed additonal parameter within "Form" element to make data post correctly: action="{% url 'contact_form'%}". After adding this data was posting correctly.

### Code Validation

* [W3C HTML Validator](https://validator.w3.org/) found no HTML errors throughout the site - result for home page shown below

  ![html-validation](https://i.imgur.com/ta2lfbsh.png)

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) found no CSS errors throughout my files - result for all CSS shown below

  ![css-validation](https://i.imgur.com/WYsFvlkh.png)

* [JS Hint](https://i.imgur.com/5TrZYoSh.png) found no serious JavaScript errors throughout my files. There were a couple suggested use of dot notation:

* [PEP8 Online](http://pep8online.com/) found no Python errors throughout my files, except for settings.py. This is a known issue with the built-in Django settings file, but it is acceptable not to force a line break here.
  - line too long (>79 characters) - AUTH_PASSWORD_VALIDATORS = [{}] x4

### Chrome Dev Tools Lighthouse

Chrome dev tools lighthouse was used to test the site for performance, accessibility, best practices and SEO.

#### Performance

Performance was consistently good throughout all pages, only being slowed down slightly by images (which were already compressed), external embeded youtube video, and external JavaScript resources such as JQuery.


#### Best Practises

Scored between 95 - 100 on every page.

#### SEO

The SEO score tended to be around 90.

#### Screenshot from dev tools

I was getting notification warning about Chrome extensions affecting results, even in icognito mode.

![Dev-tools](https://i.imgur.com/lSNGt6ah.png)


## Technologies Used

### Languages Used

* HTML5
* CSS3
* JavaScript
* Python 3

### Frameworks, Libraries and Programs Used

* [Bootstrap 5.0.2](https://getbootstrap.com/) - Used for responsive layout, flexbox and several components e.g. cards, navbar, form elements.
* [jQuery](https://jquery.com/) - Used for interactive elements on the DOM and to simplify JavaScript use
* [Fontawesome](https://fontawesome.com/) - This was used for all icons on the page
* [Google Fonts](https://fonts.google.com/) - To get fonts
* [Git](https://git-scm.com/) - Used for version control
* [Gitpod](https://gitpod.io/) - Text editor used to write all code
* [Github](https://github.com/) - GitHub is used to store the project's code after being pushed from Git
* [Heroku](https://id.heroku.com/) - Used to deploy website - Heroku PostgreSQL used for relational database in deployed site
* [Balsamiq](https://balsamiq.com/) - Used to create the wireframe
* [Compressjpeg](https://compressjpeg.com/) - Used to compress images
* [Google Maps](https://maps.google.com/) - Used to embed maps
* [tabletomarkdown](https://tabletomarkdown.com/convert-spreadsheet-to-markdown/ ) - Used to convert spreadsheet tables to markdown for use in this readme
* [Cloudinary)](https://cloudinary.com/) - Used to store media files


#### Validation Programs Used

* [W3C HTML Validator](https://validator.w3.org/) - Used to validate HTML file
* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) - Used to validate CSS file
* [JS Hint](https://jshint.com/) - Used to validate JavaScript code
* [PEP8 Online](http://pep8online.com/) - used to validate Python code
