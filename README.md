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
1a | `Click submit to add profile to database`| `Add to database and redirect to Profile page and display profile`| **Pass** 
3b | `Click  to delete profile to database`| `Remove from database and redirect to Profile page`| **Pass** 