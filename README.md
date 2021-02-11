# Facebook Account Handler

This can login to your account, add a friend from your location, Update Account Status and Comment on Friend's latest post.

## Tech Stack

It uses **Selenium** - A Python Library for Web Automation and a little bit of Javascript

## How to Setup?

I have used Virtual Enviornment (venv) to isolate this project from others.
To activate Virtual Env *cd* into ./fb/Scripts Directory and run this command

(Windows)
```bash
activate.bat
``` 

For Linux it is in bin/ directory

(Linux)
```bash
source <venv>/bin/activate
```

After That, 

```bash
python main.python
```
run this command and your program is ready to run.

## Structure

To use perform different tasks you can call respective functions from Facebook Class.

login() - It is the method which logs in your account

*To login account you need to send email and password when you intiate Facebook Class*

findFriends() - It finds friend from your location and sends a friend request

updateStatus() - It updates Status

comment() - It comments on recent post of recent friend

## Misc

It uses Chrome as its browser

Facebook's input field is hard to locate because it does not exist. I have seen that they use div as input field which makes it harder to send_keys to them, So updateStatus() does not work properly.

I didn't find out a way to find current location of profile so it searches India in Search box and sends friend request

If Virtual Env doesn't works then use local system