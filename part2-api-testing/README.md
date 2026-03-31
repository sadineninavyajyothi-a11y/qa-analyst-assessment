# Part 2: API Testing - JSONPlaceholder API

## Overview
Automated tests for the JSONPlaceholder REST API covering:
1. **GET /users/1** - Fetches a user and validates response structure (200, id/name/email fields)
2. 2. **POST /posts** - Creates a new post and verifies the response matches submitted data (201)
   3. 3. **GET /users/999** - Tests 404 error handling for a non-existent resource
     
      4. ## How to Run
     
      5. ### Install dependencies
      6. ```bash
         cd part2-api-testing
         pip install -r requirements.txt
         ```

         ### Run the tests
         ```bash
         pytest test_jsonplaceholder_api.py -v
         ```

         ## Requirements
         - Python 3.7+
         - - pytest
           - - requests
