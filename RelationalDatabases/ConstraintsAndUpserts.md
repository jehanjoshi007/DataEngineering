### Constrants and Upserts

- Constraints can be of the type not null,unique,primary key etc.
- You can define a composite key as primary key(col1,col2).
- Sometimes while inserting data into a table you want to define
  if a conflict occurs what would you do ? update the values
  or ignore the row to be inserted as it already exists
  these are defined in upserts.

- example for ignoring the row to be inserted

```
insert into table1(col1,col2,col3)
values(val1,val2,val3)
on conflict(col1) do nothing
```

- example for updating values if conflict occurs

```
insert into table1(col1,col2,col3)
values(val1,val2,val3)
on conflict(col1)
do update
set (col2) = excluded.col2

```
- These are important to do bulk inserts when we don't know if
  value exists or not.
