# InstruMental

## A classified ads site for used music related items.

![Mockup of Instrumental](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/screenshots/mockup.png)

**InstruMental - a forum for users to buy and sell used musical instruments and gear.**

[Click here](https://instru-mental.onrender.com) to visit the deployed site.

## Contents


1. [Project Goals](#project-goals)
2. [User Goals](#user-goals)
3. [Structure](#structure)
    1. [Home Screen](home-screen)
    2. [Booking Process for Patient](#booking-process-for-patient)
    3. [Staff area](#staff-area)
    4. [Staff Schedule](#staff-schedule)
    5. [Patient Log](#patient-log)
4. [User Stories](#user-stories)
    1. [Patient User Stories](#patient-user-stories)
    2. [Staff Member User Stories](#staff-member-user-stories)
    3. [Site Owner Goals](#site-owner-goals)
5. [Technical Design](#technical-design)
    1. [Flow Chart](#flow-chart)
    2. [Data Models](#data-models)
    3. [User Interface](#user-interface)
6. [Features](#features)
    1. [Feature 1: The Patient Booking System](#feature-1-the-patient-booking-system)
    2. [Feature 2: The Schedule](#feature-2-the-schedule)
    3. [Feature 3: The Patient Log](#feature-3-the-patient-log)
    4. [Features to be implemented](#features-to-be-implemented)
7. [Technologies Used](#technologies-used)
    1. [Languages](#languages)
    2. [Applications, Platforms and Libraries](#applications-platforms-and-libraries)
        1. [Applications and Platforms](#applications-and-platforms)
        2. [Python Libraries](#python-libraries)
        3. [Third Party Libraries](#third-party-libraries)
8. [Validation](#validation)
9. [Testing of Patient User Stories](#testing-of-patient-user-stories)
10. [Testing of Staff Member User Stories](#testing-of-staff-member-user-stories)
11. [Testing of Site Owner Goals](#testing-of-site-owner-goals)
12. [Bugs](#bugs)

13. [Deployment](#deployment)
    1. [Forking the GitHub Repository](#forking-the-github-repository)
    2. [Making a Local Clone](#making-a-local-clone)
    3. [Heroku](#heroku)
    4. [Google API](#google-api)
14. [Credits](#credits)
15. [Coding tips and tricks](#coding-tips-and-tricks)
16. [Acknowledgments](#acknowledgments)

# User Experience

## Strategy

### Project Goals

Project Goals for intended use are:

- Creating a forum where users can buy and sell items
- The main features of the forum are members only
- Signing up is easy, secure and fast
- The users can manage their ads and themselves as users


My personal project goals of FeelGood Physio are:

- To create a user-friendly application that stands out from the crowd
- To expand my knowledge of Django, Python and Full Stack Development in general

### User Goals

Users should be able to search for, browse lists of and view advertisements on the site.

Logged in users should be able to post ads, manage posted ads and view other users contact details. They should also be able to view and edit a personal profile.

### Site Owner Goals

Site owners should be able to log in to an admin area, where they can review and delete ads or users that violate the site regulations.

**Target Audience**

- Musicians
- Music enthusiasts
- Hobby musicians
- Parents with children who play an instrument

## Structure

The structure of this site is simple; the heart of the site is the list of ads, depending on the search criteria. The pages are listed below. All pages contain a navbar at the top with the main logo and navigational menu, as well as a footer with navigational links, contact and copyright info.

### 1. Home

<details>
    <summary>Click here to view the home screen</summary>

![Screenshot of Home](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/screenshots/home_1.png)

</details>

The home screen contains a lot, but is well organized. It contains:

- A Hero Image
- A search field
- Links to categories of all ads posted
- Three feature cards mostly for design purposes, including an external link

### 2. Sign In/Sign Up

<details>
    <summary>Click to view image</summary>

![Login/Signup](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/screenshots/sign_in.png)

</details>

This page contains username and password fields, as well as links to sign up and retrieve password. If a user clicks on Sign Up, fields appear for the user to fill in. 

![Signup](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/screenshots/signup.png)

</details>

### 3. Ads List

The heart of the site, showing the ads relevant from the users search.

### 4. Ad Detail

The specific ad clicked on, with more detailed info, including for the seller.

### 5. User Profile

This contains the basic user information, and the ads that the user has published. All of which can be edited. Users can also view other users profiles and their ads, and remove their profile if desired.

### 6. Contact

On the Contact page, users can fill in a simple contact form, sending an email to the site owner via the Django email service.

## Epics and User Stories

### Epic 1: Core functionality - User Stories

1. As a user, I can easily navigate to the main site pages by scrolling to the top of the page and clicking a link

2. As a user, I can perform a search so that a list of items for sale is generated

3. As a user, I can refine my search so that the results display items in a specific location or category.

4. As a user, I can click on an item so that I can view its details

5. As a user, If I am not signed in, I am redirected to sign in/up if I click on any of the links or buttons restricted to logged in users

6. As a user, I get direct response and confirmation of my actions made on the website

### Epic 2: User Authentication - User Stories

7. As a user, I can sign up, so that I can utilise the full functionality of the website

8. As a registered user, i would like my login info and the ability to edit my personal ads be restricted to me only

9. As a registered user, I can receive a new password if it is forgotten, so that i can login to the site again

### Epic 3: Features for logged in users - User Stories

10. As a registered user, I would like to see a “Sign in/Sign Out” option, so that i can sign in or out

11. As a logged in user, I can view other sellers profiles

12. As a logged in user, i can save ads to a “saved” list so that I can easily view them later

### Epic 4: The Location Field

13. As a logged in user, I can add a street to the location field in my profile and it will automatically appear as my default location when I post a new ad

14. As a logged in user, as I enter a street, the location field fills in an actual adress for me to choose.

15. As a registered user, my city but not my street is saved on my public profile, so that others cannot see my exact address

### Epic 4: User Profiles - User Stories

16. As a registered user, I can create edit or remove a user profile, so that I and others can easily view my ads and personal info

17. As a registered user, I can view other sellers ads on their profiles

### Epic 5: The Ad Detail Page - User Stories

18. As a user, I can view a picture and a description of the item on the Ad Detail page

19. As a registered user, I can view options to post and edit ads, so that I can create, read, update and delete my ad
20. As a logged in user, I can mark my item as sold, so that other users are aware of this

21. As a user, I can click a share button in the ad detail page, so that I can share it on social media platforms

### Epic 6: The Contact Page - User Stories

22. As a user, I can view a contact page so that I can easily contact the site owner if needed, whether I am registered or not

### Epic 7: Admin/Site-Owner Functionality - User Stories
23. As a site owner, I can access an admin page, where I can view all ads and profiles, and delete them if necessary
24. As a site owner, I receive an email when users submit the contact form, so that I can reply to them



## Technical Design

### Code Structure

As usually is the case with Django projects, InstruMental is devided into apps. The apps are listed below.

* user_profile - This caters for users personal profile, edit and remove functionality for that.

* ads - is responsible for all functionality regarding posting, editing, iewing and removing ads.

* contact - A simple page where users can contact the site owner.

* main - This app caters for showing the home or index page, and includes the python code responsible for autogenerating adresses in the area/location fields.

* search - responsible for making queries to generate the desired list of ads.

* user_account - A simple app solely responsible for removing a user from the site's database if they desire.

#### Other Directories

* jv_instrumental - the project directory, contains settings and configurations for the entire project.

* docs - documetation, screenshots, testing, etc are included here.

* media - images on the site and uploaded by users

* static - CSS and JavaScript files

* templates - The html code with built in python / django logic to work with data to and from from the database

* Various other files - various setting files for core functionality.


### Database

This is a datacentric website using HTML, Javascript and CSS, including libraries Jquery and Bootstrap.
Python and the Django framework was used for the backend, with SQLite3 as a development backend and Postgre for the deployed version.

Read more about them here.

* PostGres: (https://www.postgresql.org/)

* SQLLite: (https://www.sqlite.org/index.html)

### Data models

AS the standard goes working with databases, I have learned to use the Data model and have three in this project, including the built in User model that Django provides. You can see the fields 

* User - As authorisation is accounted for by Django automattically, it seemed daft to not take advantage of that.

* Profile - As the user model has limited data fields, I expanded them using my own Profile model as a complimentary one. Together they have all the fields necessary for the application.

* Ad - The data model for a users ad, with fields linking it to the user.

Below is a detailed image of the models and their relation to each other.

### Schema of models

This schema describes the structure of the application, and was created with [Lucidchart](https://lucid.co/product/lucidchart).

<details>
    <summary>View schema here</summary>

![Schema](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/schemas/db_schema_models.png)

</details>

## Skeleton

### Wireframes

![Wireframes](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/wireframes/wf_instru_mental_home_desktop.png)

Wireframes haev been made for each of the pages and cak be found here: [Wireframes](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/tree/main/docs/wireframes)


## Surface

I wanted an artistic and not so perfect design this time, and chose shades of beige and orange mostly. I wanted it to feel a little like a second hand store.

### Typography

found these two fonts on Google Fonts that were perfect for this project.

* Comforter Brush:

![Comforter Brush](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/screenshots/typography/conforter_brush.png)

This is solely used for the main heading, and I think it makes a big impression for that

* PT Sans

![PT Sans](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/screenshots/typography/pt_sans.png)

### Color Palette

![Color Palette](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/screenshots/color_palette.png)

Here are the main colors, which I think give a good feel to the website. The design is simple, and the subtle colours complement each other.

Color palette here was generated using [canva.com]https://www.canva.com/colors/color-palette-generator/

## Existing Features

### Feature 1: The Navbar

This is the means in which users can make their way around the website. From here they can navigate to all pages of relevance, Home, Post Ad, Profile, Contact, and Sign In/Sign Up.

![Navbar](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/docs/screenshots/features/navbar.png)

This is always visible at the top of the page, once scrolled up. I chose not to retain it as a 'sticky' navbar, so that the smallest of screens can view as much content as possible.

**User stories goals covered:**

1. As a user, I can easily navigate to anywhere of relevance on the site by scrolling to the top of the page and clicking a link

5. As a user, If I am not signed in, I am redirected to sign in/up if I click on any of the links or buttons restricted to logged in users

6. As a user, I get direct response and confirmation of my actions made on the website


### Feature 2: The Home Page / Search

![Home Page](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/screenshots/features/search.png)

The Home page consists of a search form, which is its main functionality. The purpose is that users can make their search straight away when they visit the website - whether they are logged in or not.

a hero image, links for the different categories and three feature cards.

In the search form, users can query a location, category and free search text, and get results that are relevant for those criteria.

**User stories covered:**

2. As a user, I can perform a search so that a list of items for sale is generated

3. As a user, I can refine my search so that the results display items in a specific location or category.

### Feature 3: The User Profile

![The User Profile](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/screenshots/features/profile.png)

The User Profile is the users own space in this application. This is where the user adds their personal data, can modify, mark as sold, or remove their ads. The users saved ads will appear here also. Users can click on the username in the ad and view others profiles, and the ads they have posted, aswell as I chose a simple design to bring focus to the ads.

If a user desires, they can remove their user account completely.

**User stories/site-owner goals covered:**

4. As a user, I can click on an item so that I can view its details

5. As a user, If I am not signed in, I am redirected to sign in/up if I click on any of the links or buttons restricted to logged in users

8. As a registered user, i would like my login info and the ability to edit my personal ads be restricted to me only

11. As a logged in user, I can view other sellers profiles

12. As a logged in user, i can save ads to a “saved” list so that I can easily view them later

16. As a registered user, I can create edit or remove a user profile, so that I and others can easily view my ads and personal info

17. As a registered user, I can view other sellers ads on their profiles

### Feature 4: Ad Post, Edit and Remove

![Ads](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/screenshots/features/post_ad.png)

The ad functionality is the heart of the site, and it it super simple to post, edit and delete ads.

The Post Ad button is visible in the navbar throughuot the site and users just have to fill in a form with the ad title, pick a category, add a description, price, upload an image, and finally add a location. When the user clicks Post Ad the ad is visible in the search on the home page, as well as on the users profile.

The Edit Ad page is visible through the Ad detail page, and from there users can modify all fields of the ad, as well as delete it.

**User stories covered:**

6. As a user, I get direct response and confirmation of my actions made on the website

8. As a registered user, i would like my login info and the ability to edit my personal ads be restricted to me only

11. As a logged in user, I can view other sellers profiles

16. As a registered user, I can create edit or remove a user profile, so that I and others can easily view my ads and personal info

17. As a registered user, I can view other sellers ads on their profiles

19. As a registered user, I can view options to post and edit ads, so that I can create, read, update and delete my ad
20. As a logged in user, I can mark my item as sold, so that other users are aware of this

### Feature 5: The Ad Detail Page

![Ad Detail](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/screenshots/features/ad_detail.png)

The Ad Detail is where the user can view a sellers contact details, a larger picture of the ad and save the ad to their Saved Ads list. Here they can view a location of the ad, but not the exact street for security purposes.

**User stories covered:**

6. As a user, I get direct response and confirmation of my actions made on the website

12. As a logged in user, i can save ads to a “saved” list so that I can easily view them later

18. As a user, I can view a picture and a description of the item on the Ad Detail page

19. As a registered user, I can view options to post and edit ads, so that I can create, read, update and delete my ad
20. As a logged in user, I can mark my item as sold, so that other users are aware of this

21. As a user, I can click a share button in the ad detail page, so that I can share it on social media platforms


### Feature 6: The Location Field

![Location Field](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/screenshots/features/ad_detail.png)

**User stories/site-owner goals covered:**

13. As a logged in user, I can add a street to the location field in my profile and it will automatically appear as my default location when I post a new ad

14. As a logged in user, as I enter a street, the location field fills in an actual adress for me to choose.

15. As a registered user, my city but not my street is saved on my public profile, so that others cannot see my exact address


### Feature 7: The Contact Page

![Contact Page](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/screenshots/features/contact.png)

The "contact" page contains a simple form, where the user can fill in their name, email address subject and message, which they can send by clicking the submit-button.

The form is validated and sent by Django and the site owner recieves an email straight away.

**User stories/site-owner goals covered:**

22. As a user, I can view a contact page so that I can easily contact the site owner if needed, whether I am registered or not

24. As a site owner, I receive an email when users submit the contact form, so that I can reply to them

#### Feature 8: The Admin Page

The admin page is where site owners can access all users data, and modify or remove anything they like. A discreet link to the admin page is visible in the page footer.

**User stories/site-owner goals covered:**

23. As a site owner, I can access an admin page, where I can view all ads and profiles, and delete them if necessary



### Features to be implemented

This application is of the simplest sort, when it comes to classified ads sites, burt the most important things are in place. Here are some features that could be implemented in a future version.

* A chat or messaging app, to communicate with others

* The ability to add several pictures to an ad

* Ad posts for buyers also

* Notifications if an ad is posted that matches a users query


## Technologies used

### Languages

- [Python 3.8](https://www.python.org/) was used for backend programming

- [HTML5](https://en.wikipedia.org/wiki/HTML5) was used for building all web pages

- I used [CSS3](https://en.wikipedia.org/wiki/CSS) for styling the website

- A little [JavaScript](https://en.wikipedia.org/wiki/JavaScript) for alert and location fnunctionality

### Applications, Libraries and Platforms

This project is built solely through the framework [Django](https://www.djangoproject.com/), and I have tried to make use of its many powerfiul features.

I have used [Bootstrap 5](https://getbootstrap.com/) as a framework for styling for efficiency purposes, although that wasn't always the case.

A few lines of [JQuery](https://jquery.com/) for autodissapear of alerts

- [Font Awesome](https://fontawesome.com/) fonts were used for all icons in this project.

- [Google Fonts](https://fonts.google.com/) - Were used for all fonts and icons in this project.

- [Git](https://git-scm.com/) - Version control system used to commit and push to Github via Gitpod.

- [Github](https://github.com/) - The projects repository and all its branches were commited,
and pushed to Github.

- [Heroku](https://www.heroku.com) - Used to deploy the application.

- [AWS S3 Bucket](https://aws.amazon.com/s3/) - Used to host media and static(CSS and JavaScript) files for the site.

- [Gitpod](https://gitpod.com/) - All code was written and tested with the Gitpod web-based IDE.

- - [Google Cloud Platform](https://console.cloud.google.com/) was used for the location autocomplete functionality via the Google Javascript and Google Geocoding API's.

- [Balsamiq Wireframes](https://balsamiq.com/wireframes/) was used to create wireframe images of the website which you can view [here](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/wireframes/all_wireframes_musical_minds.pdf).

- [Lucidchart](https://lucid.co/product/lucidchart) was used to create the visual [data schema](#data_schema) of the project.


## Validation

All Python files passed the [PEP8](http://pep8online.com/) and [Pylint](https://www.pylint.org/) tests with 0 errors and the following result on all files.

![PEP8 Validation](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/validation/pep8.png)

All Javascript files passed JSHint validation with 0 errors

![JSHint Validation](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/validation/jshint.png)

### HTML Validation

All pages passed the [W3C HTML Validation](https://validator.w3.org/) tests with 0 errors, and can be viewed [here](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/tree/main/docs/validation/w3c/html)

### CSS Validation

The CSS on the website passed the [W3C CSS Jigsaw](https://jigsaw.w3.org/css-validator/) validation with 0 errors:

![Results from CSS-validation](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/tree/main/docs/validation/jigsaw_w3c.png)


### Performance/Accessibility

[Google Chromes Lighthouse](https://developers.google.com/web/tools/lighthouse) was used for testing the performance and accessibility of the website, which passed the tests on both desktop and mobile simulator. You can see the results [here](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/tree/main/docs/validation/lighthouse)

### Devices

Testing was done using a MacBook Pro and Google Chromes device simulator for smartphone (iPhone SE), Tablet (iPad) and desktop views. All devices were successful in display and functionality.

## Testing of User Stories

User stories are tested with the features that cover them. All user stories passed the tests and can be viewed [here](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/tree/main/docs/TESTING_USER_STORIES.md)




</details>

## Bugs

<details>
    <summary>View bugs here</summary>
___

**Bug**: Page not loading, GET error and django wants to load wrong page

**Fix**: Change precedence of urls in urls.py, so Django doesn't think that I'm using a non-existent slug

___

**Bug**: Autocomplete in location field doesn't work.

**Fix**: .
___


**Bug**: Images not loading

**Fix**: Incorrectly configured directory and reference in HTML-file
___

**Bug**: Search not providing any results

**Fix**: Conflict with ad Django object and HTML class with same name. Remove class.
___

**Bug**: Page not displaying properly

**Fix**: Stray <div> tag, removal fixed it
___

**Bug**: Image flowing outside the ad element covering the whole page

**Fix**: Contain it with CSS
___

**Bug**: Loading wrong page

**Fix**: Slug issue again, wrongly configured
___

**Bug**: Images not loading on deployed version

**Fix**: Correct syntax for displaying media in Django for AWS S3 bucket
___

**Bug**: All ads appearing as liked

**Fix**: Wrongly configured logic, remove visibility for likes except in ad detail
___


</details>


## Deployment

### Forking the GitHub Repository

To make a clone, or 'Fork' this repository, follow the steps below.

1. Access your GitHub account and find the relevant repository.
2. Click on 'Fork' on the top right of the page.
3. You will find a copy of the repository in your own Github account.

### Making a Local Clone

1. Access your GitHub account and find the relevant repository.
2. Click the 'Code' button next to 'Add file'.
3. To clone the repository using HTTPS, under clone with HTTPS, copy the link.
4. Open Git Bash.
5. Access the directory you want the clone to be have.
6. In your IDE's terminal type 'git clone' and the paste the URL you copied.
7. Press Enter.
8. You now have a local clone.

### Heroku

This application has been deployed from Github using Heroku. Here's how:

1. Create an account at [heroku.com](https://.heroku.com/)
2. Create a new app, add app name and your region
3. Click on create app
4. Go to "Settings"
5. Under Config Vars, add your sensitive data (creds.json for example)
6. For this project, I set buildpacks to <Python> and <NodeJS> in that order.
7. Go to "Deploy" and at "Deployment method", click on "Connect to Github"
8. Enter your repository name and click on it when it shows below
9. Choose the branch you want to buid your app from
10. If desired, click on "Enable Automatic Deploys", which keeps the app up to date with your Github repository
11. All done!

### AWS S3

The deployed version of this website has static(CSS and JavaScript) and media files hosted to it via a web based service called Amazon Web Services S3 Bucket.

The steps to take are:

1. Create an account at aws.amazon.com
2. Navigate to the IAM application and create a user and group
3. Set the AmazonS3FullAccess for the user and copy the AWS ACCESS and SECRET keys as config vars to your workspace and deployment environment
4. Create a new Bucket within the S3 application with an appropriate name.
5. Enable public access for your bucket so users can access and use the services on your website (upload, view, download, etc). More info can be read in the official documentation: https://aws.amazon.com/s3/


### Google API

Here's how you can set up your own API:

1. Login or create a Google account and navigate to https://console.cloud.google.com/
2. Create a new Project by clicking on the New Project icon
3. Add Project name and details
4. Under API's and services, enable the relevant API for your project (in this case Google Drive, Sheets and Calendar)
5. IF the API requires, create a credential (service account in this case) for your project
6. Save the API key as a secret in config vars in your workspace and deployment environment
7. Under API's and services, enable the relevant API for your project (in this case Google Drive, Sheets and Calendar)
8. Search for the needed tasks to be performed in the documentation for the specific API, for example here for the calendar API: [Google Maps API Reference](https://developers.google.com/maps/documentation/javascript/overview)
9. Add them to your code.


## Credits

### Copywrites

* Images:

Instrument category icons: https://www.flaticon.com/authors/flat-icons, https://www.freepik.com

Home page images are from https://pixabay.com

Ad images are from https://commons.wikimedia.org, https://www.sequential.com/, private image.


### Coding tips and tricks

Thess links have helped me getting it all to work, and learn more about the Django framework.


Django social share:
https://studygyaan.com/uncategorised/adding-a-social-share-button-to-your-django-website

Ellipsis Overflow:
https://stackoverflow.com/questions/20552957/fluid-width-with-text-overflow-ellipsis

Delete user:
https://stackoverflow.com/questions/38047408/how-to-allow-user-to-delete-account-in-django-allauth

Geocoding:
https://www.codingforentrepreneurs.com/blog/python-tutorial-google-geocoding-

Hide ugly arrows from integer input:
https://stackoverflow.com/questions/3790935/can-i-hide-the-html5-number-input-s-spin-box

Being able to display other users than the one logged in:
https://stackoverflow.com/questions/64379294/make-user-profile-visible-to-all-users-include-anonymouseuser-on-django

User linked profile with two forms:
https://rohitlakhotia.com/blog/django-custom-user-model/

get_initial:
https://gist.github.com/rodo/8560557

Add slug to Django CreateView:
https://kodnito.com/posts/slugify-urls-django/

Using CreateView:
https://www.agiliq.com/blog/2019/01/django-createview/#using-createview
DetailView
https://www.agiliq.com/blog/2019/01/django-when-and-how-use-detailview/

Building a custom user profile:
https://www.ordinarycoders.com/django-custom-user-profile

CORS configs in AWS S3:
https://stackoverflow.com/questions/65133018/i-need-to-configure-cors-in-s3-bucket-the-code-i-have-isnt-a-valid-json


Geocoding example:
https://www.codingforentrepreneurs.com/blog/python-tutorial-google-geocoding-api

### Acknowledgments

This project was created from a GitHub template made by [Code Institute](https://codeinstitute.net/) to recreate the terminal in a regular web browser.

The tutors Jo, Scott, John, Johann and Sean and my mentor Mo Shami at Code Institute, have helped me tremendously with this project. Also my good friend Daniel, who has guided me in understanding the basic concepts of OOP and data. Many thanks to them, and of course to the comprehensive course material from Code Institute.