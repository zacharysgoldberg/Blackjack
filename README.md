# Blackjack game

Requires user to register an account and login before playing. User account and leaderboard data is stored in a local redis database (Development stage).
JSON objects for data storage (RedisJson).
Typical Blackjack game features including hit, stand, bet, split, and leaderboard scores.

## How to play

From root directory, install dependencies: `pip install -r requirements.txt`, build docker image for RedisJson: `docker-compose up -d`, and run `python blackjack.py`.
