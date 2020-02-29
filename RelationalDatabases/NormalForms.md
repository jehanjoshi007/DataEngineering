### Normalization is an important concept when we talk about relational databases

- First Normal Form
- Second Normal Form
- Third Normal Form

### How to achieve _First Normal_ Form

- Each cell in your table must contain singular, atomic and unique values.
- Separate different relationship in different tables.
- Relate these tables with foreign keys.

### How to achieve _Second Normal_ Form

- You should achieve First Normal form first.
- Your primary key must uniquely identify the records in your table.
- example user_id uniquely identifies the users in customers table.

### How to achieve _Third Normal_ Form

- This being an iterative process Second Normal form should be achieved.
- In one row of data if you need information in cell A and cell B to
  identify cell C this is a transitive dependency.
- We should eliminate all such transitive dependencies and from cell A we
  should identify cell C.
- Ideally you can split the tables into two and use a foreign key relationship
  to achieve this.


###References :- Udacity Data Engineering Nano Degree. 
