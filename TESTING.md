# Testing

Return back to the [README.md](README.md) file.

## Code Validation

### HTML

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.

| Page | W3C URL | Screenshot | Notes |
| --- | --- | --- | --- |
| Home | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Finstapilot-e1ebc8c013f4.herokuapp.com%2F) | ![screenshot](documentation/testing/html-testing-homepage.png) | Pass: No Errors |
| Register | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Finstapilot-e1ebc8c013f4.herokuapp.com%2Faccounts%2Fsignup%2F) | ![screenshot](documentation/testing/html-p-register.png) ![screenshot](documentation/testing/html-p-error-register.png) ![screenshot](documentation/testing/html-error-register2.png) | Extra < p > and < /p > in the {{ form.as_p }} of the Allauth signup.html template |
| Login | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Finstapilot-e1ebc8c013f4.herokuapp.com%2Faccounts%2Flogin%2F) | ![screenshot](documentation/testing/html-testing-login.png) | Pass: No Errors |
| Upload Post | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Finstapilot-e1ebc8c013f4.herokuapp.com%2Fupload_post) | ![screenshot](documentation/testing/html-testing-addpost.png) | Pass: No Errors |
| Details | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Finstapilot-e1ebc8c013f4.herokuapp.com%2Fdetails%2F13) | ![screenshot](documentation/testing/html-testing-details.png) | Pass: No Errors |
| Edit | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Finstapilot-e1ebc8c013f4.herokuapp.com%2F) | ![screenshot](documentation/testing/html-testing-edit.png) | Pass: No Errors |
| Logout | [W3C](https://validator.w3.org/nu/?doc=https%3A%2F%2Finstapilot-e1ebc8c013f4.herokuapp.com%2F) | ![screenshot](documentation/testing/html-testing-logout.png) | Pass: No Errors |


### CSS

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| File | Jigsaw URL | Screenshot | Notes |
| --- | --- | --- | --- |
| live site | [Jigsaw](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Finstapilot-e1ebc8c013f4.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en#errors) | ![screenshot](documentation/testing/css-testing.png) | Warnings and Errors relate to Bootstrap, FontAwesome and Leaflet |
| style.css | [Jigsaw](https://jigsaw.w3.org/css-validator/validator) | ![screenshot](documentation/testing/css-testing-stylecss.png) | Pass: No Errors |

### JavaScript

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| File | Screenshot | Notes |
| --- | --- | --- |
| base.html | ![screenshot](documentation/testing/js-testing-basehtml.png) | Pass: No Errors |
| edit_upload.html | ![screenshot](documentation/testing/js-testing-editeuploadhtml.png) | Pass: No Errors |
| upload_details.html | ![screenshot](documentation/testing/js-testing-uploaddetails.html.png) | Five warnings related to django code |
| upload_post.html | ![screenshot](documentation/testing/js-testing-uploadposthtml.png) | Pass: No Errors |

### Python

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| File | CI URL | Screenshot | Notes |
| --- | --- | --- | --- |
| settings.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/InstaPilot/main/main/settings.py) | ![screenshot](documentation/testing/python-testing-settingpy.png) | Pass: No Errors |
| urls.py (main) | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/InstaPilot/main/main/urls.py) | ![screenshot](documentation/testing/python-testing-urlsmain.png) | Pass: No Errors |
| admin.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/InstaPilot/main/pilot_posts/admin.py) | ![screenshot](documentation/testing/python-testing-adminpy.png) | Pass: No Errors |
| apps.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/InstaPilot/main/pilot_posts/apps.py) | ![screenshot](documentation/testing/python-testing-appspy.png) | Pass: No Errors |
| forms.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/InstaPilot/main/pilot_posts/forms.py) | ![screenshot](documentation/testing/python-testing-formspy.png) | Pass: No Errors |
| models.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/InstaPilot/main/pilot_posts/models.py) | ![screenshot](documentation/testing/python-testing-modelspy.png) | Pass: No Errors |
| urls.py (pilot_posts) | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/InstaPilot/main/pilot_posts/urls.py) | ![screenshot](documentation/testing/python-testing-urlspy.png) | Pass: No Errors |
| views.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/InstaPilot/main/pilot_posts/views.py) | ![screenshot](documentation/testing/python-testing-viewspy.png) | Pass: No Errors |
| manage.py | [PEP8 CI](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/JamesH003/InstaPilot/main/manage.py) | ![screenshot](documentation/testing/python-testing-managepy.png) | Pass: No Errors |


## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Browser | Home | Register | Add post | Edit post | Delete post |
| --- | --- | --- | --- | --- | --- |
| Chrome | ![screenshot](documentation/testing/browser-chrome-home.png) | ![screenshot](documentation/testing/browser-chrome-register.png) | ![screenshot](documentation/testing/browser-chrome-addpost.png) | ![screenshot](documentation/testing/browser-chrome-edit.png) | ![screenshot](documentation/testing/browser-chrome-delete.png) | Works as expected |
| Firefox | ![screenshot](documentation/testing/browser-firefox-home.png) | ![screenshot](documentation/testing/browser-firefox-register.png) | ![screenshot](documentation/testing/browser-firefox-addpost.png) | ![screenshot](documentation/testing/browser-firefox-edit.png) | ![screenshot](documentation/testing/browser-firefox-delete.png) | Works as expected |
| Edge | ![screenshot](documentation/testing/browser-edge-home.png) | ![screenshot](documentation/testing/browser-edge-register.png) | ![screenshot](documentation/testing/browser-edge-addpost.png) | ![screenshot](documentation/testing/browser-edge-edit.png) | ![screenshot](documentation/testing/browser-edge-delete.png) | Works as expected |
| Safari | ![screenshot](documentation/testing/browser-safari-home.png) | ![screenshot](documentation/testing/browser-safari-register.png) | ![screenshot](documentation/testing/browser-safari-addpost.png) | ![screenshot](documentation/testing/browser-safari-edit.png) | ![screenshot](documentation/testing/browser-safari-delete.png) | Works as expected |
| Brave | ![screenshot](documentation/testing/browser-brave-home.png) | ![screenshot](documentation/testing/browser-brave-register.png) | ![screenshot](documentation/testing/browser-brave-addpost.png) | ![screenshot](documentation/testing/browser-brave-edit.png) | ![screenshot](documentation/testing/browser-brave-delete.png) | Works as expected |
| Opera | ![screenshot](documentation/testing/browser-opera-home.png) | ![screenshot](documentation/testing/browser-opera-register.png) | ![screenshot](documentation/testing/browser-opera-addpost.png) | ![screenshot](documentation/testing/browser-opera-edit.png) | ![screenshot](documentation/testing/browser-opera-delete.png) | Works as expected |

## Responsiveness

I've tested my deployed project on multiple devices to check for responsiveness issues.

| Device | Home | Register | Add post | Edit post | Notes |
| --- | --- | --- | --- | --- | --- |
| Mobile (DevTools) | ![screenshot](documentation/testing/responsive-phone-home.png) | ![screenshot](documentation/testing/responsive-phone-register.png) | ![screenshot](documentation/testing/responsive-phone-addpost.png) | ![screenshot](documentation/testing/responsive-phone-edit.png) | Works as expected |
| Tablet (DevTools) | ![screenshot](documentation/testing/responsive-tablet-home.png) | ![screenshot](documentation/testing/responsive-tablet-register.png) | ![screenshot](documentation/testing/responsive-tablet-addpost.png) | ![screenshot](documentation/testing/responsive-tablet-edit.png) | Works as expected |
| Desktop | ![screenshot](documentation/testing/browser-chrome-home.png) | ![screenshot](documentation/testing/browser-chrome-register.png) | ![screenshot](documentation/testing/browser-chrome-addpost.png) | ![screenshot](documentation/testing/browser-chrome-edit.png) | Works as expected |
| iPhone 11 | ![screenshot](documentation/testing/responsiveness-iphone11-home.PNG) | ![screenshot](documentation/testing/responsiveness-iphone11-register.PNG) | ![screenshot](documentation/testing/responsiveness-iphone11-addpost.PNG) | ![screenshot](documentation/testing/responsiveness-iphone11-edit.PNG) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues.

| Page | Mobile | Desktop | Notes |
| --- | --- | --- | --- |
| Home | ![screenshot](documentation/testing/lighthouse-mobile-home.png) | ![screenshot](documentation/testing/lighthouse-desktop-home.png) | Some minor warnings |
| Register | ![screenshot](documentation/testing/lighthouse-mobile-register.png) | ![screenshot](documentation/testing/lighthouse-desktop-register.png) | Some minor warnings |
| Add post | ![screenshot](documentation/testing/lighthouse-mobile-addpost.png) | ![screenshot](documentation/testing/lighthouse-desktop-addpost.png) | Some minor warnings |
| Edit post | ![screenshot](documentation/testing/lighthouse-mobile-edit.png) | ![screenshot](documentation/testing/lighthouse-desktop-edit.png) | Some minor warnings |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Fix | Screenshot |
| --- | --- | --- | --- | --- | --- |
| Home | | | | | |
| | From the home page a user should be able to view the images, but not edit or delete them, unless the user is logged in and the image belongs to them or is a superuser | Tested the feature by remaining logged out and clicking on an image | The feature behaved as expected, and neither the edit or delete options were displayed | Test concluded and passed | ![screenshot](documentation/testing/defprog-edit-edit-not-possible.png) |
| | From the home page a user should not be able to brute-force a URL to navigate to a restricted page | Tested the feature by remaining logged out and typing '/edit/13' at the end of the site url (https://instapilot-e1ebc8c013f4.herokuapp.com/edit/13) | The feature behaved as expected, and access was denied | Test concluded and passed | ![screenshot](documentation/testing/defprog-no-access.png) |
| Register | | | | | |
| | Registration form is expected to require a username be entered | Tested the feature by leaving the field blank | The feature behaved as expected, and requested a username be entered | Test concluded and passed | ![screenshot](documentation/testing/defprog-register-username-missing.png) |
| | Registration form is expected to request a different username if the one entered is already in use | Tested the feature by entering a username already in use | The feature behaved as expected, and requested a different username be entered | Test concluded and passed | ![screenshot](documentation/testing/defprog-register-user-exists.png) |
| Login | | | | | |
| | The login form is expected to only grant access with a correct username and password combination | Tested the feature by entering an incorrect password | The feature behaved as expected, and it did not grant me access | Test concluded and passed | ![screenshot](documentation/testing/defprog-login-incorrect-password.png) |
| Add post | | | | | |
| | Add post form is expected to require a caption | Tested the feature by not entering a caption | The feature behaved as expected, and it requested a caption be entered | Test concluded and passed | ![screenshot](documentation/testing/defprog-addpost-caption-required.png) |
| | Add post form is expected to require a flight number | Tested the feature by not entering a flight number | The feature behaved as expected, and it requested a flight number be entered | Test concluded and passed | ![screenshot](documentation/testing/defprog-addpost-flightnumber-required.png) |
| | Add post form is expected to require a location | Tested the feature by not entering a location | The feature behaved as expected, and it requested a location be entered | Test concluded and passed | ![screenshot](documentation/testing/defprog-addpost-location-required.png) |
| | Add post form is expected to require a location be set on the map | Tested the feature by not entering a location | The feature behaved as expected, and didn't allow the share button be clicked | Test concluded and passed | ![screenshot](documentation/testing/defprog-addpost-map.png) |
| Delete modal | | | | | |
| | Details page is expected to prompt the user to confirm they wish to delete their image before deleting it | Tested the feature by clicking delete on an image | The feature behaved as expected, and a modal appeared requesting the user to confirm they wish to delete the image | Test concluded and passed | ![screenshot](documentation/testing/defprog-delete-modal.png) |


## User Story Testing

| User Story | Screenshot |
| --- | --- |
| As a new site user, I would like to register an account, so that I can post my own images. | ![screenshot](documentation/register-features.png) |
| As a new site user, I would like to post an image, so that I can view my image on the site. | ![screenshot](documentation/homepage-features.png) |
| As a new site user, I would like to add a caption, flight number, airline and location so that I can add information to my post.️ | ![screenshot](documentation/addpost-features.png) |
| As a new site user, I would like to click on an image, so that I can view the full image and information. | ![screenshot](documentation/testing/defprog-edit-edit-not-possible.png) |
| As a returning site user, I would like to login to my account, so that I can view, edit and delete my posts. | ![screenshot](documentation/login-features.png) |
| As a returning site user, I would like to logout of my account, so that I can logout and prevent others editing and deleting my posts. | ![screenshot](documentation/logout-features.png) |
| As a returning site user, I would like to edit my post, so that I can amend my posts as required. | ![screenshot](documentation/edit-post-features.png) |
| As a returning site user, I would like to delete a post, so that I can delete unwanted posts. | ![screenshot](documentation/delete-post-features.png) |
| As a site administrator, I should be able to login to my account, so that I can view, edit and delete posts. | ![screenshot](documentation/admin-features.png) |


## Bugs

- Background image not displaying on deployed site through Heroku

    ![screenshot](documentation/testing/bugs-bg-img-original.png)

    - I originally had my css code as per the screenshot above. To fix this, I contacted tutor support and was advised by a tutor to hard-code the URL. Although this isn't an ideal solution, it got the job done. I intend to revisit this when I have more time to do it properly.

    ![screenshot](documentation/testing/bugs-bg-img-tutor-fix.png)

- Python `E501 line too long`

    ![screenshot](documentation/testing/bugs-python-too-long.png)

    - To fix this, I hit return after the open bracket on lines 19 & 22.

- Background image not extending the full length of the content on smaller screens

    ![screenshot](documentation/testing/bugs-bg-img-not-extending.png)

    - To fix this, I added a media query in style.css with a min-width value of 780px and removed the no-repeat attribute from the background image.

    ![screenshot](documentation/testing/bugs-bg-img-fix.png)


## Unfixed Bugs

There are no remaining bugs that I am aware of.
