# 431W-Project
Brief explanation of all usable functions within the CLI-Interface. If you wanted to use this yourself, you would need to change the database that you are accessing with the code. There are a lot of parts where the database is opened, so you would need to make sure you change all of them to fit the database you created. 


# 1. Insert Data

Allows users to insert new records into the database. Users can insert records into player info, player skills, teams, matches, or deliveries.

Input:
Select the option number corresponding to the type of data you want to insert.
Follow the prompts to enter the required information for inserting the selected data type.

Output:
Upon successful insertion, the database will be updated with the new record.

# 2. Delete Data
   
Enables users to delete existing records from the database. Users can delete records from player info, player skills, teams, matches, or deliveries.

Input:
Select the option number corresponding to the type of data you want to delete.
Follow the prompts to enter the required information for deleting the selected data type.

Output:
Upon successful deletion, the specified record will be removed from the database.

# 3. Update Data
   
Allows users to update existing records in the database. Users can choose to update player information, player skills, teams, matches, or deliveries.

Input:
Select the option number corresponding to the type of data you want to update.
Follow the prompts to enter the required information for updating the selected data type.

Output:
Upon successful update, the database will be updated with the new information.

# 4. Search Data
   
Enables users to search for specific records in the database based on certain criteria. Users can search in player info, player skills, teams, matches, or deliveries.

Input:
Select the option number corresponding to the type of data you want to search.
Enter the query for the WHERE clause to filter the search results.

Output:
Displays the records that match the search criteria.

# 5. Aggregate Functions
   
Allows users to perform aggregate functions such as count, sum, average, min, and max on a selected column of a table.

Input:
Select the aggregate function you want to perform.
Choose the table on which to perform the aggregate function.
Enter the column on which to apply the aggregate function.
Optionally, enter a query for the WHERE clause to filter the data.

Output:
Displays the result of the aggregate function.

# 6. Sorting
   
Enables users to sort records in a table either in ascending or descending order based on a selected column.

Input:
Select the sorting order (ascending or descending).
Choose the table on which to perform sorting.
Enter the column to sort by.

Output:
Displays the sorted records.

# 7. Joins
   
Allows users to perform inner join, left join, right join, or full join between two tables.

Input:
Select the type of join (inner, left, right, or full).
Choose the first table for the join operation.
Choose the second table for the join operation.
Specify the column from each table to join on.

Output:
Displays the joined records.

# 8. Grouping
   
Enables users to group records in a table based on a selected column.

Input:
Choose the table on which to perform grouping.
Specify the column to group by.

Output:
Displays the grouped records.

# 9. Subqueries
    
Allows users to execute subqueries in the SELECT, FROM, WHERE, or GROUP BY clauses.

Input:
Select the type of subquery (SELECT, FROM, WHERE, or GROUP BY).
Choose the table on which to execute the subquery.
Specify the column to use in the subquery.

Output:
Displays the results of the subquery.

# 10. Transactions
    
Enables users to manage transactions by beginning, committing, or rolling back transactions.

Input:
Select the transaction operation (begin, commit, or rollback).

Output:
Executes the selected transaction operation.

# 11. Error Handling
    
Allows users to raise or handle errors for testing purposes.

Input:
Select the error operation (raise an error or handle an error).

Output:
Raises or handles the selected error.
