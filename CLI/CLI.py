import psycopg2

import datetime

import sys

print("Python Version:", sys.version)

def main():
    # Create an ArgumentParser object
    def intro():
        print(f"\nWelcome to the Database CLI Interface!\n")
        print(f"Please select an option: \n1. Insert Data \n2. Delete Data \n3. Update Data \n4. Search Data")
        print(f"5. Aggregrate Functions \n6. Sorting \n7. Joins \n8. Grouping \n9. Subqueries \n10. Transactions \n11. Error Handling \n12. Exit\n")
        user_input = int(input("Enter your choice (1-12): "))
        if user_input == 1:
            insert_data()
        elif user_input == 2:
            delete_data()
        elif user_input == 3:
            update_data()
        elif user_input == 4:
            search_data()
        elif user_input == 5:
            aggregrate_functions()
        elif user_input == 6:
            sorting()
        elif user_input == 7:
            joins()
        elif user_input == 8:
            grouping()
        elif user_input == 9:
            subqueries()
        elif user_input == 10:
            transactions()
        elif user_input == 11:
            error_handling()
        elif user_input == 12:
            print("Exiting CLI...")
            return
        else:
            print("Invalid input. Please try again.")
            intro()

    def insert_data():
        print(f"\nInsert Data\n")
        print(f"Please select an option: \n1. Insert into Player_Info \n2. Insert into Player_Skills \n3. Insert into Team")
        print(f"4. Insert into Match \n5. Insert into Delivery \n6. Back")
        user_input = int(input("Enter your choice (1-6): "))
        if user_input == 1:
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()

            # Prompt the user for the required attributes and validate them
            while True:
                try:
                    player_id = int(input("Enter player id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.") 

            while True:
                date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                try:
                    datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
                    break
                except ValueError:
                    print("This is not a valid date. Please enter a valid date in the format YYYY-MM-DD.")

            while True:
                name = input("Enter name: ")
                if len(name) <= 100:
                    break
                else:
                    print("Name is too long. It should be up to 100 characters.")

            while True:
                country = input("Enter country: ")
                if len(country) <= 50:
                    break
                else:
                    print("Country name is too long. It should be up to 50 characters.")

            # Execute the SQL INSERT statement
            c.execute(f"INSERT INTO Player_Info (player_id, date_of_birth, name, country) VALUES (%s, %s, %s, %s)", (player_id, date_of_birth, name, country))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        elif user_input == 2:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()

            # Prompt the user for the required attributes and validate them
            while True:
                try:
                    player_id = int(input("Enter player id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                name = input("Enter name: ")
                if len(name) <= 100:
                    break
                else:
                    print("Name is too long. It should be up to 100 characters.")

            while True:
                batting_hand = input("Enter batting hand: ")
                if len(batting_hand) <= 20:
                    break
                else:
                    print("Batting hand is too long. It should be up to 20 characters.")

            while True:
                bowling_skill = input("Enter bowling skill: ")
                if len(bowling_skill) <= 20:
                    break
                else:
                    print("Bowling skill is too long. It should be up to 20 characters.")

            # Execute the SQL INSERT statement
            c.execute(f"INSERT INTO Player_Skills (player_id, name, batting_hand, bowling_skill) VALUES (%s, %s, %s, %s)", (player_id, name, batting_hand, bowling_skill))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        elif user_input == 3:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()

            # Prompt the user for the required attributes and validate them
            while True:
                name = input("Enter team name: ")
                if len(name) <= 100:
                    break
                else:
                    print("Team name is too long. It should be up to 100 characters.")

            while True:
                try:
                    home_wins = int(input("Enter number of home wins: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                try:
                    away_wins = int(input("Enter number of away wins: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                try:
                    home_matches = int(input("Enter number of home matches: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                try:
                    away_matches = int(input("Enter number of away matches: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            # Execute the SQL INSERT statement
            c.execute(f"INSERT INTO Team (name, home_wins, away_wins, home_matches, away_matches) VALUES (%s, %s, %s, %s, %s)", (name, home_wins, away_wins, home_matches, away_matches))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        elif user_input == 4:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()

            # Prompt the user for the required attributes and validate them
            while True:
                try:
                    id = int(input("Enter match id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                try:
                    season = int(input("Enter season: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                toss_winner = input("Enter toss winner: ")
                if len(toss_winner) <= 100:
                    break
                else:
                    print("Toss winner is too long. It should be up to 100 characters.")

            while True:
                toss_decision = input("Enter toss decision: ")
                if len(toss_decision) <= 20:
                    break
                else:
                    print("Toss decision is too long. It should be up to 20 characters.")

            while True:
                city = input("Enter city: ")
                if len(city) <= 100:
                    break
                else:
                    print("City name is too long. It should be up to 100 characters.")

            while True:
                team1 = input("Enter team1: ")
                if len(team1) <= 100:
                    break
                else:
                    print("Team1 name is too long. It should be up to 100 characters.")

            while True:
                team2 = input("Enter team2: ")
                if len(team2) <= 100:
                    break
                else:
                    print("Team2 name is too long. It should be up to 100 characters.")

            while True:
                result = input("Enter result: ")
                if len(result) <= 20:
                    break
                else:
                    print("Result is too long. It should be up to 20 characters.")

            while True:
                match_date = input("Enter match date (YYYY-MM-DD): ")
                try:
                    datetime.datetime.strptime(match_date, '%Y-%m-%d')
                    break
                except ValueError:
                    print("This is not a valid date. Please enter a valid date in the format YYYY-MM-DD.")

            # Execute the SQL INSERT statement
            c.execute(f"INSERT INTO Match (id, season, toss_winner, toss_decision, city, team1, team2, result, match_date) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)", (id, season, toss_winner, toss_decision, city, team1, team2, result, match_date))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        elif user_input == 5:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()

            # Prompt the user for the required attributes and validate them
            while True:
                batting_team = input("Enter batting team: ")
                if len(batting_team) <= 100:
                    break
                else:
                    print("Batting team name is too long. It should be up to 100 characters.")

            while True:
                try:
                    match_id = int(input("Enter match id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                try:
                    inning_num = int(input("Enter inning number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                non_striker = input("Enter non striker: ")
                if len(non_striker) <= 100:
                    break
                else:
                    print("Non striker name is too long. It should be up to 100 characters.")

            while True:
                batsman = input("Enter batsman: ")
                if len(batsman) <= 100:
                    break
                else:
                    print("Batsman name is too long. It should be up to 100 characters.")

            while True:
                try:
                    ball_num = int(input("Enter ball number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                try:
                    over_num = int(input("Enter over number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            # Execute the SQL INSERT statement
            c.execute(f"INSERT INTO Delivery (batting_team, match_id, inning_num, non_striker, batsman, ball_num, over_num) VALUES (%s, %s, %s, %s, %s, %s, %s)", (batting_team, match_id, inning_num, non_striker, batsman, ball_num, over_num))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        elif user_input == 6:
            intro()
        else:
            print("Invalid input. Please try again.")
            insert_data()
        intro()
    
    def delete_data():
        print(f"\nDelete Data\n")
        print(f"Please select an option: \n1. Delete from Player_Info \n2. Delete from Player_Skills \n3. Delete from Team")
        print(f"4. Delete from Match \n5. Delete from Delivery \n6. Back")
        user_input = int(input("Enter your choice (1-6): "))

        if user_input == 1:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()

            # Prompt the user for the required attributes and validate them
            while True:
                try:
                    player_id = int(input("Enter player id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            # Execute the SQL DELETE statement
            c.execute(f"DELETE FROM Player_Info WHERE player_id = %s", (player_id,))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        elif user_input == 2:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()

            # Prompt the user for the required attributes and validate them
            while True:
                try:
                    player_id = int(input("Enter player id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            # Execute the SQL DELETE statement
            c.execute(f"DELETE FROM Player_Skills WHERE player_id = %s", (player_id,))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        elif user_input == 3:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()

            # Prompt the user for the required attributes and validate them
            while True:
                name = input("Enter team name: ")
                if len(name) <= 100:
                    break
                else:
                    print("Team name is too long. It should be up to 100 characters.")

            # Execute the SQL DELETE statement
            c.execute(f"DELETE FROM Team WHERE name = %s", (name,))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        elif user_input == 4:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()

            # Prompt the user for the required attributes and validate them
            while True:
                try:
                    id = int(input("Enter match id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            # Execute the SQL DELETE statement
            c.execute(f"DELETE FROM Match WHERE id = %s", (id,))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        elif user_input == 5:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()

            # Prompt the user for the required attributes and validate them
            while True:
                try:
                    match_id = int(input("Enter match id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            while True:
                name = input("Enter team name: ")
                if len(name) <= 100:
                    break
                else:
                    print("Team name is too long. It should be up to 100 characters.")
            
            while True:
                try:
                    inning_num = int(input("Enter inning num: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            # Execute the SQL DELETE statement
            c.execute(f"DELETE FROM Delivery WHERE match_id = %s AND batting_team = %s AND inning_num = %s", (match_id,name,inning_num))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        elif user_input == 6:
            intro()
        else:
            print("Invalid input. Please try again.")
            insert_data()
        intro()
    
    def update_data():
        print(f"\nUpdate Data\n")
        print(f"Please select an option: \n1. Update Player_Info \n2. Update Player_Skills \n3. Update Team")
        print(f"4. Update Match \n5. Update Delivery \n6. Back")
        user_input = int(input("Enter your choice (1-6): "))

        if user_input == 1:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()

            # Prompt the user for the required attributes and validate them
            while True:
                try:
                    old_player_id = int(input("Enter player id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            while True:
                try:
                    player_id = int(input("Enter new player id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                date_of_birth = input("Enter date of birth (YYYY-MM-DD): ")
                try:
                    datetime.datetime.strptime(date_of_birth, '%Y-%m-%d')
                    break
                except ValueError:
                    print("This is not a valid date. Please enter a valid date in the format YYYY-MM-DD.")

            while True:
                name = input("Enter name: ")
                if len(name) <= 100:
                    break
                else:
                    print("Name is too long. It should be up to 100 characters.")

            while True:
                country = input("Enter country: ")
                if len(country) <= 50:
                    break
                else:
                    print("Country name is too long. It should be up to 50 characters.")

            # Execute the SQL UPDATE statement
            c.execute(f"UPDATE Player_Info SET player_id = %s, date_of_birth = %s, name = %s, country = %s WHERE player_id = %s", (player_id, date_of_birth, name, country, old_player_id))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        elif user_input == 2:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()

            # Prompt the user for the required attributes and validate them
            while True:
                try:
                    old_player_id = int(input("Enter player id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            while True:
                try:
                    player_id = int(input("Enter new player id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                name = input("Enter name: ")
                if len(name) <= 100:
                    break
                else:
                    print("Name is too long. It should be up to 100 characters.")

            while True:
                batting_hand = input("Enter batting hand: ")
                if len(batting_hand) <= 20:
                    break
                else:
                    print("Batting hand is too long. It should be up to 20 characters.")

            while True:
                bowling_skill = input("Enter bowling skill: ")
                if len(bowling_skill) <= 20:
                    break
                else:
                    print("Bowling skill is too long. It should be up to 20 characters.")

            # Execute the SQL UPDATE statement
            c.execute(f"UPDATE Player_Skills SET player_id = %s, name = %s, batting_hand = %s, bowling_skill = %s WHERE player_id = %s", (player_id, name, batting_hand, bowling_skill, old_player_id))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        elif user_input == 3:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()

            # Prompt the user for the required attributes and validate them
            while True:
                old_name = input("Enter team name: ")
                if len(old_name) <= 100:
                    break
                else:
                    print("Team name is too long. It should be up to 100 characters.")
            while True:
                name = input("Enter new team name: ")
                if len(name) <= 100:
                    break
                else:
                    print("Team name is too long. It should be up to 100 characters.")

            while True:
                try:
                    home_wins = int(input("Enter number of home wins: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                try:
                    away_wins = int(input("Enter number of away wins: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                try:
                    home_matches = int(input("Enter number of home matches: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                try:
                    away_matches = int(input("Enter number of away matches: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            # Execute the SQL UPDATE statement
            c.execute(f"UPDATE Team SET name = %s, home_wins = %s, away_wins = %s, home_matches = %s, away_matches = %s WHERE name = %s", (name, home_wins, away_wins, home_matches, away_matches, old_name))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        elif user_input == 4:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()

            # Prompt the user for the required attributes and validate them
            while True:
                try:
                    old_id = int(input("Enter match id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            while True:
                try:
                    id = int(input("Enter new match id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                try:
                    season = int(input("Enter season: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                toss_winner = input("Enter toss winner: ")
                if len(toss_winner) <= 100:
                    break
                else:
                    print("Toss winner is too long. It should be up to 100 characters.")

            while True:
                toss_decision = input("Enter toss decision: ")
                if len(toss_decision) <= 20:
                    break
                else:
                    print("Toss decision is too long. It should be up to 20 characters.")

            while True:
                city = input("Enter city: ")
                if len(city) <= 100:
                    break
                else:
                    print("City name is too long. It should be up to 100 characters.")

            while True:
                team1 = input("Enter team1: ")
                if len(team1) <= 100:
                    break
                else:
                    print("Team1 name is too long. It should be up to 100 characters.")

            while True:
                team2 = input("Enter team2: ")
                if len(team2) <= 100:
                    break
                else:
                    print("Team2 name is too long. It should be up to 100 characters.")

            while True:
                result = input("Enter result: ")
                if len(result) <= 20:
                    break
                else:
                    print("Result is too long. It should be up to 20 characters.")

            while True:
                match_date = input("Enter match date (YYYY-MM-DD): ")
                try:
                    datetime.datetime.strptime(match_date, '%Y-%m-%d')
                    break
                except ValueError:
                    print("This is not a valid date. Please enter a valid date in the format YYYY-MM-DD.")
            
            c.execute(f"UPDATE Match SET id = %s, season = %s, toss_winner = %s, toss_decision = %s, city = %s, team1 = %s, team2 = %s, result = %s, match_date = %s WHERE id = %s", (id, season, toss_winner, toss_decision, city, team1, team2, result, match_date, old_id))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        elif user_input == 5:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()

            # Prompt the user for the required attributes and validate them
            while True:
                try:
                    old_match_id = int(input("Enter match id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                old_batting_team = input("Enter batting team: ")
                if len(batting_team) <= 100:
                    break
                else:
                    print("Batting team name is too long. It should be up to 100 characters.")
            
            while True:
                try:
                    inning_num = int(input("Enter inning number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")
            
            while True:
                batting_team = input("Enter new batting team: ")
                if len(batting_team) <= 100:
                    break
                else:
                    print("Batting team name is too long. It should be up to 100 characters.")

            while True:
                try:
                    match_id = int(input("Enter new match id: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                try:
                    inning_num = int(input("Enter new inning number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                non_striker = input("Enter non striker: ")
                if len(non_striker) <= 100:
                    break
                else:
                    print("Non striker name is too long. It should be up to 100 characters.")

            while True:
                batsman = input("Enter batsman: ")
                if len(batsman) <= 100:
                    break
                else:
                    print("Batsman name is too long. It should be up to 100 characters.")

            while True:
                try:
                    ball_num = int(input("Enter ball number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            while True:
                try:
                    over_num = int(input("Enter over number: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            c.execute(f"UPDATE Delivery SET batting_team = %s, match_id = %s, inning_num = %s, non_striker = %s, batsman = %s, ball_num = %s, over_num = %s WHERE match_id = %s", (batting_team, match_id, inning_num, non_striker, batsman, ball_num, over_num, old_match_id, old_batting_team, old_inning_num))

            # Commit the changes and close the connection
            conn.commit()
            conn.close()
        elif user_input == 6:
            intro()
        else:
            print("Invalid input. Please try again.")
            insert_data()
        intro()
    
    def search_data():
        print(f"\nSearch Data\n")
        print(f"Please select an option: \n1. Search from Player_Info \n2. Search from Player_Skills \n3. Search from Team")
        print(f"4. Search from Match \n5. Search from Delivery \n6. Back")
        user_input = int(input("Enter your choice (1-6): "))
        table = ""
        if user_input == 1:
            table = "Player_Info"
        elif user_input == 2:
            table = "Player_Skills"
        elif user_input == 3:
            table = "Team"
        elif user_input == 4:
            table = "Match"
        elif user_input == 5:
            table = "Delivery"
        elif user_input == 6:
            intro()
        else:
            print("Invalid input. Please try again.")
            search_data()
        # Connect to the database
        conn = psycopg2.connect(
            dbname="431W",
            user="postgres",  # Default username
            password="Manban12!",
            host="localhost",
            port="5432"
        )
        c = conn.cursor()
        query = input("Enter the query for WHERE: ")
        c.execute(f"SELECT * FROM {table} WHERE {query}")
        rows = c.fetchall()
        for row in rows:
            print(row)
        conn.close()
        intro()

    def aggregrate_functions():
        print(f"\nAggregrate Functions\n")
        print(f"Please select an function: \n1. Count \n2. Sum \n3. Average")
        print(f"4. Min \n5. Max \n6. Back")
        user_input = int(input("Enter your choice (1-6): "))
        table = ""
        function = ""
        if user_input == 1:
            function = "COUNT"
        elif user_input == 2:
            function = "SUM"
        elif user_input == 3:
            function = "AVG"
        elif user_input == 4:
            function = "MIN"
        elif user_input == 5:
            function = "MAX"
        elif user_input == 6:
            intro()
        else:
            print("Invalid input. Please try again.")
            aggregrate_functions()

        use = input(f"What will you use this function on: ")

        print(f"Please select a table: \n1. Player_Info \n2. Player_Skills \n3. Team \n4. Match \n5. Delivery")
        user_input = int(input("Enter your choice (1-5): "))
        if user_input == 1:
            table = "Player_Info"
        elif user_input == 2:
            table = "Player_Skills"
        elif user_input == 3:
            table = "Team"
        elif user_input == 4:
            table = "Match"
        elif user_input == 5:
            table = "Delivery"
        else:
            print("Invalid input. Please try again.")
            aggregrate_functions()
        
        # Connect to the database
        conn = psycopg2.connect(
            dbname="431W",
            user="postgres",  # Default username
            password="Manban12!",
            host="localhost",
            port="5432"
        )
        c = conn.cursor()
        query = input("Enter the query for WHERE: ")
        c.execute(f"SELECT {function}({use}) FROM {table} WHERE {query}")
        rows = c.fetchall()
        for row in rows:
            print(row)
        conn.close()
        intro()

    def sorting():
        print(f"\nSorting\n")
        print(f"Please select an option: \n1. Ascending \n2. Descending \n3. Back")
        user_input = int(input("Enter your choice (1-3): "))
        table = ""
        order = ""
        if user_input == 1:
            order = "ASC"
        elif user_input == 2:
            order = "DESC"
        elif user_input == 3:
            intro()
        else:
            print("Invalid input. Please try again.")
            sorting()

        print(f"Please select a table: \n1. Player_Info \n2. Player_Skills \n3. Team \n4. Match \n5. Delivery")
        user_input = int(input("Enter your choice (1-5): "))
        col = ""
        if user_input == 1:
            table = "Player_Info"
            cols = ["player_id", "date_of_birth", "name", "country"]
            print(cols)
            while True:
                col = input(f"What column would you like to sort by : ")
                if col in cols:
                    break
                else:
                    print("Invalid column. Please try again.")
        elif user_input == 2:
            table = "Player_Skills"
            cols = ["player_id", "name", "batting_hand", "bowling_skill"]
            print(cols)
            while True:
                col = input(f"What column would you like to sort by : ")
                if col in cols:
                    break
                else:
                    print("Invalid column. Please try again.")
        elif user_input == 3:
            table = "Team"
            cols = ["name", "home_wins", "away_wins", "home_matches", "away_matches"]
            print(cols)
            while True:
                col = input(f"What column would you like to sort by : ")
                if col in cols:
                    break
                else:
                    print("Invalid column. Please try again.")
        elif user_input == 4:
            table = "Match"
            cols = ["id", "season", "toss_winner", "toss_decision", "city", "team1", "team2", "result", "match_date"]
            print(cols)
            while True:
                col = input(f"What column would you like to sort by : ")
                if col in cols:
                    break
                else:
                    print("Invalid column. Please try again.")
        elif user_input == 5:
            table = "Delivery"
            cols = ["batting_team", "match_id", "inning_num", "non_striker", "batsman", "ball_num", "over_num"]
            print(cols)
            while True:
                col = input(f"What column would you like to sort by : ")
                if col in cols:
                    break
                else:
                    print("Invalid column. Please try again.")                   
        else:
            print("Invalid input. Please try again.")
            sorting()
        
        # Connect to the database
        conn = psycopg2.connect(
            dbname="431W",
            user="postgres",  # Default username
            password="Manban12!",
            host="localhost",
            port="5432"
        )
        c = conn.cursor()
        use = input(f"What will you use this function on: ")
        
        c.execute(f"SELECT {use} FROM {table} ORDER BY {col} {order}")
        rows = c.fetchall()
        for row in rows:
            print(row)
        conn.close()
        intro()
    
    def joins():
        print(f"\nJoins\n")
        print(f"Please select an option: \n1. Inner Join \n2. Left Join \n3. Right Join")
        print(f"4. Full Join \n5. Back")
        user_input = int(input("Enter your choice (1-5): "))
        table1 = ""
        table2 = ""
        if user_input == 1:
            join = "INNER JOIN"
        elif user_input == 2:
            join = "LEFT JOIN"
        elif user_input == 3:
            join = "RIGHT JOIN"
        elif user_input == 4:
            join = "FULL JOIN"
        elif user_input == 5:
            intro()
        else:
            print("Invalid input. Please try again.")
            joins()

        print(f"Please select a table: \n1. Player_Info \n2. Player_Skills \n3. Team \n4. Match \n5. Delivery")
        user_input = int(input("Enter your choice (1-5): "))
        if user_input == 1:
            table1 = "Player_Info"
        elif user_input == 2:
            table1 = "Player_Skills"
        elif user_input == 3:
            table1 = "Team"
        elif user_input == 4:
            table1 = "Match"
        elif user_input == 5:
            table1 = "Delivery"
        else:
            print("Invalid input. Please try again.")
            joins()

        print(f"Please select a table: \n1. Player_Info \n2. Player_Skills \n3. Team \n4. Match \n5. Delivery")
        user_input = int(input("Enter your choice (1-5): "))
        if user_input == 1:
            table2 = "Player_Info"
        elif user_input == 2:
            table2 = "Player_Skills"
        elif user_input == 3:
            table2 = "Team"
        elif user_input == 4:
            table2 = "Match"
        elif user_input == 5:
            table2 = "Delivery"
        else:
            print("Invalid input. Please try again.")
            joins()

        # Connect to the database
        conn = psycopg2.connect(
            dbname="431W",
            user="postgres",  # Default username
            password="Manban12!",
            host="localhost",  
            port="5432"
        )
        c = conn.cursor()
        use = input(f"What will you use this function on: ")
        key1 = input(f"Column from {table1}: ")
        key2 = input(f"Column from {table2}: ")
        
        c.execute(f"SELECT {use} FROM {table1} {join} {table2} ON {table1}.{key1} = {table2}.{key2}")
        rows = c.fetchall()
        for row in rows:
            print(row)
        
        conn.close()
        intro()

    def grouping():
        print(f"\nGrouping\n")
        
        print(f"Please select a table: \n1. Player_Info \n2. Player_Skills \n3. Team \n4. Match \n5. Delivery")
        user_input = int(input("Enter your choice (1-5): "))
        if user_input == 1:
            table = "Player_Info"
        elif user_input == 2:
            table = "Player_Skills"
        elif user_input == 3:
            table = "Team"
        elif user_input == 4:
            table = "Match"
        elif user_input == 5:
            table = "Delivery"
        else:
            print("Invalid input. Please try again.")
            grouping()

        # Connect to the database
        conn = psycopg2.connect(
            dbname="431W",
            user="postgres",  # Default username
            password="Manban12!",
            host="localhost",
            port="5432"
        )
        c = conn.cursor()
        use = input(f"What will you use this function on: ")
        key = input(f"Column to group by: ")
        
        c.execute(f"SELECT {use} FROM {table} GROUP BY {key}")
        rows = c.fetchall()
        for row in rows:
            print(row)
        
        conn.close()
        intro()

    def subqueries():
        print(f"\nSubqueries\n")
        print(f"Please select an option: \n1. Subquery in SELECT \n2. Subquery in FROM \n3. Subquery in WHERE")
        print(f"4. Subquery in GROUP BY \n5. Back")
        user_input = int(input("Enter your choice (1-5): "))
        table = ""
        if user_input == 1:
            subquery = "SELECT"
        elif user_input == 2:
            subquery = "FROM"
        elif user_input == 3:
            subquery = "WHERE"
        elif user_input == 4:
            subquery = "GROUP BY"
        elif user_input == 5:
            intro()
        else:
            print("Invalid input. Please try again.")
            subqueries()

        print(f"Please select a table: \n1. Player_Info \n2. Player_Skills \n3. Team \n4. Match \n5. Delivery")
        user_input = int(input("Enter your choice (1-5): "))
        if user_input == 1:
            table = "Player_Info"
        elif user_input == 2:
            table = "Player_Skills"
        elif user_input == 3:
            table = "Team"
        elif user_input == 4:
            table = "Match"
        elif user_input == 5:
            table = "Delivery"
        else:
            print("Invalid input. Please try again.")
            subqueries()

        # Connect to the database
        conn = psycopg2.connect(
            dbname="431W",
            user="postgres",  # Default username
            password="Manban12!",
            host="localhost",
            port="5432"
        )
        c = conn.cursor()
        use = input(f"What will you use this function on: ")
        key = input(f"Column to use in subquery: ")
        
        c.execute(f"SELECT {use} FROM {table} WHERE {key} IN (SELECT {key} FROM {table})")
        rows = c.fetchall()
        for row in rows:
            print(row)
        
        conn.close()
        intro()

    def transactions():
        print(f"\nTransactions\n")
        print(f"Please select an option: \n1. Begin Transaction \n2. Commit Transaction \n3. Rollback Transaction")
        print(f"4. Back")
        user_input = int(input("Enter your choice (1-4): "))
        if user_input == 1:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()
            c.execute("BEGIN TRANSACTION")
            conn.commit()
            conn.close()
        elif user_input == 2:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()
            c.execute("COMMIT")
            conn.commit()
            conn.close()
        elif user_input == 3:
            # Connect to the database
            conn = psycopg2.connect(
                dbname="431W",
                user="postgres",  # Default username
                password="Manban12!",
                host="localhost",
                port="5432"
            )
            c = conn.cursor()
            c.execute("ROLLBACK")
            conn.commit()
            conn.close()
        elif user_input == 4:
            intro()
        else:
            print("Invalid input. Please try again.")
            transactions()
        intro()

    def error_handling():
        print(f"\nError Handling\n")
        print(f"Please select an option: \n1. Raise an error \n2. Handle an error \n3. Back")
        user_input = int(input("Enter your choice (1-3): "))
        if user_input == 1:
            raise Exception("This is an error")
        elif user_input == 2:
            try:
                raise Exception("This is an error")
            except Exception as e:
                print(f"An error has occurred: {e}")
        elif user_input == 3:
            intro()
        else:
            print("Invalid input. Please try again.")
            error_handling()
        intro()
    intro()
if __name__ == '__main__':
    main()