# MySQL 
Precise code.
Use documentation.
use docstrings.

# DB
Locations

id: primary key
name: varchar
location: -do-

# Flask Routes

/list.json - all json location

```
{
name: "kiet1",
location: "23423.22,12313123.233"
}
```
`/ show me all the links /list /list.json /create /delete / update`

`/list - normal all location in plain html {% for location in locations}`

`/delete/<id>/ -  make a delete operation redirect to /list`

`/update/<id>/ - open a form filled with existing values redirect to /list`

`/create/ - should open a form with form attributes name and location`
