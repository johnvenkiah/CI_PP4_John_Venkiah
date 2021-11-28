# InstruMental

## A classified ads site for used music related items.

![Mockup of Instrumental](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/screenshots/mockup.png)

**InstruMental - a forum for users to buy and sell used musical instruments and gear.**

[Click here](https://instru-mental.herokuapp.com/) to visit the deployed site.

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

1. As a user, I can easily navigate to anywhere of relevance on the site by scrolling to the top of the page and clicking a link

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

### Epic 4: User Profiles - User Stories

13. As a registered user, I can create edit or remove a user profile, so that I and others can easily view my ads and personal info

14. As a registered user, I can view other sellers ads on their profiles

### Epic 5: The Ad Detail Page - User Stories

15. As a user, I can view a picture and a description of the item on the Ad Detail page

17. As a registered user, I can view options to post and edit ads, so that I can create, read, update and delete my ad
18. As a logged in user, I can mark my item as sold, so that other users are aware of this

### Epic 6: The Contact Page - User Stories

19. As a user, I can view a contact page so that I can easily contact the site owner if needed, whether I am registered or not

### Epic 7: Admin/Site-Owner Functionality - User Stories
20. As a site owner, I can access an admin page, where I can view all ads and profiles, and delete them if necessary
21. As a site owner, I receive an email when users submit the contact form, so that I can reply to them



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

**User stories/site-owner goals covered:**

1. As a user, I can easily navigate to anywhere of relevance on the site by scrolling to the top of the page and clicking a link

5. As a user, If I am not signed in, I am redirected to sign in/up if I click on any of the links or buttons restricted to logged in users

6. As a user, I get direct response and confirmation of my actions made on the website

___
#### Feature 2: The Home Page

![Home Page](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/features/feature_two_desktop.png)

The Home page consists of a search form, a hero image, links for the different categories and three feature cards.

In the search form, I 

**User stories/site-owner goals covered:**

1. Easily navigate the websites pages via the menu or links provided

2. Be presented with a well designed, user-friendly interface

3. Experience the same quality in design, user interaction and structure on small mobile devices, tablets as on larger screens.


#### Feature 3: The Quiz

![The Quiz](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/features/feature_3_quiz_mobile.png)

The quiz is a seemingly simple feature, but with a lot of functionality. The user has 60 seconds to answer the most questions correctly.

The quiz has several sub-features of its own:

- The staffbox

![Staffbox](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/features/staffbox.png)

Displays an image of the note in question for the user to answer. When answered, the image is updated to display the next note in question.

- The answers box



On opening the page, the answers box contains one button: "Lets Play!"

Clicking on this starts the quiz and displays four buttons, with three incorrect and one correct answer. The value of these buttons are updated for each question answered.

If the user clicks on the incorrect answer button, the user is alerted that this was incorrect by sounds and animation, and the user is informed of the correct answer.

If the user clicks on the correct answer-button, the user is greeted with a different sound and animation, and and the score above is incremented.

- The Timer

This keeps track of the time, once the user has clicked "Let's Play!"; the timer counts down from 60 to 0.

- The Score

Once a user has answered a question correctly, the score is incremented with 10 points. The score is then displayed in an end game modal.

- The End Game Modal

This is displayed once the 60 seconds are up, covering the screen. The user is greeted with one of five different greetings, depending on the score they have achieved.

The modal window also displays two buttons with choices for the user; "Play Again" and "Close".

**User stories/site-owner goals covered:**

2. Be presented with a well designed, user-friendly interface

3. Experience the same quality in design, user interaction and structure on small mobile devices, tablets as on larger screens

4. Get responses and confirmation from the website by my interactions with it

5. Be able to play a quiz on note names, symbols and note lengths

6. Get points if I answer a question right

7. See a timer ticking down from one minute

8. See an end game screen alerting me of my score and how the quiz went

9. Be able to choose to close the end game screen or play again

16. Display a menu in a navigation bar or popout menu at the top of the page

17. Display a quiz for users to test their knowledge

21. Have a website that contains validated HTML, CSS and JavaScript


#### Feature 4: The Piano (Play Page)

![The Piano](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/features/feature_4_piano_desktop.png)

The play page has two sub-features, a miniature piano and a stave showing both the bass clef and treble clef. When the user clicks a key, the relevant note displays on the stave together with the note name. The correct note is also heard when clicking it.

**User stories/site-owner goals covered:**

2. Be presented with a well designed, user-friendly interface

3. Experience the same quality in design, user interaction and structure on small mobile devices, tablets as on larger screens

4. Get responses and confirmation from the website by my interactions with it

10. Be able to play notes on a piano on the screen and see which tone is being played

11. Be able to play the notes on the computer keyboard

19. Display a page where users can play the piano and view the note played

21. Have a website that contains validated HTML, CSS and JavaScript


#### Feature 5: The Learn Page



Here, the user can navigate through a list of videos generated a search by the YouTube API, updating the list dynamically.
In the list, title, thumbnail and decription data is displayed for each video in the list.

Users can click on a video and view it in the main viewing window, located either to the left of the screen or at the top for mobile devices in portrait mode.

**User stories/site-owner goals covered:**

2. Be presented with a well designed, user-friendly interface

3. Experience the same quality in design, user interaction and structure on small mobile devices, tablets as on larger screens

4. Get responses and confirmation from the website by my interactions with it

12. View videos to learn about music theory and sight reading

18. Display a learn page containing the results of a YouTube search dynamically updated, using YouTube API

21. Have a website that contains validated HTML, CSS and JavaScript


#### Feature 6: The Contact Page

![Contact Page](https://github.com/johnvenkiah/CI_MS2_John_Venkiah/blob/master/docs/screenshots/features/feature_6_contact_mobile.png)

The "contact" page contains a simple form, where the user can fill in their name, email address and message, which they can send by clicking the submit-button.

The form is validated by the contact.js JavaScript file, and sent via the Email web service [EmailJS](https://www.emailjs.com/) to my email inbox.

**User stories/site-owner goals covered:**

3. Experience the same quality in design, user interaction and structure on small mobile devices, tablets as on larger screens

4. Get responses and confirmation from the website by my interactions with it

13. Get in touch with the site owner

20. Be able to be contacted should the user wish to do so, through an emailing service to my private email address

21. Have a website that contains validated HTML, CSS and JavaScript


#### Feature 7: The 404-error Page

The 404-error page is displayed when a user enters an invalid link within the website. From here, users can easily navigate to the other pages of the website.

**User stories/site-owner goals covered:**

3. Experience the same quality in design, user interaction and structure on small mobile devices, tablets as on larger screens

14. View an errors page if I have entered an invalid url within the website

21. Have a website that contains validated HTML, CSS and JavaScript



### Features to be implemented
___

This is a basic web application but could be expanded with all kinds of sections and functions. For example, there could be a play-by-ear section, where notes are played and the user has to answer which note. There could also be a chords-section, introducing chords and their uses in music. Users could create a profile, save videos they like, compete in high scores and a lot more.


## Technologies used

### Languages

- [Python 3](https://www.python.org/) - Was used solely to create this project.


### Applications, Platforms and Libraries


#### Applications and Platforms

- [Git](https://git-scm.com/) - Version control system used to commit and push to Github via Gitpod.

- [Github](https://github.com/) - The projects repository and all its branches were commited, pushed and deployed to Github.

- [Gitpod](https://gitpod.com/) - All code was written and tested using the Gitpod web-based IDE.

- [Heroku](https://www.heroku.com) - Used to deploy the application.

- [Lucidchart](https://lucid.co/product/lucidchart) - Lucidchart was used to create the [flowchart](#flowchart) of the project.

- [Google Calendar](https://calendar.google.com/) - The users input data creates and edits events on Google Calendar

- [Google Sheets](https://calendar.google.com/) - - The users input data creates and edits content on Google Sheets

- [Google Cloud Platform](https://console.cloud.google.com/) - All data send and received with the help of the Google API, through the Google Cloud Platform


#### Python Libraries

I have used these third party libraries and Python libraries for this project:

- datetime: As time is of essence when working with calendars, this was essential.

- os: By using os I was able to both have my password in the workspace without pushing it to github, but also use it as a config var on heroku.

- re: to be able to validate using regular expressions

#### Third Party Libraries

- googleapiclient.discovery: needed to work with the Google API

- google.oauth2.service_account: So the application can access the account that the sheet and calendar are on with the credentials

- gspread: so the application can read Google Spreadsheets




## Validation

All Python files passed the [PEP8](http://pep8online.com/) and [Pylint](https://www.pylint.org/) tests with 0 errors.

Click [here](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/validation/validation.md) to view them.



## Testing of Patient User Stories

User stories are tested with the features that cover them. All user stories passed the tests.


### Testing of user story 1

**"I would like to be able to book an appointment at a time of my choosing, should the appointement be available"**


**Covered by feature 1: The Patient Booking System**

<details>
    <summary>View image of initial steps of the booking</summary>

![User story 1, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_1_1.png)

</details>

- **Actions**:

    * *User hits "b" to begin*
    * *User enters "1" to agree on the application logging the patient data*
    * *User enters desired month of the appointment (Three letters)*
    * *User enters desired date (one or two figure numbers both work)*
    * *User is notified if the date is bookable*
    * *User enters desired hour of the appointment*
    * *User is notified if the timeslot is free or not*
    * *User enters their name*
    * *User enters their email*
    * *User enters their symptoms*
    * *User confirms by hitting "y"*
    * *User is greeted with their newly made booking*
    * *User can choose to go back to the beginning*

<details>
    <summary>View image of date validation here</summary>

![User story 1, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_1_2.png)

</details>

<details>
    <summary>View image of booking confirmation here</summary>

![User story 1, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_1_3.png)

</details>

 - Expected result: *To Make a successful booking at an available time*

 - Actual result: *Works as intended*


### Testing of user story 2

**"I would like to be alerted if my details are saved before I enter them"**


**Covered by feature 1: The Patient Booking System**

- **Action** - *In the welcome screen, user hits "b" to get to the booking screen*

- **Expected Result** - *Application displays message about storing data and user needs to confirm this to carry on*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image here</summary>

![User story 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_2.png)

</details>

### Testing of user story 3

**"I would like to be well informed from the application throughout the booking process"**


This user story is tested in the steps needed to make an appointment.

**Covered by feature 1: The Patient Booking System**

- **Action**: *User initiates a booking by pressing "b"*

- **Expected Result**: *Application displays message about storing data*

- **Actual Result**: *Works as intended*

<details>
    <summary>View image here</summary>

![User story 1, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_3_1.png)

</details>

___

- **Action** - *User hits "1" to continue*

- **Expected Result** - *Application asks user for the month they would like to come*

- **Actual Result** - *Works as intended*

___

- **Action** - *User enters the three first letters of the month that they want to come*

- **Expected Result** - *Application confirms the month entered and asks for the desired appointment date*

- **Actual Result** - *Works as intended*

___

- **Action** - *User enters the desired appointment date*

- **Expected Result** - *Application lets user know if the date is unbookable, (weekends for example) or if it is available to book, in which case the app confirms date and asks user for time of appointment*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image here</summary>


![User story 3, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_3_2.png)

</details>

___

- **Action** - *User enters hour of desired appointment time*

- **Expected Result** - *Application confirms the time and asks user for name if the desired appoinment time is free and bookable, otherwise lets the user know and user has to choose new time*

- **Actual Result** - *Works as intended*

___

- **Action** - *User enters their name*

- **Expected Result** - *Application Confirms the users name and asks for their email*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image here</summary>

![User story 3, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_3_3.png)

</details>

___

- **Action** - *User enters their email*

- **Expected Result** - *Application Confirms the users email address and asks user to enter their symptoms*

- **Actual Result** - *Works as intended*

___

- **Action** - *User enters their symptoms*

- **Expected Result** - *Application displays all the patient data retrieved and asks user to confirm appointment*

- **Actual Result** - *Works as intended*

___

- **Action** - *User confirms appointment*

- **Expected Result** - *Application displays confirmation, that patient data is logged and user can return to the main screen*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image here</summary>

![User story 3, 4](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_3_4.png)

</details>

### Testing of user story 4

**"I would like to be alerted if my choice is invalid anywhere in the application, and get a chance to try again"**


**Covered by feature 1: The Patient Booking System**


- **Action** - *User enters invalid value, or date/time that is not free*

- **Expected Result** - *Application let user know that the entry is invalid, and the user gets to try again*

- **Actual Result** - *Works as intended*

The testing of this user case is best portrayed with the images below. All areas of navigation have passed the tests.

<details>
    <summary>View images of user 4 testing results</summary>

*Invalid choices at home screen:*

![User story 4, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_1.png)

___

*Invalid choices when choosing month:*

![User story 4, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_2.png)

___

*Invalid choices when choosing date:*

![User story 4, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_3.png)

___

*Invalid choices when choosing weekend date:*

![User story 4, 4](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_4.png)

___

*Invalid choices when choosing an already booked timeslot:*

![User story 4, 5](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_5.png)

___

*Invalid choices when entering single word:*
![User story 4, 6](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_6.png)

___

*Invalid choices when entering invalid email:*
![User story 4, 7](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_7.png)

___

*Invalid choices when entering too short description of symptoms:*
![User story 4, 8](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_4_8.png)

</details>

### Testing of user story 5

**"I would like to be able to confirm the booking right before it is made"**


**Covered by feature 1: The Patient Booking System**

**Action** - *User completes booking and enters valid information throughout the booking process*

**Expected Result** - *User is asked to confirm the booking*

**Actual Result** - *Works as intended*

<details>
    <summary>View image here</summary>

![User story 5](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_1_3.png)

</details>

### Testing of user story 6

**"I would like to view a confirmation of the booking when it is made"**


**Covered by feature 1: The Patient Booking System**

- **Action** - *User confirms the booking made*

- **Expected Result** - *Application displays the details of the booking*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image here</summary>

![User story 6](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_6.png)

</details>


### Testing of user story 7

**"I would like to at any point cancel my booking during the booking process should I wish to do so"**


**Covered by feature 1: The Patient Booking System**

- **Action** - *User follows instructions to exit on screen*

- **Expected Result** - *Booking returns to the home screen or the previous stage*

- **Actual Result** - *Works as intended*

<details>
    <summary>View images here</summary>


![User story 7](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_7_1.png)

![User story 7, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_7_2.png)

</details>

## Testing of Staff Member User Stories


### Testing of user story 8

**"I would like for users to only be able to book appointments on weekdays between 9 and 17, and when the schedule is free"**


**Covered by feature 1: The Patient Booking System**

- **Action** - *User tries to make a booking on a weekend, outside the schedule or when a booking is already scheduled*

- **Expected Result** - *Patient is alerted that the time is invalid or unavailable*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image here</summary>

![User story 8](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_1_2.png)

</details>

### Testing of user story 9

**"I would like appointments made by new users add a new row with their information to the Google Sheets patient log"**


**Covered by feature 1: The Patient Booking System and feature 3, the Patient Log**

- **Action** - *User successfully books an appointment*

- **Expected Result** - *Patients information is added on a new row in the patient log on the Google spreadsheet, which is viewable in the application*

- **Actual Result** - *Works as intended*

<details>
    <summary>View images here</summary>

*A completed patient booking*

![User story 9, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_booking/p_booking_done.png)

*The patient log after booking*

![User story 9, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_log/patient_log.png)

*The Google Sheet after booking is made*
![User story 9, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_log/g_sheets_new.png)

</details>


### Testing of user story 10

**"I would like the appointments made by patients dynamically update my Google Calendar"**


**Covered by feature 1: The Patient Booking System**

- **Action** - *User successfully books an appointment*

- **Expected Result** - *Event on Google Calendar is created from input by user during booking*

- **Actual Result** - *Works as intended*

<details>
    <summary>View image of updated calendar here</summary>

![User story 9, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/google_cal/g_cal_new.png)

</details>


### Testing of user story 11

**"I would like the changes made in the schedules edit menu to update the events on my Google Calendar"**


**Covered by feature 2: The Schedule**

- **Action**: *User edits an appointment from the schedule*

- **Expected Result**: *The appointment is updated on Google Calendar with new data from user*

- **Actual Result**: *Works as intended*

<details>
    <summary>View images here</summary>

![user story 11, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_11_1.png)

![user story 11, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_11_2.png)

![user story 11, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_11_3.png)

</details>


### Testing of user story 12

*"I would like to be able to view the patient log"*

**Covered by feature 3: The Patient Log**

- **Action**: *User hits "l" in the staff area*

- **Expected Result**: *The patient log is displayed*

- **Actual Result**: *Works as intended*

<details>
    <summary>View image of the result</summary>

![User story 12](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/patient_log/patient_log.png)

</details>

### Testing of user story 13

*"I would like to view my schedule for the coming week"*

**Covered by feature 2: The Schedule**

- **Action**: *User hits "s" in the staff area*

- **Expected Result**: *The schedule is displayed*

- **Actual Result**: *Works as intended*

<details>
    <summary>View image of the result</summary>

![User story 13](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/images/schedule/schedule.png)

</details>

### Testing of user story 14

*"I would like to navigate between weeks in my schedule"*

**Covered by feature 2: The Schedule**

- **Action**: *User hits "n" or "b" when viewing the schedule*

- **Expected Result**: *The next week is displayed*

- **Actual Result**: *Works as intended*

<details>
    <summary>View image of the result</summary>

![User story 14](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_14.png)

</details>

### Testing of user story 15

*"I would like to be able to update or remove any appointment viewed in my schedule"*

**Covered by feature 2: The Schedule**

#### Edit appointment

- **Actions**:

* *User enters number of appoinment when viewing the schedule*
* *User chooses what to edit; time, name or details*
* *User enters new time, name or details for appointment*
* *User confirms changes*


- **Expected Result**: *The event is updated on Google Calendar*

- **Actual Result**: *Works as intended*

<details>
    <summary>View images of editing appointments</summary>

*The edit menu*
![User story 15, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_15_1.png)

*Editing the date and time*
![User story 15, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_15_2.png)

*Changes are confirmed*
![User story 15, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_15_3.png)

*The Google event now has the new time*
![User story 15, 4](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_15_4.png)

</details>

#### Remove appointment

- **Actions**:

* *User enters number of appoinment when viewing the schedule*
* *User chooses what to edit; time, name or details*
* *User enters new time, name or details for appointment*
* *User confirms changes*


- **Expected Result**: *The event is removed from Google Calendar*

- **Actual Result**: *Works as intended*

<details>
    <summary>View images of removing appointment</summary>

*Choice to remove and confirmation once removed*

![User story 15, 5](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_15_5.png)

*The Google event is now nowhere to be seen*

![User story 15, 6](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_15_6.png)

</details>

### Testing of user story 16

*"I would like to easily be able to return to the main staff area in the application"*

**Covered by feature 2: The Schedule, and feature 3: The Patient Log**


- **Action**: *User follows the instructions to get to the staff menu*

- **Expected Result**: *Staff main menu is displayed*

- **Actual Result**: *Works as intended*

<details>
    <summary>Click to view images</summary>

*Returning from patient log to staff menu*

![User story 16, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_16_1.png)

*Returning from schedule to staff menu*

![User story 16, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_16_2.png)

</details>

### Testing of user story 17

*"I would like the staff area to be password protected"*

**Covered by all features**


- **Action**: *User enters "s" to view staff area*

- **Expected Result**: *User must enter password to continue*

- **Actual Result**: *Works as intended*

<details>
    <summary>Click to view image</summary>

*The password being displayed*

![User story 17](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_17.png)

</details>

## Testing of Site Owner Goals

### Testing of user story 18

*"I would like for the application to contain validated Python code without returning any errors, whatever the user does"*

**Covered by all features**


- **Action**: *User enters invalid information*

- **Expected Result**: *Application lets user know and user can enter info again*

- **Actual Result**: *Works as intended*

This was tested by trying all possible entries in all menus in the application. The application passed all validation tests which can be viewed [here](#validation), and user will be displayed with information in all menus if user input is incorrect.

<details>
    <summary>Click to view images</summary>

*Incorrect date entered, staff area*

![User story 18, 1](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_18_1.png)

*Incorrect month entered, patient booking area*

![User story 18, 2](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_18_2.png)

*Incorrect name entered, patient booking area*

![User story 18, 3](https://github.com/johnvenkiah/CI_PP3_John_Venkiah/blob/main/docs/testing_user_stories/user_story_18_3.png)

</details>

## Bugs

<details>
    <summary>View bugs here</summary>
___

**Bug**: When user tries to delete whole words with option delete on mac, nothing happens, then deleting the input has no effect on the string. Probable error with terminal and not in Python code.

**Fix**: Print message to users not to use this function in the application. No fix for the bug as of yet.
___

**Bug**: User can navigate with arrows anywhere in the terminal window, entering input here renders the printed text in a false manner.

**Fix**: Print message to users not to use this function in the application. No fix for the bug as of yet.
___


**Bug**: Error when entering month "oct" in patient booking system

**Fix**: Correct typo "Okt" in month dictionary, create try and except to catch time format value errors
___

**Bug**: Error ``code: 500, APIerror`` when calling the sheets API

**Fix**: Only happened once, difficult to recreate. Created a "try", "except" to catch API errors when calling the sheets API
___

**Bug**: Checking schedule displayed twice

**Fix**: Change code so things happen in correct order
___

**Bug**: Password hiding library import stdiomsk doesn't work on terminal in Heroku and produced ``termios.error: 25, 'Inappropriate ioctl for device'``

**Fix**: Remove stdiomsk and let password entered be shown
___

**Bug**: Datetime parsing not working, returning errors

**Fix**: Create TimeFConverter class, convert formats with that
___

**Bug**: Says date incorrect although it is correct

**Fix**: Fix while loop and indentation in get date function
___

**Bug**: Sheets updating wrong cell when user exists

**Fix** code at end of sheet.py; use update_cell sheets method
___

**Bug**: Schedule displaying wrong weeks when navigating through weeks, out of schedule back in and then showing next week again

**Fix**: Add initialize method to IncDecWeek class, so when user exits, the weeks count resets
___

**Bug**: Some lines appearing without space below

**Fix**: Add new line to print and input strings where relevant
___

**Bug**: "e" didn't let user exit

**Fix**: Add paretheses to e_to_edit function
___

**Bug**: Error when selecting date in month that has passed

**Fix**: Changed datetime method to year that was wrongly named as variable "yr"

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

### Google API

Here's how you can set up your own API:

1. Login or create a Google account and navigate to https://console.cloud.google.com/
2. Create a new Project by clicking on the New Project icon
3. Add Project name and details
4. Under API's and services, enable the relevant API for your project (in this case Google Drive, Sheets and Calendar)
5. IF the API requires, create a credential (service account in this case) for your project
6. Download the credential and upload it to your workspace a a json-file
7. Under API's and services, enable the relevant API for your project (in this case Google Drive, Sheets and Calendar)
8. Search for the needed tasks to be performed in the documentation for the specific API, for example here for the calendar API: [Google Calendar API Reference](https://developers.google.com/calendar/api/v3/reference?hl=en)
9. Add them to your code.


## Credits

Here are links to sites that answered a lot of my questions on coding and the Python language.

### Coding tips and tricks

Overriding false errors when Flake and Pylint validate code:

[StackOverflow, pyflakes](https://stackoverflow.com/questions/8427701/how-to-ignore-pyflakes-errors-imported-but-unused-in-the-init-py-file)

[StackOverflow, pylint](https://stackoverflow.com/questions/26657265/hide-some-maybe-no-member-pylint-errors)

Creating a class to increment and decrement a number free from functions: [Stack Overflow](https://stackoverflow.com/questions/47697945/python-how-to-increment-number-and-store-in-variable-every-time-function-runs/47698278)

Using the dictionary zip function to join two lists: [StackOverflow](https://stackoverflow.com/questions/209840/how-do-i-convert-two-lists-into-a-dictionary)

Creating a user login:[StackExchange](https://codereview.stackexchange.com/questions/164359/python-username-and-password-program)

Using the python datetime library: [docs.python.org](https://docs.python.org/3/library/datetime.html)

Calculating a leap Year with a conditional statement: [geeksforgeeks.org](https://www.geeksforgeeks.org/program-check-given-year-leap-year/)

Regular expression for validating email: [Stack Overflow](https://stackoverflow.com/questions/8022530/how-to-check-for-valid-email-address)

Using the isnumeric function: [delftstack.com](https://www.delftstack.com/howto/python/user-input-int-python/)

### Acknowledgments

This project was created from a template made by [Code Institute](https://codeinstitute.net/) to recreate the terminal in a regular web browser.

The tutors Scott and Sean and my mentor Mo Shami at Code Institute, have helped me in times of trouble. Many thanks to them, and of course to the comprehensive course material from Code Institute.