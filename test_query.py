import os
from time import sleep
from mysql.connector import connect, Error

sleep(2)
try:
    with connect(
        host="my_db",
        port=3306,
        user=os.environ.get("MYSQL_USER"),
        password=os.environ.get("MYSQL_PASSWORD"),
        database="db_mysql",
    ) as connection:
        print("MYSQL:", connection)

        select_bid = """SELECT client_number as client, 
                                SUM(outcome = "win") as win, 
                                SUM(outcome = "lose") AS lose 
                                -- SUM(CASE WHEN outcome = "win" OR outcome = "lose" THEN 1 ELSE 0 END) AS Totalwinlose 
                        FROM bid
                        INNER JOIN event_value
                        ON bid.play_id = event_value.play_id
                        GROUP BY client_number; """

        select_event_entity = """
                        SELECT least(home_team, away_team) AS A, 
                                greatest(home_team, away_team) AS B, 
                                COUNT(*)
                        FROM event_entity
                        GROUP BY A, B
                        HAVING COUNT(*) >= 1
                        ORDER BY A, B 
                            """

        def connect_sql(sql):
            with connection.cursor() as cursor:
                cursor.execute(sql)
                return cursor.fetchall()

        result = connect_sql(select_bid)
        print('User: ', 'wins: ', 'lost: ')


        for n, win, lose in result:
           print('|', ' '*3, n, ' '*5,
                      '|', ' ', win,
                      ' |', ' '*2, lose, '    |'
                      )

        result = connect_sql(select_event_entity)
        ss = '-'*57
        print('+'+ss+'+')
        print('+'+ss+'+')

        for event1, event2, res in result:

            s = f" {event1} {event2}"
            len_s = len(s)
            if len_s < 53:
                len_str = 53 - len_s
                print(f"| {event1} {event2}" + " "*len_str + (f"| {res}  |" if res < 10 else f"| {res} |"))
        print('+'+ss+'+')

except Error as e:
    print("ERROR:", e)
