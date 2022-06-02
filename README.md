# Blackjack game

Requires user to register account and login with valid credentials before playing. User account and leaderboard data is stored in a local redis database (Development stage).
JSON objects for data storage (RedisJson), typical Blackjack game features including hit, stand, bet, split, and leaderboard scores.

## Future improvements

Forget password

## How to run/test

From terminal, install requirements `pip install -r requirements.txt`, run docker container for redis `docker run -p 6379:6379 --name redis-redisjson redislabs/rejson:latest`, and run `python blackjack.py` in root dir.
