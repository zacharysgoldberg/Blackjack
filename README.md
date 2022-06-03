# Blackjack game

Requires user to register account and login with valid credentials before playing. User account and leaderboard data is stored in a local redis database (Development stage).
JSON objects for data storage (RedisJson).
Typical Blackjack game features including hit, stand, bet, split, and leaderboard scores.

## Future improvements

Forget password.
Will not include cloud based Redis database due to pricing restrictions to include RedisJson module.

## How to play

From terminal, install requirements `pip install -r requirements.txt`, pull docker image for RedisJson `docker pull redislabs/rejson`, then run docker container for redis database `docker run -p 6379:6379 --name redis-db redislabs/rejson:latest`, and run `python blackjack.py` in root dir.
