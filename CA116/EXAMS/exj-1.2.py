#!/usr/bin/env python

home_goals = int(input()) * 7
home_points = int(input())
away_goals = int(input()) * 7
away_points = int(input())

home_score = home_goals + home_points
away_score = away_goals + home_points

if home_score < away_score:
 print("away win")
elif away_score < home_score:
 print("home win")
else:
 print("draw")