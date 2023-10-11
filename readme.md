## Cinema_DWH_DBS local deployment guideline
Welcome!
Here desribed information how to run this on local environment.

- Required software:
    - PostgreSQL (or another convenient database);
    - VS Code;
    - Having access to AWS Redshift, Bigquery, Snowflake data warehouses, use either of them. I created a PostgreSQL database, because it`s an open-source database, and AWS Redshift is a Postgres-based data warehouse;
    - PowerBI.
      
- Run cunfiguration:
  - Go to **CreateDBsInPostgre** folder and execute SQL code to create databases and tables in PostgreSQL;
  - (optionally) Go to **CreateFakeSQL** and run `.py` scripts (it will create fake SQL-inserts);
  - Go to **InsertFakeSQL** and copy `.sql` scripts into PostgreSQL Query tool (it is to insert data into your newly created tables);
  - Go to **ETL_Python** and run `ETLfromPostgreSQL.py` (merges all tables, and loads to the "improvised" PostgreSQL data warehouse);
  - Go to **PBI** and open dashboards in PowerBI. There are several dashboards (switch pages through UI).
 
 'to be continued'
 
