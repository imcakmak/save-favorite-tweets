# save-favorite-tweets
This script lets you save the entire favorite tweet collection (texts & links) of any user you want into a .txt file called "output.txt".

It is the easiest way I could find to save favorite tweets using Twitter API.

It's coded in python version 3.x.

## Requirements
It requires `oauth2`, you can install it via the PIP package.
`$ pip install oauth2`

You need to create an application on https://apps.twitter.com, this will give you the `Consumer Token`, and the `Consumer Secret`. After that you need to create an access token for that application on the same website, which will give you the `Access Token` and the `Access Secret`. Then you have to manually type these values into indicated places of the .py file along with the Twitter handle you want to target.

That's all.
