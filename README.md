# psycopg2-college
psycopg2-college was an assignment given by my Database course's professor at university, where we had to work with the Psycopg2 module on Python. Please keep in mind that I could use neither any external module nor more than one file (script.py).

As you can probably deduce, this was my first time programming in Python. I could have done a few things differently, but I'm quite proud of the final results. I decided to create this repository and maybe work on this project once I have some spare time! 


This was the database structure given:
- Sailor ( id:int , name:char(50), address:char(50), age:int, level:float)
- Boat ( bid:char(25) , bname:char(50), size:char(30), captain:int)
captain is a FK to Sailor and no attribute can be null.

Below you can find the instructions given by the professors:
1. Drops the two tables from the database if they already exist.
2. Creates the two tables as described in the database structure above.
3. Generates 1 million (random) tuples, so that each tuple has a different value for the level attribute, and inserts them into the table Sailor. Make sure that the last inserted tuple, only that one, has the value 185 for the level attribute.
4. Generates one more million (random 1 ) tuples and inserts them in the table Boat.
5. Retrieves from the database and prints to stderr all the id of the 1 million sailors.
6. Updates all tuples that have value 185 as level and makes them have a level equal to 200 – (your query should work even if many tuples have value 185 in the attribute level ).
7. Selects from the table Sailor and prints to the stderr the id and the address of the sailors with level 200.
8. Creates a B+tree index on the attribute level.
9. Retrieves from the database and prints to the stderr the id of the 1 million sailors.
10. Updates all the tuples that have value 200 as level and makes them have a level equal to 210 -- (your query should work even if many tuples have value 200 in the attribute level ).
11. Selects from the table Sailor and prints to the stderr the id and the address of the sailors with level 210.

Below you can find the output expected by the assignment:

For each of the above operations, you need to report (print to the stdout ) the time it took to execute it. To do it you may keep in a variable the time before starting the execution (in nanoseconds), then get the system time after the execution has been completed and the difference in nanoseconds is the approximate time it took for the step to execute.
