# Watcher of Friends Online

Stalk for your friends from command line!
Just enter you login and password and script will show you your friends who is online right now.

# How to use
Command line:
`python vk_friends_online.py [-h] [-s] login [password]`.
 -	`login` - Your vk login
 -	`password` - Your vk password *(if you want to show it in command line)*
 -	`-h (--help)` -  Show this help message and exit
 -	`-s (--sort)` -  Sort your mates by name, not by vk hints

If `password` not entered via args, script will ask you for it later.

Profit of it is that you dont want to show it in command line. Therefore script will ask it in **secret-mode**.

# Example of script execution
```
vk_friends_online> python vk_friends_online.py login@vk.com -s
Password: 
Friend 1 [m]
Friend 2
Friend 3 [m]
Friend 4
--
Total friends online: 4 
```

# Preparations
But before launch you need to install external module. Just print this:
`pip install -r requirements.txt`.

# Just something you need to know
This script uses `vk 2.0.2` module from official python repo.
All we do with your `login` and `pass` - *just passing them to that module*.
