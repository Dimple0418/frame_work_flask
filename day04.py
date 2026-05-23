'''
GET-- This GET  request is used to retrieve data from the server . [Data Visible]
POST -- This POST request is used to send data to the server .
PUT -- This PUT request is used to update existing data on the server .
DELETE --> This DELETE request is used to delete data from the server .

#control structure 
-------------------
1.condition
2.loops


1)conditions
-----------
syntax:-{%Condition or loop %}
{% if marks >= 35 %}
    <h2> Pass </h2>
{%else%}
     <h2> Fail </h2>
{% end if%}

2)loops
-------
syntax:-{%Condition or loop %}
{% for item in subjects %}
    <p>{{item}}</
{%end for%}



Template Inheritence
---------------------
This allows one HTML file to reuse another HTML file

GET --> request.args.get
-------------------------
-->Values Throught URL

POST--> request.form
--------------------
---> Data Submitted from HTML

JSON data -->request..get_json()
---------
--> The structure data sent in API request
'''
