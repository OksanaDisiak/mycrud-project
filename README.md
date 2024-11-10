# mycrud-project



#1) Validate authorization for CREATE request with API key

Preconditions:
Endpoint URL for CREATE request is available and functioning:
	POST https://petstore.swagger.io/v2/pet
API key details provided: 
	valid api key - api_key:special-key, 
invalid api key - api_key:invalid-key
Body for CREATE request is prepared with valid data according to the model in swagger.

Scenario 1: CREATE without Authorization
Set up a CREATE request without any authorization headers.
Send the request to the CREATE endpoint with correct data in the body.
Expected Result: The response status code should be 401 Unauthorized or another failure code, the response body should indicate that authorization is required.
Status: Fail - now I can create new pets in the store without auth.

Scenario 2: CREATE with Invalid API Key
Set up a CREATE request with an invalid API key in the authorization header: api_key:invalid-key
Send the request to the CREATE endpoint with correct data in the body.
Expected Result: The response status code should be 401 Unauthorized or 403 Forbidden or another failure code, the response body should indicate that authorization is required.
Status: Fail -  now I can create new pets in the store without invalid api key.

Scenario 3: CREATE with Valid API Key
Set up a CREATE request with a valid API key in the authorization header: api_key:special-key
Send the request to the CREATE endpoint with correct data in the body.
Confirm that entity was created successfully.
Expected Result: The response status code should be 200 OK Created and the response body should match the structure and data sent in the request, including correctly generated IDs.
Status: Pass


#2) Validate authorization for CREATE request with OAuth2: 

Preconditions:
Endpoint URL for CREATE request is available and functioning:
	POST https://petstore.swagger.io/v2/pet
OAuth2 details provided: 
login: xxxxxx, password: xxxxxx
Body for CREATE request is prepared with valid data according to the model in swagger.

Scenario 1: user logged in without read-write permission
Authorize user with no selected permission (read: unchecked, write: unchecked)
Get a token and set it up in the header of CREATE request. 
Send the request to the CREATE endpoint with correct data in the body.
Expected Result: The response status code should be 403 Forbidden or another failure code, the response body should indicate that authorization is required.
Status: Blocked - can not authorize with OAuth2.

Scenario 2: user logged in with read-only permission
Authorize user with read-only selected permission (read: checked, write: unchecked)
Get a token and set it up in the header of CREATE request. 
Send the request to the CREATE endpoint with correct data in the body.
Expected Result: The response status code should be 403 Forbidden or another failure code, the response body should indicate that authorization is required.
Status: Blocked - can not authorize with OAuth2.

Scenario 3: user logged in with write-only permission
Authorize user with read-only selected permission (read: unchecked, write:checked)
Get a token and set it up in the header of CREATE request. 
Send the request to the CREATE endpoint with correct data in the body.
Expected Result: The response status code should be 200 OK Created and the response body should match the structure and data sent in the request, including correctly generated IDs.
Status: Blocked - can not authorize with OAuth2.

Scenario 4: user logged in with read-write permission
Authorize user with read-write selected permission (read: checked, write:checked)
Get a token and set it up in the header of CREATE request. 
Send the request to the CREATE endpoint with correct data in the body.
Expected Result: The response status code should be 200 OK Created and the response body should match the structure and data sent in the request, including correctly generated IDs.
Status: Blocked - can not authorize with OAuth2.
