#!/usr/bin/env bash

echo "Updating GitHub Repository"
git add .
git commit -m 'Automatic Update'
git push
clear
echo "GitHub Updated Succesfully!"

echo "Updating Website!"
aws s3 sync . s3://grocery-smart.com
aws s3 sync . s3://www.grocery-smart.com 

clear
echo "Website Updated Succesfully!"