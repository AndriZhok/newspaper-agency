# Newspaper agency

## Introduction
Welcome to our Django-based Newspaper Management System. This project is built to streamline newspaper publication management through a simple and efficient user interface. The system allows for the creation of newspapers, management of redactors, and organization of topics. It is designed to simplify the process of producing and managing content, offering a straightforward solution for news agencies and independent publishers.

# Key features

1. Newspaper Management
- Create, View, and Edit Newspaper: Reductor can create new Newspapers, view Newspaper details, and edit existing Newspapers.
2. Reductor Management
- Reductor Creation: Reductor can create new Reductors through a dedicated form.
- Reductor Information: View and update user information.
3. Topic Management
- Topic Creation and Management: Add and manage Topics associated with Newspaper, improving organization and searchability.


## Check it in out!

[Newspaper Agency project deployed to Render](https://newspaper-agency-rele.onrender.com)

#### If you want to visit the page use this:
```
login: user
password: user12345
```


# Installation Instructions


```sh
- git clone https://github.com/AndriZhok/newspaper-agency.git
- cd newspaper-agency
- python -m venv env
- env\Scripts\activate or source env/bin/activate on mac
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py runserver
- go to http://127.0.0.1:8000/
```

# Usage guide

1.	Main Page
URL: /catalog/
View: index
2.	Logout
URL: /logout/
View: logout
3.	Newspaper List
URL: /newspaper-list/
View: NewspaperListView.as_view()
4.	Newspaper Detail
URL: /newspaper-detail/<int:pk>/
View: NewspaperDetailView.as_view()
5.	Newspaper Creation
URL: /newspaper-create/
View: NewspaperCreateView.as_view()
6.	Newspaper Update
URL: /newspaper-update/<int:pk>/
View: NewspaperUpdateView.as_view()
7.	Newspaper Delete
URL: /newspaper-delete/<int:pk>/
View: NewspaperDeleteView.as_view()
8.	Redactor List
URL: /redactor-list/
View: RedactorListView.as_view()
9.	Redactor Detail
URL: /redactor-detail/<int:pk>/
View: RedactorDetailView.as_view()
10.	Redactor Creation
URL: /redactor-create/
View: RedactorCreateView.as_view()
11.	Redactor Update
URL: /redactor-update/<int:pk>/
View: RedactorUpdateView.as_view()
12.	Redactor Delete
URL: /redactor-delete/<int:pk>/
View: RedactorDeleteView.as_view()
13.	Topic List
URL: /topic-list/
View: TopicListView.as_view()
14.	Topic Creation
URL: /topic-create/
View: TopicCreateView.as_view()
15.	Topic Update
URL: /topic-update/<int:pk>/
View: TopicUpdateView.as_view()
16.	Topic Delete
URL: /topic-delete/<int:pk>/
View: TopicDeleteView.as_view()

# demo
<img width="1037" alt="image" src="https://github.com/user-attachments/assets/600cd314-9991-48b7-b41a-0ce576913ed2">

