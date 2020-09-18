[![Build Status](https://travis-ci.com/Fordalex/family_organiser.svg?branch=master)](https://travis-ci.com/Fordalex/family_organiser)

# Family Organiser 

This web application is designed to keep users in touch with their family and allow them to book events, share shopping lists, work together getting chores done, as well as write status and message one another. This idea came to me as in my house remembering to put the bins out and always running out of milk was getting a bit of a problem. I wanted to find a solution but one that I wasn't just in control of, as 'Teamwork makes the dream work', Adding API's and google authentication to speed up the user's interaction with the site was important as we're all short on time.

# UX

The overall app theme is green and white with hand drawn icons, I have tried to animate most of the intractions with the application but not to affect loading times. I feel this helps navigate the user to the desiered location and elicit a positive emotional response, making sure the user finds it easy to find their desired impormation and enjoy the process was quite important.

### User

On the profile page I have added a easiy visable '+' Add button so that if the user would like to add data to their profile this can easiy be achiveve. After this button has been pressed the page will open up revealing
a list of actions for the user to choose from, when one of these options has been selected they will ethier be navigated to their desired location or the page will dropdown further displaying a form for the user to fill out.

### Shopping

The first time the user loads this page or if they have no categories the page will be redirected to make sure the user has at least created one category. This is important because when saving an item, a category will have to be selected, this is to help break up their shopping list into different sections, helpful if their shopping and all their items for the 'frozen' foods are together. After an item has been created, it will be saved to a quick add section and the category already saved to that item for convenience.
I have used Ajax to update the page when the user is adding via the quick add option but also when incrementing and decrementing items on their shopping list, reloading the page just didn't give the UX I was going for.

The navigation for this application has been added to the top of the page with three links 'List','Partners','Insight' for the user to easily navigate themself to the location they desire. Also, a shopping partner has been added to help users interact and take the load of big shopping duties.

Under the shopping app, I have added an insights section with a different section that I discuss under the features section. This has been added to make sure the user can see some visual representation for their data. Making sure the user can make the right decision on what foods to be consuming and help keep costs down where needed.

### Status

User's can create and interacte with each others status, liking and commenting to make sure that staying intouch with each other is very important with this appliation.


### Messages

Also a messages app has been created so that users can communicate with one another, I would like to add a email API to this to make sure the user gets notified or somehow get the appliation to notify the user's device.

### Event

Finally this app has been created so that events for holidays, birthdays, days out, any event the user desired can be created with ease. After a event has been created the creator of the event can then invite users from ther family/friends list. I have added some confetti to the invitation to again try and give the user a positive responce when opening their event notification.

### Premium 

Some features to this app are for premium users only, this is the that the cost of hosting the application can pay for itself. The payment is a one off payment only can be easily achieved by the be navigated to the premium app and giving their bank details.

### Notifiations

I have added notifications on the profile page for liked posts, commented posts, accepted friend requests and partner requests. Also, events can be add to the users Google Calendar to make sure they don't miss any events!


## Project plan

[Wireframe](https://github.com/Fordalex/family_organiser/blob/master/project_plan/wireframe/mobile.PNG),
[User Stories](https://github.com/Fordalex/family_organiser/blob/master/project_plan/user_stories/user_stoires.JPG),
[Database Schema](https://github.com/Fordalex/family_organiser/blob/master/project_plan/database_schema/Web%201920%20%E2%80%93%201.png)

# Features

## Existing Features

### User

- A user can add their own profile image and bio from their profile, also they can see a count of their family.

- From the 'family' page a list of all the user's friends/family can be found, from this page, users can click on family member and be taken to view their profile. On a users profile their family list can also be viewed.

- The search for a member page is easy to locate from the add button or be redirected from the family page, the users will be able to send requests to their chosen user with ease.

- When a user likes, comments, send a friend request or an event, all this information can be found on their notifications page, also the user can click these notifications and be taken to the relevant page.

- Users can view/edit their personal information and remove their account from the settings page.

- A Status can be created from the profile page and seen on both their profile page and the news feed.

### Status

- All users status from their family list will be displayed on this page, also the user can create their status from here.

- If there are more than two comments on a post, user's can click 'more' and be taken to a personal page to view all the activity for that status.

- A Status can be created with a title, description and even an image.

### Shopping

- A custom shopping list can be created with categories and items. Items that are added to their shopping list will be saved to a quick add vertical scroll section just above their shopping list. The quick add section is ordered by the users most added items first. Also, items quantity can be incremented and decremented directly from the shopping list without the page having to be refreshed.

#### Shopping (Premium)

- Users can invite people from their friend's list to help them with their shopping, adding, removing and editing items in the same shopping list!

- An insights page has been created so that users can view their purchased items and see some useful data from their day to day habits. A monthly report will be automatically created from the user's purchased items list, this will be viewed by the users as a table. Also from this table, a line graph can then be easily created, bar charts have also been added so the user can view their most purchased items.

- The user can also see their personal insights for their shopping list or a collection of everyone's data that has been added as a shopping partner, giving them stats for their household or personal information. This can easily be filtered from the top of the page.

### Messages

- User's can search and create new conversation with people in their friends list, a notification will be sent to the user on their profile page to alert them that a message has been sent to them.


### Events (Premium)

- Events have been added so that users can book appointments/days out and other important events with their family and friends.

- An event is created with a title, description, time slot and location of where is event will be taken place, after the event is created the user can then invite their chosen participants.

- A notification will be sent to each user that has been invited, a invitation page be shown after the notification has been selected. On this page the user can remove the invite or accept, adding them to the event.

- Also the user can save this event to their Google Calendar with just one click at the top of the page. This has been added to make sure the user dosen't forget any events coming in the future.

[Top 10 Features](https://github.com/Fordalex/family_organiser/blob/master/readme/features.md)

## Features Left To Implement

### Shopping page

- Allow the user to add an item to their purchased items list.

- Preset shopping lists for users to create custom lists to save their time and help them stay organised and buy the right foods.

- Removing a shopping partner

### Messages

- Delete a coversation and the messages.

- React to a users message e.g. like, sad, happy

### Events

- Allow users attending the event to create messages on the event page.

### Merch Shop

I would like to add a merch shop for users to purchase back to school equitment and other family related items.

- Also allow users to create custom pages to sell their own items.

### Premium

Also I am going to add a order number when the user makes a purchase so that their order can be tracked if there are problems with their payment. Meanwhile this will be tracked using stripe.

## Bugs

### Shopping page

- If an item is removed by the quantity being set the zero and then the item is re-added, the item will be added twice by the same user (Shopping list).

### Messages

- On reload the page will resend the users message again.

### Status

- When a user is removed their status are removed but not comments on their status. Same when removing a status the comment stay in the database.

### Navigation

- When you change from mobile view to desktop view the white alpha over stays on the screen untill clicked or the page is reloaded.

### Event

- The time when saving an event to google calendar the time slot is one hour off...



## Technologies Used

#### Programs

- [Adobe XD](https://www.adobe.com/products/xd.html)

- [Photoshop](https://jquery.com)

- [Adobe Illustrator](https://www.adobe.com/uk/products/illustrator.html)

#### Frontend

- Languages
    - HTML
    - CSS
    - JavaScript

- Framework
    - [Bootstrap4](https://getbootstrap.com/)

- Preprocessor
    - [SCSS](https://sass-lang.com/)

- Js Libaries
    - [GSAP](https://greensock.com/)
    - [Chart.js](https://www.chartjs.org/)
    - [Jquery](https://jquery.com/)
    - [Confetti](https://github.com/GeekLaunch/confetti)

#### Backend

- Languages
    - Python

- Framework
    - Django

- Python modules
    - Gunicorn
    - dj_database_url
    - psycopg2-binary
    - [Stripe]()
    - pillow

## Testing 

I have tried to automate most of the important tests. Also, I have created a functions.py file to make sure the code is easier to read and to make sure that functions that work, can be resued to reduce the amount of bugs.

The views on each app either return the desired page or redirect the user when needed, this has been tested on the test_view.py and I've used coverage to make sure adequate testing has been done.

I have tested some of the larger functions under the test_functions.py.

[Manual Testing](https://github.com/Fordalex/family_organiser/blob/master/readme/testing.md)

## Deployment

I've hosted this project on heroku and also used Travis to make sure the build will pass. Also with this project the static files such as the css, js and images have been hosted using Amazon AWS. The project was hosted by doing the following:

#### Heroku

1. Creating a Procfile with information for heroku on what type of project this is.
2. Creating a requirements.txt file for the python dependencies to be installed to run the application by typing the following command into the terminal 'pip freeze --local > requirements.txt'. 
3. Then creating a new project on heroku.
4. Finally adding the environment variables and deploying the branch.

#### Amazon AWS

1. After loggin into my Amazon account, I search for s3 and create a new bucket and set the access to public.
2. Change the properties to static website hosting.
3. Then under the premissions tab I've added the CORS configuration.
4. Move to the bucket policy I generated a policy type of S3 and the action of 'GetObject'
5. Last configuration setting is under the 'access control list', and I've set the list objects permission to everyone.
6. After thats done I've moved over to IAM and created a new group.
7. Then I created a new policy and imported a manage policy called 'AmazonS3FullAccess'.
8. Next I've added the bucket ARN to the key 'Resource'.
9. Now I'll add the new policy to the group I created eariler.
10. Then creating a user to be added to the group and giving them programmatic access.
11. I then downloaded the csv file after the user was created.

#### Connecting Django to the S3 bucket

Back to the project, two new packages need to be installed for this to work.

1. boto3
2. django-storages

Then I've added the access key and the secret access key to the settings.py file and saving these values as environment variables. These variable were also saved in heroku under 'Confg Vars' for security reasons.

#### Running This Project Locally

- Frontend Method (Download)
    1. Go to [Family Organiser Project](https://github.com/Fordalex/power-in-numbers)
    2. Click on
    3. Click download zip
    4. Extract zip file
    5. Import into preferred IDE

- backend Method (Git)
    1. Open your terminal in your preferred IDE.
    2. Type "git clone https://github.com/Fordalex/power-in-numbers".
    3. A Virutal environment will need to be created, if your using linux the following command is 'python3 -m venv .venv'.
    4. Then 'source .venv/bin/activate' to activate the environment.
    5. The following command will install the dependencies for this project 'pip install -r requirements.txt'.
    6. Finally again in the terminal write 'pyton app.py' to run the application.

If running this project locally you will need to add a file call 'env.py', with the following values:
- DATABASE_URL
- SECRET_KEY
- STRIPE_PUBLIC_KEY
- STRIPE_SECRET_KEY
- EMAIL_HOST_USER
- CRED (Used for the Google Calendar API)
- OAUTHLIB_INSECURE_TRANSPORT
- OAUTHLIB_RELAX_TOKEN_SCOPE

## Credits

### Media

[Profile Image](https://illlustrations.co/)

[Icons8 - Icons](https://icons8.com/icons/set/tick-list)

[Fontawesome - Icons](https://fontawesome.com/)

[Undraw - Illustarations](https://undraw.co/illustrations)

### Acknowledgements

[The Basics for sass - Sass](https://www.youtube.com/watch?v=Zz6eOVaaelI&t=651s)

[Google login - Django](https://www.youtube.com/watch?v=ZTBexYIIOP8&t=333s)

[Custom User Registration - Django](https://www.youtube.com/watch?v=66l9b2QrBR8)

[Adding Friends - Django](https://www.youtube.com/watch?v=_DqmVMlJzqA&t=538s)

[ImageField - Django](https://www.youtube.com/watch?v=Rr1-UTFCuH4)

[Sorting array of objects - Python](https://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-based-on-an-attribute-of-the-objects)

[Setting up Ajax](https://www.youtube.com/watch?v=LLBx4beHI1U)

[Lambda - Python](https://www.youtube.com/watch?v=Ob9rY6PQMfI)

[strftime - Python](https://strftime.org/)

[Remove duplicates form an array - Python](https://www.w3schools.com/python/python_howto_remove_duplicates.asp)

[Creating a random number - Python](https://machinelearningmastery.com/how-to-generate-random-numbers-in-python/)

[AJAX and Django csrf_token](https://stackoverflow.com/questions/6506897/csrf-token-missing-or-incorrect-while-post-parameter-via-ajax-in-django)

[JsonResponse - Django](https://stackoverflow.com/questions/34971605/django-version-of-flask-jsonify-jsonify)

[Using Jquery to update page](https://www.youtube.com/watch?v=Kcka5WBMktw)

[Scroll To Top - Jquery](https://stackoverflow.com/questions/19012495/smooth-scroll-to-div-id-jquery)

[Comprehensions - Python](https://www.youtube.com/watch?v=3dt4OGnU5sM)

[If user is anonymous](https://stackoverflow.com/questions/4642596/how-do-i-check-whether-this-user-is-anonymous-or-actually-a-user-on-my-system/4642607)

[Styling forms using forms.py - Django](https://www.youtube.com/watch?v=Y4ieyOCC3gU)

[Using is_valid() - Django](https://www.youtube.com/watch?v=qwE9TFNub84)

[login required - Django](https://docs.djangoproject.com/en/3.0/topics/auth/default/)

[Client login test - Django](https://stackoverflow.com/questions/2705235/django-test-failing-on-a-view-with-login-required)

[Creating A Custom Scroll Bar - CSS](https://www.w3schools.com/howto/tryit.asp?filename=tryhow_css_custom_scrollbar2)

[Between two dates - Python](https://stackoverflow.com/questions/7274267/print-all-day-dates-between-two-dates/7274316)

[If request get_full_path](https://stackoverflow.com/questions/7462398/django-template-if-tag-based-on-current-url-value)

[Tracate and Slice - Django Templating Language](https://stackoverflow.com/questions/5235994/django-template-tag-to-truncate-text)

[Animate scroll - Jquery](https://stackoverflow.com/questions/1144805/scroll-to-the-top-of-the-page-using-javascript)

[ManyToMany count - Django](https://stackoverflow.com/questions/27149984/django-how-to-get-count-for-manytomany-field)

[Format date - Django](https://stackoverflow.com/questions/7737146/how-can-i-change-the-default-django-date-template-format)

[Confetti.js](https://github.com/GeekLaunch/confetti)

[Google calendar](https://developers.google.com/calendar/quickstart/python)

[Working on a server - Google calendar](https://github.com/googleapis/google-api-python-client/issues/755)

[Adding server-side oauth - Google calendar](https://developers.google.com/identity/protocols/oauth2/web-server#python_1)

[Authorisation changed - Google Calendar](https://stackoverflow.com/questions/51499034/google-oauthlib-scope-has-changed)

[INSECURE_TRANSPORT - Google Calendar](https://requests-oauthlib.readthedocs.io/en/latest/examples/real_world_example.html)