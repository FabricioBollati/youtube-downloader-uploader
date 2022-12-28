import requests

client_id = "595235249031-0ronnn9vhnkrnjancuct9dl4v6416kui.apps.googleusercontent.com"
client_secret = "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"

# Replace {AUTHORIZATION_CODE} with the authorization code obtained in the previous step
auth_code = "4/0AWgavdcnW8qnyGf3CLge3EUic1Z4GHIrfrz3XHNX3Kgv8tlRYx2tO1fdli2vO7Egr1yHPw"

# Make a POST request to the token URL to exchange the authorization code for an access token and refresh token
token_response = requests.post(
    "https://oauth2.googleapis.com/token",
    data={
        "client_id": client_id,
        "client_secret": client_secret,
        "code": auth_code,
        "grant_type": "authorization_code",
        "redirect_uri": "http://localhost",
    }
)
print(token_response.text)
# Parse the response
response_data = token_response.json()
print(response_data)
access_token = response_data["access_token"]
refresh_token = response_data["refresh_token"]

print(refresh_token)