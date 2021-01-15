# login_required
limiting access using login_required decorator

# purpose:
Simple example of controlling urls in Django using it's buit-in decorator (login_required) when we want to give access to only logged in users.

# notice:
1) Logging function (page) must be defined as our first function.
2) It's better to redirect (to homepage) logged in users when they try to access the logging page again.

# requirements:
1) python 3.9
2) Django 3.1.4
