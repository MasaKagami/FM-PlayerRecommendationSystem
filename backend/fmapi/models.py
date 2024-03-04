from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    club = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    
    Left_Foot= models.PositiveIntegerField()
    Right_Foot= models.PositiveIntegerField()
    Height = models.PositiveIntegerField()
    Weight = models.PositiveIntegerField()
    national_team_appearances = models.PositiveIntegerField()
    national_team_goals = models.PositiveIntegerField()
    ca = models.PositiveIntegerField()
    pa = models.PositiveIntegerField()
    Values = models.PositiveIntegerField()
    Salary = models.PositiveIntegerField()
    UID = models.PositiveIntegerField()

    GK = models.PositiveIntegerField()
    DL = models.PositiveIntegerField()
    DC = models.PositiveIntegerField()
    DR = models.PositiveIntegerField()
    WBL = models.PositiveIntegerField()
    WBR = models.PositiveIntegerField()
    DM = models.PositiveIntegerField()
    ML = models.PositiveIntegerField()
    MC = models.PositiveIntegerField()
    MR = models.PositiveIntegerField()
    AML = models.PositiveIntegerField()
    AMC = models.PositiveIntegerField()
    AMR = models.PositiveIntegerField()
    ST = models.PositiveIntegerField()

    Corners = models.PositiveIntegerField()
    Crossing = models.PositiveIntegerField()
    Dribbling = models.PositiveIntegerField()
    Finishing = models.PositiveIntegerField()
    First_Touch = models.PositiveIntegerField()
    Free_Kick_Taking = models.PositiveIntegerField()
    Heading = models.PositiveIntegerField()
    Long_Shots = models.PositiveIntegerField()
    Long_Throws = models.PositiveIntegerField()
    Marking = models.PositiveIntegerField()
    Passing = models.PositiveIntegerField()
    Penalty_Taking = models.PositiveIntegerField()
    Tackling = models.PositiveIntegerField()
    Technique = models.PositiveIntegerField()

    Aggressiion = models.PositiveIntegerField()
    Anticipation = models.PositiveIntegerField()
    Bravery = models.PositiveIntegerField()
    Composure = models.PositiveIntegerField()
    Concentration = models.PositiveIntegerField()
    Vision = models.PositiveIntegerField()
    Decision = models.PositiveIntegerField()
    Determination = models.PositiveIntegerField()
    Flair = models.PositiveIntegerField()
    Leadership = models.PositiveIntegerField()
    Off_The_Ball = models.PositiveIntegerField()
    Position = models.PositiveIntegerField()
    Teamwork = models.PositiveIntegerField()
    Work_Rate = models.PositiveIntegerField()

    Acceleration = models.PositiveIntegerField()
    Agility = models.PositiveIntegerField()
    Balance = models.PositiveIntegerField()
    Jumping_Reach = models.PositiveIntegerField()
    Natural_Fitness = models.PositiveIntegerField()
    Pace = models.PositiveIntegerField()
    Stamina = models.PositiveIntegerField()
    Strength = models.PositiveIntegerField()

