## devstoday local branch

- Clone this branch to play with API localy, using Docker.
- Clone [HEROKU branch](https://github.com/vladhutsal/devstoday/tree/heroku) to play with Heroku deployed API.
- **Postman collection:** https://www.getpostman.com/collections/4746ac593e6ada9a0905
- **Heroku URL to fetch posts:** https://devstoday.herokuapp.com/api/posts/

### Start localy:
Works well on Ubuntu 20.10
1. ``` git clone git@github.com:vladhutsal/devstoday.git ```
2. Change dir to the `devstoday` and run `docker-compose up`.

### Check Heroku:
1. Import Postman "Poster_commenter_API" collection to your workspace - LINK TO COLLECTION
2. Choose HEROKU environment - this will change ```baseUrl``` default variable to Heroku app URL.

