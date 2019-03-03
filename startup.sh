#!/bin/sh

echo 'migrate start...'
/code/manage.py migrate
echo 'migrate finish !'

supervisord -n
