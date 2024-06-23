# movie_info

Project 3 - Data Engineering

# Co-Creators

April Johnson

Trevor McDonough

Randy Silvey

# Project Overview

In this project, we took movie data supplied from the IMDB website, and used it to create an app where a user can select a genre and movie from drop downs to obtain additional information on the movie, including ratings. 

# Requirements

<ins> Instructions </ins>

For this track, your group will follow data engineering processes. Here are the specific requirements:

    1. Data must be stored in a SQL or NoSQL database (PostgreSQL, MongoDB, SQLite, etc) and the database must include at least two tables (SQL) or collections (NoSQL).

    2. The database must contain at least 100 records.

    3. Your project must use ETL workflows to ingest data into the database (i.e. the data should not be exactly the same as the original source; it should have been transformed in some way).

    4. Your project must include a method for reading data from the database and displaying it for future use, such as:

        ○ Pandas DataFrame
        ○ Flask API with JSON output

    5. Your project must use one additional library not covered in class related to data engineering. Consider libraries for data streaming, cloud, data pipelines, or data validation.

    6. Your GitHub repo must include a README.md with an outline of the project including:

        ○ An overview of the project and its purpose
        ○ Instructions on how to use and interact with the project
        ○ Documentation of the database used and why (e.g. benefits of SQL or NoSQL for this project)
        ○ ETL workflow with diagrams or ERD
        ○ At least one paragraph summarizing efforts for ethical considerations made in the project
        ○ References for the data source(s)
        ○ References for any code used that is not your own
 
    7. OPTIONAL: add user-driven interaction, either before or after the ETL process. e.g.:
 
        ○ BEFORE: provide a menu of options for the user to narrow the range of data being extracted from a data source (e.g. API or CSV file, where fields are known in advance).

        ○ AFTER: Once the data is stored in the database, add user capability to extract filtered data from the database prior to loading it in a Pandas DataFrame or a JSON output from a Flask API.

# Instructions

    1. Download the Data files from the IMDB Datasets page at https://datasets.imdbws.com/ and save to same folder as the loadAndMerge.py file.

        ○ title.ratings.tsv.gz
        ○ title.akas.tsv.gz
        ○ title.basics.tsv.gz 

    2. You will then need to extract the data. Go to a terminal, and use the following for each data file
    
        NOTE - MAKE SURE YOU'RE IN THE SAME FOLDER THE FILES ARE SAVED IN

        ○ gzip -d title.basics.tsv.gz
        ○ gzip -d title.ratings.tsv.gz
        ○ gzip -d title.akas.tsv.gz

    3. Run the loadAndMerge.py file. NOTE this can take anywhere from 10-20 minutes since the files are very large. 

        ○ The loadAndMerge.py file takes the three IMDB files and loads them each into a separate Mongo collection. 
        ○ The title.basics file is filtered for only titleType 'movie' and startYear greater than or equal to 2023.
        ○ The title.akas file is filtered on region 'US'.
        ○ The loadAndMerge.py file then merges the three collections, and creates a fourth combined collection.

    4. Run the app.py file by either:
        
        ○ Open a terminal, and navigate to the folder the project files are saved. Type 'Python app.py'.
        ○ Open the file in Visual Studio and click the Run button.

    5. Open the index.HTML file in a browser by either:
    
        ○ Open Visual Studio and right click on the file name, then select Open in Default Browser.
        ○ Open up a browser and go to the IP addess 127.0.0.1.

    6. You should now be taken to the app that will allow you to select a genre from a drop down, then a movie from the list of movies in a dropdown. 

# Database Used

For this project, we elected to use MongoDB. This gave us freedom to search the collections while testing using MongoDB Compass, as well as use coding used in class to combine the collections into one collection for the online app.

# ETL Workflow

See saved files QuickDBD-export.png and movies.txt for ETL workflow.

# Ethical Considerations

The information used in this project is public domain information. The files downloaded from IMDB were openly available for use. Diplaying this movie data on our app does not lead to any ethical concerns for the use of the data. 

# Data Sources

Data was obtained from the IMDB website at https://datasets.imdbws.com/. 

# Notes

Syntax assistance was obtained from Professor, classmates, and online forums such as Stack Overflow, Chat GPT, and library documentation.