# PROJECT 3 : FREE-HANDS 

### Objective :   
MATCHING PORTAL for individual with **FREE HANDS** to find **PART TIME JOBS**
    
#### SCOPE
The website allows individual, companies or corporations to engage staff for short period with worrying:
    
    * Allow User to register for new account and login 
    * CREATE / READ / UPATE / DELETE one or more job listing 
    
Individual can also register to showcase and market their own profile

    * Allow User to register for new account and login 
    * CREATE / READ / UPATE / DELETE their profile 
    
#### Demo
A live demo can be found here. 
_https://p4-freehands.herokuapp.com/_

#### UX
    My Considerations for the website:
    * user can find their desired job or get short term job easily.
    * companies can save on their headcount by engaging from the pool of ready staff for short terms.
    

#### Technologies
    1. HTML
    2. CSS 
    3. Bootstrap 
    4. Jinja
    5. Python
    6. Whitenoise 
    7. PostgreSQL
    8. Django 

#### Features
				
**My Design of the site :**

    -  Easy for companies and individual to create a match
    
    Limitations: 
    - link from index to individual jobs are not set up
    - search bar not ready to be implement
    - Social media links not link not set up
    Future development
    - have messages option for user to have discussions

#### Testing
Manual Testing is done to ensure that the all functions are functional.
Test Results as follows :

#### Testing User Authentication 
*No* | *Steps* | *Expected Results* | *Observations*
--- | --- | --- | ---
1 | `On the Landing Page, click on the "login" (top right)`| `Render login page for user to login and show profile (see testing profile below)`| **Pass** 
2 | `On the Landing Page, click on the "register" (top right)`| `Render register page for user to register and show profile (see testing profile below)`| **Pass** 
3 | `After login, click on the "logout" (top right of navbar)`| `logout and show landing page`| **Pass** 

#### Testing Job Listing Page
*No* | *Steps* | *Expected Results* | *Observations*
--- | --- | --- | ---
1a | `On the Landing Page, click on the "Jobs" in navbar`| `Show the full listing of all available jobs`| **Pass** 
1b | `On the Landing Page, click on the "Helps" in navbar`| `Show the full listing of all available individual`| **Pass** 
2a | `in Profile, click "add job" to add a new job`| `Render a form to enter new job listing`| **Pass** 
2b | `Click submit to add job to database`| `Add to database and redirect to Profile page`| **Pass** 
3a | `in Profile, click "edit job" to add a new job`| `Render a form to edit selected job listing`| **Pass** 
3b | `Click submit to edit job to database`| `Make changes to database and redirect to Profile page`| **Pass** 
4a | `in Profile, click "delete job" to add a new job`| `Check with user to confirm job listing`| **Pass** 
4b | `Click submit to delete job to database`| `Remove from database and redirect to Profile page`| **Pass** 

#### Testing Individual Profile
*No* | *Steps* | *Expected Results* | *Observations*
--- | --- | --- | ---
1 | `in Landing page, click "Profile" to view profile`| `Display profile details if data exist else will render form for user to enter a new profile`| **Pass** 
2 | `Click submit to add profile to database`| `Add to database and redirect to Profile page and display profile`| **Pass** 
3 | `Click  to delete profile to database`| `Remove from database and redirect to Profile page`| **Pass** 

#### Testing Payment Link
*No* | *Steps* | *Expected Results* | *Observations*
--- | --- | --- | ---
1 | In "Help List" click on the 'Book me now!' of the selected profile to make a booking for the staff`| `Go to payment page for user to give a deposit to engage the staff `| **Pass** 


#### Deployment
This site is hosted using Heroku App Link : 
_https://p4-freehands.herokuapp.com/_

    Codes are regularly commited to GitHub and links are made to Heroku by installing in bash terminal in projects.
    Regular commits are push to the Github subsequently push to heroku to deploy.
    .gitignore file is added to remove files that are not required or files that we do not wish to be uploaded to Github

_Deploy Heroku:_

    i) Install Heroku using bash
    ii) Login to Heroku
    iii) Install gunicorn
    iv) Create Procfile and requirements.txt
    V) Commit and push to Heroku 
    vi) Set up the Environment Vasriables
    vii) Update Dependencies


#### Credits
    Uses W3School for many reference (https://www.w3schools.com/)
    Uses fontawesome for the social media icons (https://fontawesome.com/)
    Uses Bootstrap for templates (https://getbootstrap.com/)
