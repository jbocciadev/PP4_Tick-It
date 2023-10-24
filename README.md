# [>_ tick·it](https://pp4-tickit-9f996504db3b.herokuapp.com/)

tick·it is a simple, user-friendly online ticketing system. With tick·it, your tickets will be resolved in no time, satisfaction guaranteed!

[Try it here!](https://pp4-tickit-9f996504db3b.herokuapp.com/)

![Responsive Mockup](/readme_files/tickit-responsive.jpg)

# The application
Based on real-life remedy ticketing systems, tick·it was developed with a user-first approach. With a clean, minimalistic visual design, users can easily find the information they are looking for. For staff, the interface is simple and clear, helping them save valuable time they can invest in fixing the issue, instead of navigating a complicated ticketing system UI.

## Features

- ### __Registration__

  - On clicking the "Register" link at the top of the page, the user is presented with a simple registration form. Once this is completed and submitted, the user is allocated the standard "user" profile, allowing them to log tickets straight-away.

- ### __Main (List) View__

  - Once users log in, they are brought to the ticket list view. As its name defines, the list view presents the user with the list of tickets they have access to.
    - __Customers__ will only have access to seeing tickets they have logged, regardless of their status.
    ![Customer list view](/readme_files/customer_list_view.PNG)
    - __Staff and Managers__ will only be able to see tickets that have not yet been closed, so they can work on them.
    ![Staff list view](/readme_files/staff_list_view.PNG)

- ### __Ticket (Detail) View__

  - __Customers__ will have access to viewing the ticket they submitted. From here, they can also delete the ticket should they wish to do so.
  ![Customer Detail View](/readme_files/customer_detail_view.PNG)

  - __Staff and Managers__ can use this view to:
  1. Change the ticket status.
  2. Assign the ticket to a different team.
  3. Assign the ticket to a different team member.
  ![Staff Detail View](/readme_files/staff_detail_view.PNG)

- ### __Ticket Logging__
  All users can open new tickets. In order to do so, they can click on the "New Ticket" button above the ticket list and fill in a very simple form. Once the ticket is submitted, it is assigned to the "Customer Care" team, who will do an initial assessment and troubleshooting and proceed according to their findings.
  ![New ticket form](/readme_files/new_ticket_form.PNG)


# Design

### Wireframes

  From very early in the development process, it was very clear that there was a need for simplicity and clarity. Pages are de-cluttered and minimalistic.

  - __Landing Page__ 

  ![Landing Page](/readme_files/Wireframes/Landing_page_wireframe.png)

  - __Table View__ 

  ![Landing Page](/readme_files/Wireframes/Table_view_wireframe.png)

  - __Detail View__ 

  ![Landing Page](/readme_files/Wireframes/Detail_view_wireframe.png)

### Background image

  - __Landing Page Background Image__ 

  An AI-generated image has been developed with the aim of evoking friendliness and technical expertise.

  ![Background image](/static/media/landing-background.webp)

  - __Colour Scheme__

  Continuing with the simplicity premise, a small and friendly set of colours was carefully selected.

  ![Colour Palette](/readme_files/tick-it_palette.png)


# Development

## Version Control

  - The chosen IDE for the development of the application was [Gitpod](https://www.gitpod.io/). Due to resource limitations, [Codespaces](https://github.com/codespaces/) was also used to finalise the project.

  - [GitHub](https://github.com) is the platform where the repository for ">_ tick·it" is hosted: [Jbocciadev tick-it](https://github.com/jbocciadev/PP4_Tick-It).

> Throughout development, the below commands were utilised to capture and store changes:
```
git add .
git commit -m "Message in quotation marks."
git push
```
>additionally
```
git pull
git stash
```

## Agile Development

  From the very begining, Agile development practices were adopted so as to maintain focus and keep track of the various requirements to be delivered.

  - As an agile development technique, __Github Projects__ was used, taking special focus on the Kanban project board view:
  ![Kanban Board](/readme_files/tick-it_kanban_board.png)

  - Issues were logged as either User Stories or Features, including acceptance criteria and adding comments where required. At the end of the development process, 2 User Stories had to be reassessed and classified as "Won't Have" in the MOSCOW model, due to time constraints.

  - ## Under the Proverbial Hood

    ### __Model__
    ![Tick-It ERD](/readme_files/tick-it_ERD.PNG)

    Along with Django's standard User model, another 3 custom models were developed:
      1. Profile. With a one-to-one relationship with the User model, this extends the latter and provides additional information about the different application users.
      2. Teams. This small table stores the name of the teams that will be composed be Users, via a many-to-one relationship.
      3. Ticket. This model connects all the others and is the cornerstone of the application functionality.
    
    #### __Forms__

    Django forms connect the Model and the View. Four forms comprise the forms.py file:

      - New ticket form:  
        ![TicketForm](/readme_files/ticket_form.png)

      - Ticket update forms:  
        ![3 ticket update forms](/readme_files/ticket_update_forms.png)
    
    ### __View__

    Django views govern the behaviour and logic behind every application. 

      - Landing Page View:  
        ![Landing](/readme_files/landing_page_view.png)

      - New Ticket View:  
        ![New ticket](/readme_files/new_ticket_view.png)

      - Delete Ticket View:  
        ![Delete ticket](/readme_files/delete_ticket_view.png)
      
      - 3 Ticket modification views, to update status, team and member.

    #### __URLs__

    Django urls.py is comprised by a list of available URLs, along with the views connected with each of these:  
    ![tick-it URLs](/readme_files/tick-it_urls.png)

    ### __Template__

    Django templates define the display of the information passed on by the views.  
    ![tick-it templates](/readme_files/tick-it_templates.png)


  ## Testing 

  Along the development process, continuous manual testing was carried out so as to ensure that User Stories were satisfactorily delivered.

  - Registration

  | Test | Result |
  |--|--|
  |User can create account| OK |
  |On account creation, user is allocated standard "customer" role| OK |
  |User can log in and out of the account| OK |

  - Navbar and footer

  | Test | Result |
  |--|--|
  |If user is not logged in, the navbar displays "Log in" and "register" options| OK |
  |If user is logged in, navbar displays "Log out" option| OK |
  |Navbar is responsive to desktop/tablet/mobile screen variations| OK |
  |All external hyperlinks direct to the appropriate url in a new browser tab| OK |

  - List View

  | Test | Result |
  |--|--|
  |On login, user is presented with a list of tickets| OK |
  |Depending on the user's role, the list will be either of own tickets, or of other's| OK |
  |When clicking on one of the list's rows, the full ticket is displayed| OK |
  |Staff members can only see not-closed tickets| OK |
  |Customers can not see team member's details| OK |

  - Ticket Detail View

  | Test | Result |
  |--|--|
  |Customers can not see team member's details| OK |
  |New tickets can only be logged if all fields are completed| OK |
  |Only staff members that belong to the assigned_team are displayed as options for edit| OK |
  |Creation date and author fields are displayed| OK |
  |"Delete Ticket" button is only available to ticket author| OK |

  - Security

  | Test | Result |
  |--|--|
  |Users cannot see ticket information if not logged in| OK |
  |Customers can ONLY see tickets that they created| OK |
  |Other than admin in admin view, only ticket authors can delete tickets| OK |
  |Despite manually changing the URL, tickets that were logged by other users cannot be deleted| OK |

    




  ### __Game Flowchart__

    > See below flowchart with the outline of the game logic:
    ![Game Flowchart](/assets/media/pp3_diego_santacarmen_flowchart.jpg)

 - ### __Helper Functions__
  The below minions have been defined to add to the visual appeal of the game:

  - clear()

    ```
    from os import system

    def clear():
        """
        Clears the terminal.
        See https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console
        """
        system("clear")
    ```


  - t_print()
    ```
    def t_print(message):
    """
    Prints the passed string to the console, simulating a typewriter.
    """
    for char in message:
        sleep(0.05)
        print(char, end='', flush=True)
    ```


  - travel(origin, destination)
    ```
    def travel(origin, destination):
    """
    prints a sequence simulating the waiting time of a trip to the destination.
    """
    trip = [".         ", " .        ", "  .       ", "   .      ", "    .     ", "     .    ", "      .   ", "       .  ", "        . ", "         ."]
    for i in range(10):
        clear()
        print(f"{origin}{trip[i]}{destination}")
        sleep(0.3)
        cursor.hide()
    ```


## Future Development Opportunities

  - ### Here are some future implementations that were left for a further version:
    
    - __Rank promotion/demotion__: A reward-punishment logic can be implemented for every case resolution/failure so the player can ascend or fall in the ranks from traffic duty agent to Captain or Superintendent.

    - __Leaderboard__: building on the previous point, a leaderboard, could be implemented with the different players and their ranks.

    - __Coloured fonts/imagery__: as a visual improvement, colours can be implemented for the different sections/headings within the game, along with images/animations to be displayed.

## Testing and known issues

  - ### __Testing__

    - __PEP8__ The code has been submitted to the Code Institute PEP8 lint and all major issues were fixed. The ones that remain are due to strings being too long, or a character in a docstring that the lint recognizes erroneously as an escape character (L229). With regard to the strings length, it has been decided that they are to remain as is for design purposes.

      ![PEP8](/assets/media/pep8.PNG)

    - Every input request has been tested with blank and invalid inputs and they handle the data as expected.

    - The game has been tested both in the IDE's and heroku's terminals and they perform as expected.

  - ### __Known Issues__

    - An issue has been identified with the locations' descriptions' lengths. A function may be defined to parse through the individual strings and place line breaks in intervals so the text does not wrap breaking words.

    - When run on Heroku, the game title does is not cleared and users can scroll up in the terminal to see the game title. Since this does not disrupts the gameplay and remains almost inperceptible as an issue, ot has been decided to leave as-is.

  - ### __Bugs__
  No bugs have been found to remain in the code as presented.

## __Development and Version Control__

  - The chosen IDE for the development of the application was [Gitpod](https://www.gitpod.io/).

  - [GitHub](https://github.com) is the platform where the repository for "Where in the World is Diego Santacarmen" is hosted: [Jbocciadev Diego Santacarmen repository](https://github.com/jbocciadev/PP3_Diego_Santacarmen).

> Throughout development, the below commands were utilised to capture and store changes:
```
git add .
git commit -m "Message in quotation marks."
git push
```
>additionally
```
git pull
git stash
```

## __Deployment__
The application has been deployed to heroku. The steps taken were:

In [heroku](https://dashboard.heroku.com/apps): 
    
  1. Open the "new" menu and click on "Create new app".
  2. Fill form fields with app name and region (Europe). Click on "Create app".
  3. In the "Settings" section, click on "Add buildpack" and add Python and NodeJS, __in that order__.
  4. In "Deployment method", select the GitHub option and provide the repository details. Click on "Connect".
  5. Click on "Enable Automatic Deploys" and finally, click on "Deploy Branch".


## Credits 

### Inspiration
- The MS DOS version of Carmen sandiego was one of my first experiences with videogames, and it holds a special place in my heart. As soon as I saw that the project was supposed to be a command-line based application, and that many other students had chosen to develop a game, Carmen Sandiego was the first thing that came to my head. I must admit that the development process has been more complicated than initially expected, the satisfaction of having a running version of this game is unmeasurable.

- [This](https://carmensandiego.fandom.com/wiki/Where_in_the_World_is_Carmen_Sandiego%3F_(1985)) site helped in refreshing my badly-maintained memory.

### Code

- I cannot talk code without thanking Prof. David Malan and all the crew at HarvardX's [CS50X](https://cs50.harvard.edu/x/2023/).

- [stack __overflow__](https://stackoverflow.com/) if you code, you know ;-). This [article](https://stackoverflow.com/questions/517970/how-to-clear-the-interpreter-console) was a godsend. Also [this](https://stackoverflow.com/questions/983354/how-do-i-wait-for-a-pressed-key).

- [geeks for geeks](https://www.geeksforgeeks.org/) this [entry](https://www.geeksforgeeks.org/switch-case-in-python-replacement/) broke my heart so I decided to go with if-elif-else in loops. :-(

- [patorjk](https://patorjk.com/) is where I created the title for the game (Text to ASCII Art Generator).

- [realpython](https://realpython.com/python-main-function/) and [freeCodeCamp](https://www.freecodecamp.org/news/if-name-main-python-example/).

### Other
- First and foremost, I owe gratitude to my family for dinners without me and days out I missed because I needed to sit and work on this project. Their support has always been unwavering.

- A masive thank you to my mentor, Spencer and his [5pence](https://5pence.net/) site.

- Thank you, thank you, thank you to the staff and colleagues at [Code Institute](https://codeinstitute.net). Course content, Tutoring sessions and (especially) Slack channels.


--------------------
Extending user model:
https://docs.djangoproject.com/en/dev/topics/auth/customizing/#extending-the-existing-user-model
https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#proxy

Django models FK on_delete:
https://sentry.io/answers/django-on-delete/

Hover effects:
Ian Lunn https://ianlunn.github.io/Hover/

User authentication:
https://docs.djangoproject.com/en/4.2/topics/auth/default/ Login required mixin

Django Forms
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms

Querying with list of values:
https://stackoverflow.com/questions/9304908/how-can-i-filter-a-django-query-with-a-list-of-values

Form querysets:
https://docs.djangoproject.com/en/4.2/ref/models/querysets/ (see Q https://docs.djangoproject.com/en/4.2/ref/models/querysets/#django.db.models.Q and select_related)

Prepopulating forms with current values:
https://studygyaan.com/django/how-to-give-initial-value-to-model-forms?utm_content=cmp-true

Getting context data:
https://docs.djangoproject.com/en/4.2/ref/class-based-views/mixins-multiple-object/#django.views.generic.list.MultipleObjectMixin.get_context_data

Form to update team member assignment, based on assigned team:
https://stackoverflow.com/questions/1697702/how-to-pass-initial-parameter-to-djangos-modelform-instance


Querying:
 - Field lookups: https://docs.djangoproject.com/en/4.2/ref/models/querysets/#field-lookups
 - One-to-one relationships: https://docs.djangoproject.com/en/4.2/topics/db/examples/one_to_one/

Meme generator:
https://imgflip.com/

Bootstrap icons with Django:
https://pypi.org/project/django-bootstrap-icons/

Form to update team member assignment, based on assigned team // https://stackoverflow.com/questions/1697702/how-to-pass-initial-parameter-to-djangos-modelform-instance


Database ERD:
https://dbdiagram.io/d

code validators:
HTML: https://validator.w3.org/
CSS: https://jigsaw.w3.org/css-validator/
JS: https://jshint.com/
Python: VScode built-in "Problems" panel display.
 ======================

Known issues

Ticket list display on smaller screens breaks the boundaries and becomes scroll-left-to-right

Messages: there are instances where the JS for dismissing the messages generates an error. To this moment, I have 
    followed the steps laid out during the blog walkthrough and did troubleshooting and checked online, but due to ...