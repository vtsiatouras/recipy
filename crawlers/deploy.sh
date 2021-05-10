#!/bin/bash

set -m
scrapyd &
scrapyd-deploy
curl http://localhost:6800/schedule.json -d project=recipes -d spider=akispetretzikis
curl http://localhost:6800/schedule.json -d project=recipes -d spider=argirobarbarigou
curl http://localhost:6800/schedule.json -d project=recipes -d spider=skarmoutsos
curl http://localhost:6800/schedule.json -d project=recipes -d spider=suntagesme
fg scrapyd
