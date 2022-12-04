# DevBooks

[Visit the website here]()

![](/static/images/devbooks_views.png)

DevBooks is a platform where readers can find the best self-development books on the market, ranked and evaluated by other readers.

Readers can express their thoughts on the books they have read, read other readers' thoughts about books they are interested, and make a decision whether to read that book or not.

The books are ranked from the most liked (at the top of the page) to the least liked (at the bottom of the page). We also provide book categories so that users who are more interested in specific genres can filter books by the category.

Our goal is for self-development book readers to easily find books that interest them, using an easy and intuitive platform with short but concise book descriptions, feedback back from other readers, and a list of filtered books by category that are ranked by reader likes from the top of the page to the bottom of the page. We also provide a "Buy Book" link that redirects users to the bookseller page so that they can buy the books they like.

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
1. All internal links work properly.
2. All external links work properly and open in another window.
3. The "Go to the top of the page" button brings users to the top of the page and only shows up when users scroll down the page.
4. The Category and Books dropdown search bar redirect users the the correct Category page or Book.
5. The book lists are correctly displayed and ordered by the number of likes on each page.
6. The like and dislike buttons work and show the number of likes for each book.
7. The "Buy Book" button redirects the users to the bookseller page in an external window.
8. The comment dropdown button shows the correct number of comments on each book and when clicked shows the comments of the selected book.
9. In the comment dropdown, if users are authenticated, it shows the add comment form, and users can add comments to the books correctly.
10. Only comments approved by the admin are displayed in the comments list.
11. If authenticated, users can edit or delete their own comments.
12. Each time a comment is added, edited, and or deleted, users get a confirmation alert message that dissipates within two seconds.
13. The "Back to top" link at the bottom of the comments list correctly returns users to the top of the comments.
14. When a book is added to the list, if it has no Cloudinary image, a placeholder image is added by default.
15. Login works properly, and when a user logs in, a success allert message appears.
16. Logout works properly, and when a user logs out, a success allert message appears.
17. User Registration works correctly, and when a user registers, it shows a success allert message.
18. If users are logged out, the navbar only shows the login and registration options.
19. If users are logged in, the navbar only shows the logout option.
20. The navbar changes to a hamburger button menu with less the 990px screen size.
21. The website is totaly responsive to the different screen sizes and all its main functions work properly in the different sizes.

### *Lighthouse*

[Lighthouse](/static/documents/lighthouse.pdf)

The lighthouse results aren't all above 90 percent, but they are something I'm aware of and working on.

### *HTML and CSS Validation*

* The "W3C HTML Validator" found some errors in my HTML files, but only related to the Django tags.
* The "W3C CSS Validator (Jigsaw)" found no errors in the CSS file.

### *Bugs and fixes*

* 



