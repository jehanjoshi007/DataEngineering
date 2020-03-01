## DataWarehousing Concepts

### Facts and Dimension tables

- Facts consist of the metrics for the business.
- Dimensions are data points that provide description to metrics.
- Each dimension table will have one or more fact table.
- Example in a restaurant menu item names are dimensions and
  menu item prices are facts.

### Important Schemas for DataWarehousing

- Star Schema
- Snowflake Schema




### Star Schemas

![StarSchema](https://github.com/jehanjoshi007/MediaAssets/blob/master/StarSchema.png)
                          *source :- MSSQLTIPS*

- As We can see this is an example of a star schema.
- A central fact table joined with dimension tables, which looks like a star.
- This schema facilitates simple query logic and reporting.
- Better query performance.
- Faster aggregation.
- Such schema's are highly denormalized in state, so one off inserts and updates can
  result in data integrity issues.


### Snowflake Schema

![StarSchema](https://github.com/jehanjoshi007/MediaAssets/blob/master/SnowflakeSchema.PNG)
                          *source :- BluePiConsulting Post*

- This is similar to Snowflake schema the only difference is this can be the more
  normalized version of the star schema
- One or more dimensions are decomposed into separate tables and thus normalized.
- This can increase query costs.
- Can improve data integrity.
