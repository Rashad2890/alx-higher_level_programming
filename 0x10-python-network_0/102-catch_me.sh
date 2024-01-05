#!/bin/bash
# catch me that causes the server response
curl -s -L -H "You got me!" -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me
