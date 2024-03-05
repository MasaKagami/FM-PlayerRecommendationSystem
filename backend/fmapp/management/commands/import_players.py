# from django.core.management.base import BaseCommand, CommandError
# from fmapp.models import Player
import csv

csv_file_path = '/Users/masa/Desktop/FM23DB/FM2023.csv'
with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    first_row = next(reader)
    print(first_row.keys())


# class Command(BaseCommand):
#     help = 'Imports players from a CSV file'

#     def add_arguments(self, parser):
#         parser.add_argument('csv_file_path', type=str, help='/Users/masa/Desktop/FM23DB/FM2023.csv')

#     def handle(self, *args, **options):
#         csv_file_path = options['csv_file_path']
#         with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
#             reader = csv.DictReader(csvfile)
#             for row in reader:
#                 Player.objects.create(
#                     name=row["Name"],
#                     age=int(row['Age']),
#                     nationality=row['Nationality'],
#                     club=row['Club'],

#                     Left_Foot=int(row['Left Foot']),
#                     Right_Foot=int(row['Right Foot']),
#                     Height=int(row['Height']),
#                     Weight=int(row['Weight']),
#                     national_team_appearances=int(row['Number of national team appearances']),
#                     national_team_goals=int(row['Goals scored for the national team']),
#                     ca=int(row['ca']),
#                     pa=int(row['pa']),
#                     Values=int(row['Values']),
#                     Salary=int(row['Salary']),
#                     UID=int(row['UID']),

#                     GK=int(row['GK']),
#                     DL=int(row['DL']),
#                     DC=int(row['DC']),
#                     DR=int(row['DR']),
#                     WBL=int(row['WBL']),
#                     WBR=int(row['WBR']),
#                     DM=int(row['DM']),
#                     ML=int(row['ML']),
#                     MC=int(row['MC']),
#                     MR=int(row['MR']),
#                     AML=int(row['AML']),
#                     AMC=int(row['AMC']),
#                     AMR=int(row['AMR']),
#                     ST=int(row['ST']),

#                     Corners=int(row['Corners']),
#                     Crossing=int(row['Crossing']),
#                     Dribbling=int(row['Dribbling']),
#                     Finishing=int(row['Finishing']),
#                     First_Touch=int(row['First Touch']),
#                     Free_Kick_Taking=int(row['Free Kick Taking']),
#                     Heading=int(row['Heading']),
#                     Long_Shots=int(row['Long Shots']),
#                     Long_Throws=int(row['Long Throws']),
#                     Marking=int(row['Marking']),
#                     Passing=int(row['Passing']),
#                     Penalty_Taking=int(row['Penalty Taking']),
#                     Tackling=int(row['Tackling']),
#                     Technique=int(row['Technique']),

#                     Aggressiion=int(row['Aggressiion']),
#                     Anticipation=int(row['Anticipation']),
#                     Bravery=int(row['Bravery']),
#                     Composure=int(row['Composure']),
#                     Concentration=int(row['Concentration']),
#                     Vision=int(row['Vision']),
#                     Decision=int(row['Decision']),
#                     Determination=int(row['Determination']),
#                     Flair=int(row['Flair']),
#                     Leadership=int(row['Leadership']),
#                     Off_The_Ball=int(row['Off The Ball']),
#                     Position=int(row['Position']),
#                     Teamwork=int(row['Teamwork']),
#                     Work_Rate=int(row['Work Rate']),

#                     Acceleration=int(row['Acceleration']),
#                     Agility=int(row['Agility']),
#                     Balance=int(row['Balance']),
#                     Jumping_Reach=int(row['Jumping Reach']),
#                     Natural_Fitness=int(row['Natural Fitness']),
#                     Pace=int(row['Pace']),
#                     Stamina=int(row['Stamina']),
#                     Strength=int(row['Strength']),
#                 )
#         self.stdout.write(self.style.SUCCESS('Successfully imported player data'))
