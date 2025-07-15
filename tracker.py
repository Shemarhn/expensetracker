import psycopg2

conn = psycopg2.connect(
    dbname = "expensetracker",
    user = "postgres",
    passord = "Password",
    host = "localhost",
    port = "5432",
)





