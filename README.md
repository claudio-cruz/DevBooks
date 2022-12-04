# DevBooks

[Visit the website here]()

![](/static/images/devbooks_views.png)

DevBooks is a platform where readers can find the best self-development books on the market, ranked and evaluated by readers and not us.

Readers can express their thoughts on the books they have read, read other readers' thoughts about particular books in which they are interested or not, and make a decision whether to read that book or not.

The books are ranked from the most liked (at the top of the page) to the least liked (at the bottom of the page). We also provide book categories so that users who are more interested in specific genres can filter books by the category they are looking for.

Our goal is for self-development book readers to easily find books that interest them to read next, using an easy and intuitive platform with short but concise book descriptions, feed back from other readers, and a list of filtered books by category that are ranked by reader likes from the top of the page to the bottom of the page. We also provide a "Buy Book" link that redirects users to the book seller page so that they can buy the books they like.

This website is made up of the following sections:

1. Home Page / contains a list of all books
2. Finace Category / contains the finance book list
3. Spiritual Category / contains the spiritual book list
4. Health Category / contains the health book list
5. Leadership Category / contains the leadership book list
6. Biographies Category / contains the biographies book list
7. About us / contains information about the website

The user goals of this website are:
1. Find good self-development to read next
2. Give feedback about each book
3. Read the feedback of other users about each book
4. See the most popular books
5. Access an easy and intuitively filtered book list
6. Interact with other self-development book readers
7. Find where to buy the book they want to read next

The business goals for this website are:
1. Earn a commission of the book sales from the book sellers linked to this page
2. Have targeted ads
3. Sponsering
4. Paid recommendations

## UX
---
### **Strategy**

With the UX in mind, I started to think about who the target users would be and how this website would help them reach their goals.

DevBooks target users are:
* Aged 12-60
* Readers who like self-development books
* People who are interested in self-growth and self-development

What these users would be looking for:
* Clear and concise information about self-development books
* List of the best self-developmemt books
* Readers feed back on each book
* A "Buy Book" link on every single book

This website reaches all those points, and more will be added in the future, like a "My Page" area where users can go and have access to their own information and be able to edit it, access to a favorite book list where users can add their favorite books to their own list, add new books to the main list (upon admin approval), and new categories will be added.

### **Scope**

In order to achieve the desired user and business goals, the following features will be included in this release:
* Navigation bar fixed on the top of each page to make navegation easy and intuitive
* Category Search dropdown list to filter the books by category
* Book Search dropdown list to isely find the book users are looking for
* Five diferent book categories(finance, spiritual, health, leadership, biographies)
* Register, login and logout futures
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

The skeleton of the website has changed since the initial draws. Originally, it was intended to be a simple home page with a tipping search bar where users could write and navigate to specific categories and books. During the website's development, I changed that to a list display of all the books ordered by the number of user likes. with two dropdown lists on the top of the book lists, one with the categories and the other with the books, making a better user experience.

The category pages were originally planned to have a top book list ranked by the admin, but with the development of the website, I decided to rank the books by the number of user likes so that users make the ranks and not the admin.

Both the login, logout, and registration pages are very similar, with a container in the middle of the page with the same sign just changing the content inside that container to create a better user experience.

### **Surface**

To avoid confusing users, I try to keep the website as simple as possible, with as few sections, buttons, and texts. Because users require high contrast and light colors for a better user experience, I used high color contrast and light colors.

For easy navigation, all the pages have a "go to top" button, reducing the scroling up and down. Also,  the book comment section has a dropdown button with all the user approved comments for a particular book and a go to the top of the comments button at the bottom of the comments.

I will go more in depth about this in the features section.

## **Features**
---
### *Navbar*

[Wireframes](/static/documents/nav_bars.pdf)