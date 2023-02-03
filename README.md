# HUMAN-RESOURCES APP
# Table of Contents
* [Introduction](#introduction)
* [User Expereince (UX) design](#1-user-expereince-ux-design)
    * [User Goals](#11-user-goals)
    * [User Expectations](#12-user-expectations)
    * [Color Scheme](#13-color-scheme)
    * [Images and Log](#14-images-and-logo)
    * [Site Skeleton](#15-site-skeleton)
* [Features](#2-features)
    * [Main Section](#main-section)
* [Technologies Used](#3-technologies-used)
* [Testing](#4-testing)
    * [Testing tools](#41-testing-tools)
    * [Manual Testing](#42-manual-testing)
    * [Lighthouse Reports](#43-lighthouse-reports)
* [Bugs](#5-bugs)
* [Deployment](#6-deployment)
* [Acknowledgement](#7-acknowledgement)

Welcome to [Player vs. Player Game!](https://human-resources.onrender.com/)

# Introduction

HR-App is an basic humnan resources app where a small company can manage employees. The app was build with HTML, CSS, JavaScript,Python and Django. The main purpose of the project is to Create, Read, Update and Delete (CRUD) entries in a database and display them.

![dahsboard image](/static/images/dashboard.PNG)

# 1. User Expereince (UX) design

* The app was build to 100vh;
* The app is interactive, with nice alerts after each action;
* The app was built mostly for admin, a regular user can only apply for leaves.


# 1.1 User Goals

The app is designed for a small company. The main user of the app is an admin user because he can add other users, add emokoyees and their details;

# 1.2 User Expectations

The content of the app changes at every action of a user. Folloiwng user's expections ware considered while designing the site:

* The site structure is designed considering the expectation of users to be simple and easy to use;
* The user interface is easy to navigate;
* Responsive design for all screen/device sizes like mobile, tablet and desktop;

# 1.3 Color Scheme

The choice of website right foreground and background colour is essential that decides the site visitors wheather to emote the site or not. I used [Color Hunt](https://colorhunt.co/) to select the background and foreground color. Colors that i used are:

* #0E5E6F and #F2DEBA; - main background colors;
* and some bootstrp5 colors: warning, info, primary, alert

# 1.4 Images and Logo

This website was created for academic purposes, all photos were searched and downloaded from [Giphy website](https://giphy.com/)

# 1.5 Site Skeleton

[Balsamiq](https://balsamiq.com/) was used to create wireframes of the website. This was very useful as it gives the template of the UI. Wireframes were designed for web browser and a mobile browser format:

## Main Page:
![Main page whireframe image](/static/images/skeleton.PNG)

# 2. Features

# Main Section

* Logo is placed in the top left corner;
* I used FontAwsome for icons to the entire site;
* Login Button is placed on the top right corner. If a user is loged in the button will change to logout
* In the footer I have put only copyright and my name as a link witch will redirect on a new page to my website
* The layout is the same to the entire app.
* Sidebar with navigation links
* A small dropdown menu on the top of the page witch is visible only for logged in users as an admin;


# 3. Technologies Used

* HTML5 was used for structuring and presenting content of the website;
* CSS3 was used to provide the style to the content written in a HTML;
* JavaScript was used to add some nice alerts;
* Django was used as web framework;
* Django Template was used as a templating language for Django to display backend data to HTML;
* Django Allauth was used for user authentication, registration, and account management.
* Django Crispy Form was used to control the rendering of the forms;
* Gunicorn was used as Python WSGI HTTP Server for UNIX to support the deployment of Django application;
* Cloudinary has been used as image management solution;
* ElephantSQL database was used in production, as a service based on PostgreSQL;
* Render was used to deploy the website
* Balsamiq was used to create wireframes of the website;
* Font Awsome was used to improt icons to the sites;
* Google Fonts was used to import font-family 'Raleway' into style.css file;
* Chrome was used to debug and test the source code using HTML5 as well as to test site responsiveness;
* Github was used to create the repository and to store the cproject's code after pushed from Git;
* Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub
* Gitpod was used as the Code Editor for the site;
* Color Hunt was used to select the background and font color in the website;
* W3C Markup and Jigsaw validation tools were used to validate the HTML code and CSS style used in the proejct;


# 4. Testing


1. As a Site Admin I can create, read, update and delete employees,
2. As a Site Adnmin I can add new users,
3. As a site Andmin I can approve, unnaporve and reject leaves.
4. As a Site User I can login after an account is created for me,
5. As s Site User I can apply for leaves and view if the leave will be approved or not,
6. As a Site User I can view my profile details and view birthdays. 


# 4. Testing

## 4.1 Testing tools:

* Google Developer Tools for debug and test css and JavaScript code;
* W3C Validator Tools was used to check for any errors within my HTML pages:
* W3C CSS Validation was used to check for any error within my CSS stylesheet:


## 4.2 Manual Testing

I have tested my site on multiple devices. These include:
* Galaxy Fold (280 x 653);
* Iphone 6/7/8 Plus (414 x 736);
* Ipad (768 x 1024);
* Nest Hub (1024 x 600);


## Main Section

| TEST | OUTCOME | PASS / FAIL |
|:---:|:---:|:---:|
| Login Button| When Login is clicked I am redirected to login page | PASS |
| Logout Button| When Logout is clicked I am redirected to index page | PASS |
| Responsive | All pages and elements are responsive (mobile and desktop) using differnt breakpoints. | PASS |
| Text | Checked if all fonts and colors used are consistent or not | PASS |


## Dashboard Section

| TEST | OUTCOME | PASS / FAIL |
|:---:|:---:|:---:|
| Menus |All menus links redirect me to the right url | PASS |
| Username | Username is displayed for the right user when he is loged in | PASS |
| Logout Button | When I am loged in the login button change to logout | PASS |
| Animations | All animations effects works on all pages | PASS |
| Add Employee | Form is rendered correctly and when I submit it the new employee is added and displayed in the employees list | PASS |
| Edit Employee | Form is rendered correctly and when I submit it the employee details are updated and displayed in the employees list | PASS |
| Add/Edit Emergency Details | Form is rendered correctly and when I submit it the details are added to the correct employee| PASS |
| Add/Edit Family Details | Form is rendered correctly and when I submit it the details are added to the correct employee| PASS |
| Add/Edit Bank Details | Form is rendered correctly and when I submit it the details are added to the correct employee| PASS |
| Add User | Form is rendered correctly and when I submit it the new user is added and displayed in the users list | PASS |
| Create Leave | Form is rendered correctly and when I submit it the leave request will pe displayed on all leaves page | PASS |
| Approve/Unapprove/Reject Leave | On click the leave request is updated and will be moved on the right table | PASS |
| User Profile | On click I am redirected to the right user profile and I am able to edit it | PASS |
| Search Employees | When I search for an employee I recive the correct one | PASS |
| Search Employees | When I search for an employee I recive the correct one | PASS |
| Edit/Delete Employees | I can edit and delete employees from the employees table | PASS |
| Employees Birthdays | I can view the employees birthdays displayed from the current month | PASS |

## 4.3 Lighthouse Reports:

## Dashboard:
![Lighthouse report](/static/images/dashboard_report.PNG)

## Profile:
![Lighthouse report](/static/images/profile.PNG)

## All Employees:
![Lighthouse report](/static/images/employees.PNG)\

## All Leaves:
![Lighthouse report](/static/images/leaves.PNG)

## Birthdays:
![Lighthouse report](/static/images/birthdays.PNG)

## Coudinary Error:
![Lighthouse report](/static/images/error.PNG)


# 5. Bugs

* During the development process I had multiple bugs with the page rendering and content displayed. Ussualy some missed informations in my views was the problem all fixed;
* Error when I tried to to testing for my views problem that I did not fiexd yet
* Sidebar was not responsive so I had to rewrite the code for sidebar
* Cloudinary error in ligthouse report

# 6. Deployment

 The site was deployed to Render using the following steps: 

 * Sign up to GutHub;
 * Create a new repository on GitHub;
 * Link Github projec to Render
 * Add build.sh
 * Update settings.py
 * Add env.py to Render and Environment Variables
 * Automatic deployment by Render 


# 7. Acknowledgement

* This App was created for academic purposes, all photos were searched and downloaded from the[Giphy website](https://giphy.com/)
* For README.md file, reference of https://github.com/dhakal79/Portfolio-project-MS1 was considered; 
* Thanks to my mentor Marcel Mulders for his support and feedback.