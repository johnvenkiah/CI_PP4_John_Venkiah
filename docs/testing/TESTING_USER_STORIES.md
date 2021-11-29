# Testing of User Stories, InstruMental

### Testing of user story 1

**"As a user, I can easily navigate to anywhere of relevance on the site by scrolling to the top of the page and clicking a link"**


**Covered by feature 1: The Navbar**

![User story 1](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/features/navbar.png)


- **Action** - *User scrolls up to top*

- **Expected result** - *To be redirected to the desired link url*

- **Actual result** - *Works as intended*


### Testing of User Story 2 and 3

**1. "As a user, I can perform a search so that a list of items for sale is generated"**

**2. "As a user, As a user, I can refine my search so that the results display items in a specific location or category."**

**Covered by feature 2: The Home Page / Search**

- **Action** - *User navigates to the home page and performs a search in the search form*

- **Expected Result** - *Search result are displayed according to the users search criteria*

- **Actual Result** - *Works as intended*

![User story 2](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/search.png)


![User story 3](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/search_result.png)


### Testing of User Story 4

**"As a user, I can click on an item so that I can view its details"**

**Covered by feature 3: The User Profile**

- **Action** - *User performs a search and gets the ad results and clicks on an ad*

- **Expected Result** - *The relevant ad is displayed*

- **Actual Result** - *Works as intended*

![User story 4, 1](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/ad_detail_image.png)


### Testing of User Story 5

**"As a user, If I am not signed in, I am redirected to sign in/up if I click on any of the links or buttons restricted to logged in users"**

**Covered by feature 3: The User Profile**

- **Action** - *User is not logged in and click on the profile, or post as link*

- **Expected Result** - *User is redirected to the Sign In Page*

- **Actual Result** - *Works as intended*

![User story 5, 1](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/profile_link.png)

![User story 5, 3](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/sign_in_image.png)


### Testing of User Story 6

**"As a user, I get direct response and confirmation of my actions made on the website"**

**Covered by all features**

- **Actions** - *User performs searches, adds info to their profile, posts ad, removes ad.*

- **Expected Result** - *The content changes as the user interacts with it*

- **Actual Result** - *Works as intended*

![User story 6](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/profile_updated.png)


### Testing of User Story 7

**"As a user, I can sign up, so that I can utilise the full functionality of the website"**

**Covered by all features**

- **Action** - *User clicks sign in from the navbar or a link on the home page*
- **Expected Result** - *The User is able to sign in*

- **Actual Result** - *Works as intended*

![User story 7](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/sign_in.png)

### Testing of User Story 8

**"As a registered user, i would like my login info and the ability to edit my personal ads be restricted to me only"**

**Covered by Feature 4: Ad Post, Edit and Remove, Feature 3: The User Profile**

- **Action** - *Other user visits users profile*

- **Expected Result** - *edit buttons are not visible in other profiles than their own*

- **Actual Result** - *Works as intended*

![User story 8, 1](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/edit_ad_button.png)

![User story 8, 2](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/not_editable_ad.png)


### Testing of User Story 9

**"9. As a registered user, I can receive a new password if it is forgotten, so that i can login to the site again"**

**Covered by Feature 0: Djangos Allauth feature (not written by me so I haven't included it in my features)**

- **Action** - *User clicks Forgot Password?*

- **Expected Result** - *User gets to enter their email and can recieve a link to retrieve a new password*

- **Actual Result** - *Works as intended*

![User story 9](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/password_reset_image.png)


### Testing of User Story 10

**"9. As a registered user, I would like to see a “Sign in/Sign Out” option, so that i can sign in or out"**

**Covered by Feature 0: Djangos Allauth feature (not written by me so I haven't included it in my features)**

- **Action** - *User wants to sign in*

- **Expected Result** - *The sign in button visible is on several places on the site*

- **Actual Result** - *Works as intended*


### Testing of User Story 11

**"9. As a logged in user, I can view other sellers profiles"**

**Covered by Feature 3: The User Profile and Feature 5: Ad Post, Edit and Remove**

- **Action** - *User clicks on sellers name in ad detail page*

- **Expected Result** - *User is brought to the sellers profile*

- **Actual Result** - *Works as intended*

![User story 11](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/others_profile.png)


### Testing of User Story 12

**"9. As a logged in user, i can save ads to a “saved” list so that I can easily view them later"**

**Covered by Feature 3: The User Profile and Feature 6. The Ad Detail Page**

- **Action** - *User clicks on Saved button in ad detail*

- **Expected Result** - *Button turns red and ad is saved on current users profile*

- **Actual Result** - *Works as intended*

![User story 12](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/not_editable_ad.png)



### Testing of User Story 13, 14, 15

**"13. As a logged in user, I can add a street to the location field in my profile and it will automatically appear as my default location when I post a new ad"**

**"14. As a logged in user, as I enter a street, the location field fills in an actual adress for me to choose."**

**"15. As a registered user, my city but not my street is saved on my public profile, so that others cannot see my exact address."**

**Covered by Feature 6: The Location Field**

- **Action** - *User enters UK street in location field*
- **Expected Result** - *Field returns an actual address with that street*

- **Action** - *User clicks on Post Ad*
- **Expected Result** - *Location Field is prefilled with the profile location*

- **Action** - *User views a different profile*
- **Expected Result** - *Location Field displays city, not street of seller*

- **Actual Result** - *Works as intended*

![User story 16](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/location_field.png)

### Testing of User Story 16

**"16. As a registered user, I can create edit or remove a user profile, so that I and others can easily view my ads and personal info"**

**Covered by Feature 3: The User Profile, Feature 4: Ad Post, Edit and Remove**

- **Action** - *User enters their profile and clicks Edit Profile*

- **Expected Result** - *The Edit Profile Page is displayed and the user can update and remove all details*

- **Actual Result** - *Works as intended*

![User story 16](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/edit_profile_image.png)


### Testing of User Story 17

**"17. As a registered user, I can view other sellers ads on their profiles"**

**Covered by Feature 3: The User Profile, Feature 4: Ad Post, Edit and Remove**

- **Action** - *User clicks on the sellers name in the ad detail page*

- **Expected Result** - *The users profile is displayed with their ads*

- **Actual Result** - *Works as intended*

![User story 16](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/others_profile.png)



### Testing of User Story 18

**"18. As a user, I can view a picture and a description of the item on the Ad Detail page"**

**Covered by Feature 5: The Ad Detail Page**

- **Action** - *User enters the ad detail pagee*

- **Expected Result** - *A picture and a description is displayedin on the page*

- **Actual Result** - *Works as intended*

![User story 16](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/ad_detail_image.png)



### Testing of User Story 19

**"19. As a registered user, I can view options to post and edit ads, so that I can create, read, update and delete my ad"**

**Covered by Feature 4: Ad Post, Edit and Remove, and Feature 5: The Ad Detail Page**

- **Action** - *User sees the Post Ad button in the navbar, or clicks the edit button in the ad detail page*

- **Expected Result** - *The user can view, post, update and delete an ad*

- **Actual Result** - *Works as intended*

![User story 16](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/edit_profile_image.png)



### Testing of User Story 20

**"20. As a logged in user, I can mark my item as sold, so that other users are aware of this"**

**Covered by Feature 4: Ad Post, Edit and Remove, and Feature 5: The Ad Detail Page**

- **Action** - *User clicks the sold checkbox in the edit ad page*

- **Expected Result** - *The ad is now marled as sold for all users*

- **Actual Result** - *Works as intended*

![User story 16](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/edit_profile_image.png)



### Testing of User Story 21

**"21. As a user, I can click a share button in the ad detail page, so that I can share it on social media platforms"**

**Covered by Feature 5: The Ad Detail Page**

- **Action** - *User clicks the share button in the ad detail page*

- **Expected Result** - *A popup modal with share links appears*

- **Actual Result** - *Works as intended*

![User story 16](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/share.png)



### Testing of User Story 22

**"22. As a user, I can view a contact page so that I can easily contact the site owner if needed, whether I am registered or not"**

**Covered by Feature 7: The Contact Page**

- **Action** - *User clicks the contact link in the navbar*

- **Expected Result** - *A contact form appears for users to fill in their contact detatils and messag*

- **Actual Result** - *Works as intended*

![User story 16](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/contact_image.png)



### Testing of User Story 23

**"23. As a site owner, I can access an admin page, where I can view all ads and profiles, and delete them if necessary"**

**Covered by Feature 8: The Contact Page**

- **Action** - *User clicks the admin link at the bottom of the page*

- **Expected Result** - *The admin page is displayed and the site owner can log in*

- **Actual Result** - *Works as intended*

![User story 16](https://github.com/johnvenkiah/CI_PP4_John_Venkiah/blob/main/docs/testing/admin_immage.png)



### Testing of User Story 24

**"24. As a site owner, I receive an email when users submit the contact form, so that I can reply to them"**

**Covered by Feature 7: The Contact Page**

- **Action** - *User fills in and sends the contact form*

- **Expected Result** - *The admin has now recieved an email fromm the user*

- **Actual Result** - *Works as intended*