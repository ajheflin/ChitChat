# ChitChat

An application made by Miguel Quezada, Daniel Williams, Adam (AJ) Heflin, and Winston Bass.

ChitChat is a Vue.js-based web chat application, founded on the same core beliefs that Facebook Messenger prioritizes. These priorities are accessibility, sleek design, and efficiency. We achieve this through our use of Google's Material Design standards.

## Technologies we use:

1. Django
2. Vue.js
3. TypeScript

## To build and run a local development server:

### Ensure you have Node.js v.14.15.4

1. `cd client`
2. `npm install`
3. `npm run serve`

or with `yarn`

1. `yarn install`
2. `yarn serve`

## To build and run a local development REST Api:

1. `pip install virtualenv` _optional if you already have virutalenv installed_
2. `virtualenv env`
3. `. env/bin/activate` or `source env/bin/activate`
4. `pip install -r requirements.txt`
5. `cd api`
6. `python manage.py runserver`
