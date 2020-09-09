[![Build Status](https://travis-ci.com/Fordalex/family_organiser.svg?branch=master)](https://travis-ci.com/Fordalex/family_organiser)

# Family Organiser 

This web application is designed to keep users in touch with their family and allow them to book events, share shopping lists, work together getting chores done, as well as write status and message one another.

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

## Features

### Profile

- A Family list of all the user's friends/family can be found, from this page, users can click a profile and be take to a view of a users profile, on a users profile their family list can also be viewed.

- Search for a family member is easy to locate from the add button or family page, the users will be able to send requests to their chosen member.

- When a user's likes, comments, send a friend request or an event, all this information can be found on their notifications page, also the user can click these notifications and be taken to the relevant page.

- Users can view/edit their personal information and remove their account on the settings page.

- A Status can be created from the profile page and seen on both their profile page and the news feed.

### status

- All users status from their family list will be displayed on this page, also the user can create their status from here.

- If there are more than two comments on a post, user's can click 'more' and be taken to a personal page to view that status.

### shopping

- A custom shopping list can be created with categories and items that are added to their list will be saved to a quick add vertical scroll just above the list. The list is ordered by the users most added items first, items quantity can be incremented and decremented without the page having to be refreshed.

- Users can invite people from their friend's list to help them with their shopping, adding, removing and editing items in the same shopping list!

- An Insights page has been created so that users can view their purchased items and see some useful data from their day to day habits. 

### messages

### events







## Bugs

### Shopping page

- If an item is removed by the quantity being set the zero and then the item is re-added, the item will be added twice by the same user (Shopping list).

### Messages

- On reload the page will resend the users message again.

### Status

- When a user is removed their status are removed but not comments on their status. Same when removing a status the comment stay in the database.

### Navigation

- When you change from mobile view to desktop view the white alpha over stays on the screen untill clicked or the page is reloaded.

## Features to add

### Shopping page

- Allow the user to add an item to their purchased items list.

- Preset shopping lists for users to create custom lists to save their time and help them stay organised and buy the right foods.

### Messages

- Delete a coversation and the messages.

- React to a users message e.g. like, sad, happy

### Events

- Allow users attending the event to create messages on the event page.

### Merch Shop

I would like to add a merch shop for users to purchase back to school equitment and other family related items.

- Also allow users to create custom pages to sell their own items.

## How to run locally:

#### Download:

#### Using Git:

## Deployment

## Credits

### Content

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
