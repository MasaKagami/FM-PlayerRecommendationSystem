from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=30)
    age = models.PositiveIntegerField()
    ca = models.PositiveIntegerField()
    pa = models.PositiveIntegerField()
    nationality = models.CharField(max_length=50)
    club = models.CharField(max_length=100)

ca
pa
Nationality
Club
Corners
Crossing
Dribbling
Finishing
First Touch
Free Kick Taking
Heading
Long Shots
Long Throws
Marking
Passing
Penalty Taking
Tackling
Technique
Aggressiion
Anticipation
Bravery
Composure
Concentration
Vision
Decision
Determination
Flair
Leadership
Off The Ball
Position
Teamwork
Work Rate
Acceleration
Agility
Balance
Jumping Reach
Natural Fitness
Pace
Stamina
Strength
Stability
Foul
Contest performance
Injury
diversity
Aerial Reach
Command Of Area
Communication
Eccentricity
Handling
Kicking
One On Ones
Reflexes
Rushing Out
Punching
Throwing
Adaptation
Ambition
Argue
Loyal
Resistant to stress
Professional
Sportsmanship
Emotional control
GK
DL
DC
DR
WBL
WBR
DM
ML
MC
MR
AML
AMC
AMR
ST
Height
Weight
Left Foot
Right Foot
Values
Current reputation
Domestic reputation
World reputation
Race
RCA
Colour of skin
Date of birth
Number of national team appearances
Goals scored for the national team
Salary
Rental club
UID