## devstoday HEROKU branch

This branch is being deployed using Heroku.
There are two containers (Django and Celery) and two addons (cloudamqp as message broker, postgres as DB).

### Test API:
1. Import Postman "Poster_commenter_API" collection to your workspace - [LINK TO COLLECTION](https://www.getpostman.com/collections/4746ac593e6ada9a0905)
2. Choose HEROKU environment - this will change ```baseUrl``` default variable to Heroku app URL.
