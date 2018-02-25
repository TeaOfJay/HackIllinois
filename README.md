# TravelMatch: A Travel Buddy Finder
Bringing the world closer one buddy at at a time.

Many millenials wish to travel around the world in their ripe age. Often times, these week or month long trips can be quite lonely when one can't find a partner to go with. We're all trying to meet new people, yet we reject highly artifical and sanctioned venues such as networking events. What TravelMatch solves is this dilemma of finding a buddy who shares the same interest and taste as you.

Using the Amadeus Sandbox API, we are able to query multiple travel destinations based on various criteria of interests, trends, age, and demographic. With our algorithm, we also use this data to process potential matches based on similar travel dates and locations.

You can enter in your destination and who you want to travel with. If you don't choose your destination or your travel buddy they will be randomly assigned to you. We also implemented a feature where you can upload a photo and we will generate an airline ticket to the place where the photo was taken.

## Tests

You can enter in your destination and who you want to travel with. If you don't choose your destination or your travel buddy they will be  assigned to you via the criteria mentioned above.

Please clone the repo and launch a local server on your own machine.
```
cd hacki
python manage.py runserver
```
This should start development server at http://127.0.0.1:8000/.

You can login via Facebook at http://127.0.0.1:8000/travelmatch/login. There you will be requested your like data, which will be processed through our algorithm to find potential matches.

Run ```python manage.py migrate``` to apply migrations if you make any changes to the development environment.

## Infrastructure
This platform is built on a Django in the backend and serving inline Python to dynamically generated html in the frontend. For the purposes of the demo, we used Django's  ```sq.lite3``` database.

We have also built a universally accessible application via Google Cloud detailed below.

## Facebook Integration

For obtaining much of the user data, we decided to opt in with Single Sign On via Facebook to allow users to use their Facebook likes and interest as processing for our application rather than having them manually input data in. This does twofold: it allows ease of login as well as ease of using the application as our service will provide accurate potential matches immediately.



## Google Cloud
Much of the backend is built on the App Engine Standard Environment. Instead of using the  ``` sq.lite3 ``` database, we created a 2nd Generation MySQL database to query all the current users.

Although running and older version than the demo, our live service via Google Cloud can be found here: https://travelmatch-196222.appspot.com/

Please refer here should you be interested in taking the test above to the next level and set up your own Google Cloud server: https://cloud.google.com/python/django/appengine

## Moving Forward
Although this was just a hackathon project, we accomplished a lot in 36 hours. There are, however, many avenues that can be improved upon in future interations of this project. We had planned on implementing a feature where you can upload a photo and we will generate an airline ticket to the place where the photo was taken. This would provide yet another way for users to not only gain inspiration but also find potential travel locations with partners.

Fully deploying this service on Google Cloud would be very agreeable. Allowing this service to be universally accessible would allow anyone ANYWHERE to find potential buddies for their upcoming vacation.

### Dating App Disclaimer
Some may argue that this app reflects a dating app. While that may be an eventuality for partners to eventually find each other likening, we do not endorse relationships. Instead, we emphasize the experience that you and your partner go through in your trip. Our mission is to provide an amazing experience by providing 1.) the most compatible travel buddy and 2.) the most exceptional travel destinations via Amadeus API.

## Acknowledgments

- Built for HackIllinois in February 2018.
- Entering for the Amadeus Flight Challenge
- Entering for Facebook's "bringin the world closer" challenge.
- Entering for best use of Google Cloud challenge.
- Made by Yu-Lin Yang, Payton Garland, Ryan Gontarek,  and Jonathan Ta.

Copyright 2018  TravelMatch

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
