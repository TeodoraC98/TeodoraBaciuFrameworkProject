github link:
https://github.com/TeodoraC98/TeodoraBaciuFrameworkProject
render link:
https://teodorabaciuframeworkproject.onrender.com


Admin username: teodoraB98
password:password
Coordinator:coordinator
Password coordinator: Password98
Database name: teodora-baciu-framework-project-database
Hostname:dpg-d2dq2u8dl3ps73b5b6hg-a
password:fKp33eHJUK31NJCzonuyGdxcAcIMnF9v

Internal Database UR:postgresql://teodora_baciu_framework_project_database_user:fKp33eHJUK31NJCzonuyGdxcAcIMnF9v@dpg-d2dq2u8dl3ps73b5b6hg-a/teodora_baciu_framework_project_database
External Database UR: postgresql://teodora_baciu_framework_project_database_user:fKp33eHJUK31NJCzonuyGdxcAcIMnF9v@dpg-d2dq2u8dl3ps73b5b6hg-a.frankfurt-postgres.render.com/teodora_baciu_framework_project_database

For this project I created a web page for hiking enthusiasts. In this project users are divided into two categories, coordinators and members.
The groups were created in the administration page
A coordinator has permission to control content: to add new routes, to modify their content (even if a route is not posted by him/herself), 
to delete content. A coordinator has permission to modify user data such as profile information or their access to posted routes, but cannot access authentication information.

A user who does not have a valid account cannot see the content on the page. 
If a user is not registered or logged in and tries to access a route's information, they are informed about the access limit and are provided with links to register or log in
To access content a user must become a member. 
I create a member group to give permission to the valid users to access the information about the trails and the coordinator that posts each trail

In the navigation bar, users can access the home page which contains the list of routes posted by all coordinators, they can log in or register, or if they are logged in they can access the profile page.
If the user is a coordinator, it can access the page to create a new instance for a route from the navigation bar.

On the home page users have a list of the routes instance. A user can access the data of a route by accessing the view button. 
The user is redirected to the route details page. The details page contains information about the route such as: difficulty level, duration, date, meeting point, but also data about the coordinator. Here the user can access the coordinator's profile. 
Also on the route details page a member can join the expedition by becoming a participant. A participant is a member that join to a specific route.
A carousel with all route participants is available on the page. 
Also here users can communicate with each other by posting a comment.
(an update to the page would be to develop the comments section that allows users to change or delete posted comments)
On the route details page, a coordinator can delete a route or update its information.
A coordinator can update all posted routes, even if they are posted by him or another coordinator.

-All users have the opportunity to update their profile data
-in case a user has forgotten their password, we have implemented the possibility of password recovery

GROUP Coordinator permission:

   Content Types | content type | Can add content type 
   Content Types | content type | Can change content type 
   Content Types | content type | Can delete content type 
   Content Types | content type | Can view content type 
   Sessions | session | Can add session 
   Sessions | session | Can change session 
   Sessions | session | Can delete session 
   Sessions | session | Can view session 
   Trails | comment | Can add comment 
   Trails | comment | Can change comment 
   Trails | comment | Can delete comment 
   Trails | comment | Can view comment 
   Trails | participant | Can add participant 
   Trails | participant | Can change participant 
   Trails | participant | Can delete participant 
   Trails | participant | Can view participant 
   Trails | trail | Can add trail 
   Trails | trail | Can change trail 
   Trails | trail | Can delete trail 
   Trails | trail | Can view trail 
   Users | profile | Can add profile 
   Users | profile | Can change profile 
   Users | profile | Can delete profile 
   Users | profile | Can view profile 


---------- group Member :
   Users | profile | Can view profile 
   Trails | trail | Can view trail 
   Trails | comment | Can add comment 
   Trails | comment | Can view comment 
   Trails | comment | Can delete comment 
   Users | profile | Can add profile 
   Users | profile | Can change profile 
