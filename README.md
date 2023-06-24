# DevBooks

[Visit the website here](https://devbooks2022.herokuapp.com/)

![](/static/images/devbooks_views.png)

Welcome to DevBooks, the ultimate platform for discovering top self-development books! Our site offers a comprehensive collection of the best books in this genre, evaluated and ranked by fellow readers.

Here at DevBooks, we empower readers to share their thoughts and opinions on the books they've read. By accessing user reviews, individuals can gather valuable insights and make informed decisions about their next reading choices. Our platform encourages an interactive community where readers can engage with each other's perspectives, fostering a vibrant and informed literary environment.

To ensure an effortless browsing experience, our books are thoughtfully categorized, enabling users to filter their search based on specific genres. This feature allows readers with particular interests to explore books tailored to their preferences.

Our primary aim is to connect self-development book enthusiasts with their next great read. With concise yet informative book descriptions, user feedback, and a meticulously ranked list of books by reader likes, finding compelling titles has never been easier. Additionally, we provide a convenient "Buy Book" link that directly redirects users to the respective bookseller page, simplifying the purchase process for those who have found their ideal book.

In addition to the reader-focused features, we have equipped the site with an administrative interface. Site admins have the authority to add new books to our ever-growing collection, update existing book information, as well as approve and delete user comments. This ensures the platform remains up-to-date and maintains a high standard of quality content.

At DevBooks, we strive to create an intuitive and user-friendly experience for all self-development book enthusiasts. Join our community today and embark on a journey of personal growth through the power of literature!

All the Agile processes and user stories can be found in the project section on GitHub. (It's set to public).

This website has educational purposes only.

This website is made up of the following sections:

1. Home Page / contains a list of all books
2. Finance Category / contains the finance book list
3. Spiritual Category / contains the spiritual book list
4. Health Category / contains the health book list
5. Leadership Category / contains the leadership book list
6. Biographies Category / contains the biographies book list
7. About us / contains information about the website

The user goals of this website are:
1. Find a good self-development book to read next
2. Give feedback about each book
3. Read the feedback of other users about each book
4. See the most popular books
5. Access an easy and intuitively filtered book list
6. Interact with other self-development book readers
7. Find where to buy the book they want to read next

The business goals for this website are:
1. Earn a commission on the book sales from the booksellers linked to this page
2. Have targeted ads
3. Sponsoring
4. Paid recommendations

---
## UX

### **Strategy**

With the UX in mind, I started to think about who the target users would be and how this website would help them reach their goals.

DevBooks target users are:
* Aged 12-60
* Readers who like self-development books
* People who are interested in self-development

What these users would be looking for:
* Clear and concise information about self-development books
* List of the best self-developmemt books
* Readers feedback on each book
* A "Buy Book" link each book

This website reaches all those points, and more will be added in the future, like a "My Page" area where users can have access to their own information and be able to edit it, access to a favourite book list where users can add their favourite books to their own list, add new books to the main list (upon admin approval), and new categories will be added.

### **Scope**

To achieve the desired user and business goals, the following features will be included in this release:
* A navigation bar fixed on the top of each page to make navigation easy and intuitive
* Category Search dropdown list to filter the books by category
* Book Search dropdown list to easily find the book users are looking for
* Five different book categories(finance, spiritual, health, leadership, biographies)
* Register, login and logout features
* Add a comment, edit a comment, or delete a comment.
* Like or dislike a book

### **Structure** 

Webpage scheme
![](/static/images/devbooks_map.png)

Database scheme
![](/static/images/database_scheme.png)

This website is structured as follows:
* Home page with a fixed navigation bar at the top, a search dropdown list, a list of all the books, and a footer
* Five category pages (finance, spiritual, health, leadership, and biographies) filtering the book list by categories
* About us page, with information about the website's goals and purpose
* Login and Logout pages for logging in and out
* Register page to create an account

### **Skeleton**

The skeleton of the website has changed since the initial. Originally, it was intended to be a simple home page with a tipping search bar where users could write and navigate to specific categories and books. During the website's development, I changed to a list display of all the books ordered by the number of user likes. with two dropdown lists on the top of the book lists, one with the categories and the other with the books, making a better user experience.

The category pages were originally planned to have a top book list ranked by the admin, but with the development of the website, I decided to rank the books by the number of user likes so that users make the ranks and not the admin.

Both the login, logout, and registration pages are very similar, with a container in the middle of the page with the same sign just changing the content inside that container to create a better user experience.

### **Surface**

To avoid confusing users, I tried to keep the website as simple as possible, with as few sections, buttons, and text. Because users require high contrast and light colours for a better user experience, I used high colour contrast and light colours.

For easy navigation, all the pages have a "go to top" button, reducing the scrolling up and down. Also,  the book comment section has a dropdown button with all the user-approved comments for a particular book and a go-to the top of comments button at the bottom of the comments.

I will go more in-depth about this in the features section.

---
## **Features**

### *Navbar*

[Wireframes](/static/documents/nav_bars.pdf)

This website has a fixed navigation bar at the top containing the DevBooks logo, and the home button, both of which redirect users to the home page when clicked. It also has a categories dropdown button with the five categories available (finance, spiritual, health, leadership, and biographies), and each of the category buttons redirects users to the respective category pages. After the categories button is the "About Us" button that redirects users to the About Us page, where users can find information about the webpage.

The navigation bar changes depending on whether the user is logged in or out.If users are logged in, a logout button appears in the navigation bar; if users are logged out, a login and register button appears in the navigation bar.

The navbar is responsive; it works with small screens, as shown in the wireframe above.

### *Drop-down searching menu*

![](/static/images/search_bar.png)

The drop-down search menu has two options: the drop-down category menu, which redirects users to the specific category page when clicked, and the drop-down book menu, which redirects users to the specific book they select when clicked.

### *Booklist on each page*

![](/static/images/book_list.png)

The book lists on the home page and the category pages are ordered by the number of users who have liked them. Each book has a specific book title, book image, and book description, and at the bottom of the book description, users can see the number of likes and comments that the specific book has. Users can also like or dislike the book by clicking on the heart logo, buy the book by clicking on the "Buy Book" button, and see the book comments in the dropdown button. If users are logged in, they can also add comments (upon admin approval of each comment) and edit or delete their own comments.

### *Footer*

![](/static/images/footer.png)

A simple footer with the social media links, all the external links open in the different window.

### *Login, Logout, and Register*

[Login, Logout, and Register](/static/documents/login_out_register.pdf)

* On the Register page, users have a form with the following fields: Username, E-mail (optional), Password, and Password confirmation
* On the login page, users can login with the login data they created on the registration page. Users can choose to "remember me" so that they don't have to enter their username and password again the next time they login. On the bottom of the form, users have a "sign up" option if they haven't created a login yet
* The Logout page is straightforward; users are asked if they are certain they want to log out
* All these actions have an alert message every time a user logs in, logs out and registers

### *Comments*

![](/static/images/comments.png)

Users can access the comments by clicking on the comments dropdown button. If users are logged in, they can see an Add Comment form so that they can add a comment to that particular book. Users can also view a list of approved comments, as well as information about who submitted them and when they were written. For the comments written by the comment author, it shows two buttons under that user's comments: Edit and Delete buttons to edit and delete the comment. On the bottom of all comments, users have a "Back to top" button to go back to the top of the comments.

### *Edit Comments*

![](/static/images/edit_comment.png)
![](/static/images/edit_comment_modal.png)

When users click on the "edit" button, the edit comment form shows up and looks like the image above. It has a body field so that users can edit their comments. After editing the comment, users click on the "edit comment" button, and it will show a confirmation modal asking users if they want to edit the comment. If they confirm the comment is edited, the comment will be published.

---
## Technologies Used

The main technologies used are the following:
* GitHub
* HTML
* CSS
* JavaScript
* Python
* Django

---
## Testing

### *Manual testing*

1. Navbar:
- [x] The logo, home, about us, register, log in, and log out navigation links work correctly.
- [x] The category dropdown menu works correctly.
- [x] The category links in the category drop-down work correctly.
- [x] The navbar is responsive to all screen sizes.
- [x] The burguer menu tuggle works correctly, and all the abave links work.
- [x] The navbar shows correctly the log in and register links when users aren't authenticated.
- [x] The navbar shows the log out link correctly when users are authenticated.

2. Home Page:
- [x] The category dropdown filter displays all the category links correctly with the respected category icons.
- [x] The category links in the dropdown filter work.
- [x] The book dropdown filter displays all the book links correctly.
- [x] The book links in the dropdown book filter redirect users to the book they click on.
- [x] All books are displayed on the main page as a list, and it is responsive to all screen sizes.
- [x] The same buton works in each of the books.
- [x] The book-like count works correctly.
- [x] The buy button works correctly and redirects the users to another site on another webpage to buy the book.
- [x] The comments dropdown button works correctly and displays a list of the approved comments for each book.
- [x] The comment form is displayed for authentication users.
- [x] the comment form handles empty comment submitions
- [x] The comment form will submit successful comments and display an error message that says the comment is waiting for admin approval.
- [x] Each comment has the user comment owner, the date that the comment was created, and the correct comment.
- [x] If the user is authenticated and the owner of the comment, two buttons are displayed under the comment (delete and edit) correctly.
- [x] The comment edit works correctly and displays an alert message when a comment is edited successfully.
- [x] The comment deletion works correctly and displays an alert message when a comment is successfully deleted.
- [x] In the comments list, users have a 'Back to Top button, which redirects them to the top of the comments.
- [x] The 'go back to top' button in the right-down corner displays correctly after users scroll down the page and successfully redirects users to the top of the page when clicked.
- [x] The footer links work correctly and open the respective links in a new tab.
- [x] The home page is responsive to all screen sizes.

3. Log in and log out forms:
- [x] The log-in form handles incorrect or empty inputs correctly.
- [x] When the user log-in values are correct, the user is correctly logged in and redirected to the home page with a successful allergy message.
- [x] The link to the sign-up form under the login form redirects the user to the sign-up form correctly.
- [x] The logout page display correctly the question if the user wants to log out and duspley the user name correctly.
- [x] When the logged out button is clicked the user is logged out succesfully, redirected to the home page with a succesful alert message.
- [x] The forms are responsive to all screen sizes.

4. Sign up form:
- [x] The sign-up form correctly handles empty inputs, displaying a message telling users not to leave empty fields, with the exception of the email input field because that field is optional.
- [x] New users can successfully create an account, being redirected to the home page with a successful login message.

5. Book category pages:
- [x] The five category pages (Finance, Spirituality, Health, Leadership, and Biographies) display the books correctly by category with the exact same style as the home page book list.
- [x] All functionalities mentioned on the home page work correctly on the five different category pages.
- [x] When users like a book or submit a comment on one of these five category pages, they are redirected to the page they are on.

---
### *Lighthouse*

[Lighthouse](/static/documents/lighthouse.pdf)

The lighthouse results were improved.

### *HTML, CSS, and JavaScript Validation*

* The "W3C HTML Validator" found some errors in my HTML files, but only related to the Django tags.
* The "W3C CSS Validator (Jigsaw)" found no errors in the CSS file.
* The "JSHint JavaScript Validator" found no errors in the JavaScript file.
* There is no python PEP8 erros.

### *Bugs and fixes*

* I attempted to add a modal to the comment delete button so that users could confirm the deletions, similar to the modal I used in the edit comment, but it gave me a bug, broke the page, and I had to refresh the page to resolve it. I tried different versions of the modal, but apparently Bootstrap modals don't work inside dropdown lists, so I had to remove the modal.
* The alert messages work well, but if users thrigger to fast two messages before the page refresh, for exemple if users click two times to fast on like and dislike a book, the website shows the two alert messages at the same time, but just the first one desapear after two seconds, the second mesage dont desapear. This problem can be resolved by refreshing the page.

---
## Deployment

* These are the steps for deploying the project to Heroku:
1. Create a Heroku account (if you don't have one already)
2. Create a Heroku app:
3. Click “New”
4. Click “Create new app”
5. Give your app a name and select the region closest to you, then click “Create app”.
6. Create a ElephantSQL.com account (if you don't have one already)
7. Create a new database in ElephantSQL:
8. Log in to ElephantSQL.com and click ”Create New Instance”
9. Give your plan a Name
10. Select the Tiny Turtle (Free) plan
11. You can leave the Tags field blank
12. Select “Select Region”
13. Select a data center near you
14. Then click “Review”
15. Check if your details are correct and then click “Create instance”
16. Return to the ElephantSQL dashboard and click on the database instance name for this project
17. In the URL section, click the copy icon to copy the database URL
18. Create an env.py file:
19. Make sure that the file is at .gitignore file
20. write “import os” on the top of the env.py
21. Set a DATABASE_URL variable to the value you just copied from the ElephantSQL.com os.environ["DATABASE_URL"]="<copiedURL>"
22. Add a SECRET_KEY (can be whatever you like) os.environ["SECRET_KEY"]="my_super^secret@key"
23. In your settings file comment out the DATABASES and add the code beloew,
![](/static/images/databaseexp.png)
24. Save your file and run the migration command "python manage.py migrate"
25. Go back to the Heroku dashboard open the Settings tab
26. Add two config vars: "DATABASE_URL, and for the value, copy in your database URL from ElephantSQL, no need to add quotation marks." SECRET_KEY containing your secret key."
27. Create a Cloudinary account at https://cloudinary.com/ (if you don't have one already)
28. In Cloudinary Dasgbord, copy the API Environment variable and paste it on env.pu like this: "os.environ["CLOUDINARY_URL"] = "your Cloudinary URL" " (don't forget to remove the "CLOUDINARY_URL=" on the bigining of the API Environment variable that you just copied)
29. Add the same value to heroku Config Vars exp "CLOUDINARY_URL" "the value you copied"
30. Update the settings.py and set the debug to False
31. Create an "Procfile", in it write "web: gunicorn projectName.wsgi"
32. On Heroku select your app that you created and click "Deploy"
33. Connect your GitHub with Heroku, select the name of your project, scroll down, and select "Deploy Branch" and your project will be deployed to Heroku.


---
## Credits

I used code from the following resources:
* [Navbar](https://getbootstrap.com/docs/4.0/components/navbar/)
* [Book List](https://freefrontend.com/bootstrap-lists/)
* [Login, Logout, and Register](https://mdbootstrap.com/docs/standard/extended/login/)

I used media frm:
* [Background image](https://unsplash.com/)
* Book cover images were taken from the books' webpages.
