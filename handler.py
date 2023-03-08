#!/usr/bin/env python3
import jwt
import time
import sys
#run with:  python -c "import pythonLambda0; print (pythonLambda0.lambda_handler('',''))"
# Get PEM file path
pem = 'private-key.pem'

# Get the App ID
app_id = '226725'

def handler(event,context):

    # Open PEM
    with open(pem, 'rb') as pem_file:
        signing_key = jwt.jwk_from_pem(pem_file.read())

    payload = {
        # Issued at time
        'iat': int(time.time()),
        # JWT expiration time (10 minutes maximum)
        'exp': int(time.time()) + 600,
        # GitHub App's identifier
        'iss': app_id
    }

    # Create JWT
    jwt_instance = jwt.JWT()
    encoded_jwt = jwt_instance.encode(payload, signing_key, alg='RS256')

    return encoded_jwt

