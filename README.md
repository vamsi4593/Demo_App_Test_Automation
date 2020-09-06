# Demo_App_Test_Automation
UI :
Create a user with 
username : vamsi4593
password : vamsi@4593
firstname : vamsi
lastname : panganamala
phone : 0403636704

API :
Create user in UI, with username and password with which you want to test and pass as parameters in the test.

Q1 : How do you review code? 
Answer : Create a pull request ,when some changes are requested to be merged to the main branch.During this pull request other developers can check the code and comment changes.
Author of the code can select the reviewer for the code.The reviwer can add the general comment  to each line of code.

Q2 : How do you enforce coding standards? 
Answer : It is always better to have some style guide followed by everyone , than each developer having own style.Before any project starts , guidelines should be made for 
better modularity and re-usability of the code.These guidelines can be enforced by conducting code reviews.

Q3 : How do you plan what kind of approach you take for test automation - what libraries to use, how does it work in couple of years, how to make it easy to maintain, etc? 
What are the main points to consider? 
Answer : A well-developed framework not only helps in ensuring a higher degree of agility for testing teams or helps in testing faster and enable quicker retesting,it also 
helps in expand test coverage whilst ensuring right test coverage, while still allowing you to test across the board without sacrificing quality.
For any automation test sttrategy to work , one should consider libraries to be used, maintainability and and longevity of the test framework.A careful and structured approach 
for a test autmation startegy should focus on the elements of the test framework itself --> Library, Test Data Sources, Test Environments, Helper Functions, Modules and 
Structure & Hierarchies.
Libraries -- Should be seperated into their components as you will need to start with parts that are easy to trace and easyto build into framework.By creating custom libraries 
to support your own framework.
Test Data Sources --  By separating test script logic from test data, you will ensure the scripts are reusable and easy to maintain.For every set of inputs and actual results,
you you have at least one data source.when data is hardcoded into scripts , they fail each time when changes are made.
Test Environments -- Defining the list of environments that test should cover,broken down into type - OS, Devices and and systems.The list of devices , systems and os will be
increasing exponentially as years pass.It is important to take these groupings into consideration from very beiginning.
Helper Functions -- Such as Setup Scripts and Cleanup Scripts used to scrub the databases or scripts used to access external information.These scripts are ctach all those which
are not user's action and save lot of time.Combining the Helper Function and Test Environments play a key role.
Modules -- These are bigger part of any Test Automation Framework.Each module is a combination of library items, with their helper functions, environments, and data sources,
that together highlight a single product capability.Modules laid out this way helps in linking defects to a particular feature.
Structures & Hierarchies : Developing a folder structure for the modules represent the format of the application under test.these structures in place will help to track bugs 
faster,tracken them to requirements and tie them to releases,which will pay off in long run.

Q4 : Code testability, how do you enforce it? 
Answer : Any code can be defined testable when it can be verified programmatically and in a very granular way.Code testing can be enforced by implementing the Unit testing and 
Acceptance Test Driven Development(ATDD) or Behavioral Driven Development(BDD).

Q5 : How do you make sure that the product is testable?
Answer : Any product can be testable when a product takes input and gives an output.Testing can be done on this product by gving different types of input and check the expected
outcome to verify the intended behavior of the product.

Q6 : Recommendations for the APP :
1 . It would be better if Demo app and index app have followed case sensitivity.
2 . Show the rules to the user in setting password and username.
3 . Show the error to customer if there are no Alpha numeric characters in the registration page.

Q7 : Exploratory Testing :
1. An user is allowed to register with just the space characters  --> Not a desired functionality : FAILED CASE.
2. Phone fields allow alpha numeric characters --> Not a desired functionality : FAILED CASE.
3. Email field allows to register with no '@' character --> Not a desired functionality : FAILED CASE.

Q8 : If you would be given a week to do quality assurance for this product, briefly plan the tasks based on your skills, knowledge and expertise.
1. Understand the requirements and acceptance criteria.
2. Create Test Cases and schedule a Test Case review Meeting with the related stakeholders.
3. Post Approval of test Case , Perform Manual testing of UI and API testing using Soap API.
4. Report the Defects if any
5. Develop the Test Automation and run the tests 2-3 times.Add the recommendations if any.
6. Create the Test report with cases and bugs.
7. Arrange the Test Approval meeting and Decide on the GO-LIVE date.Prepare for Post production test data.
4. Develop the documentation on the behavior and functionality of the product.
