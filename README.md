# Group 17 Submission
1. Grading rubric is in `project3\grading.csv` file on `main` branch
2. Demo video is in `project3\README.md` file on `main` branch
3. Delta from project 2 is in `releases` section, `README.md` file as well as inside `project3\README.md` folder

# :money_with_wings: Spendwise

<hr>
<p align="center">
<a><img width=500 
  src="/docs/workflows/banner.jpg" alt="Empower Your Finances with SpendWise: Your Smart Money Manager"></a>
</p>
<hr>

![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub](https://img.shields.io/github/languages/top/ojas1901/spendwise?color=red&label=Python&logo=Python&logoColor=yellow)
![GitHub contributors](https://img.shields.io/github/contributors/ojas1901/spendwise)
[![DOI](https://zenodo.org/badge/431190543.svg)](https://zenodo.org/badge/latestdoi/431190543)
[![Platform](https://img.shields.io/badge/Platform-Telegram-blue)](https://desktop.telegram.org/)
[![codecov](https://codecov.io/gh/ojas1901/spendwise/graph/badge.svg?token=GOJZTYVHIH)](https://codecov.io/gh/ojas1901/spendwise)
[![CI](https://github.com/ojas1901/spendwise/actions/workflows/main.yml/badge.svg)](https://github.com/ojas1901/spendwise/actions/workflows/main.yml)
[![Lint](https://github.com/ojas1901/spendwise/actions/workflows/black.yml/badge.svg)](https://github.com/ojas1901/spendwise/actions/workflows/black.yml)
![Lines of code](https://img.shields.io/tokei/lines/github/ojas1901/spendwise)
![Version](https://img.shields.io/github/v/release/ojas1901/spendwise?color=ff69b4&label=Version)
![GitHub issues](https://img.shields.io/github/issues-raw/ojas1901/spendwise)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/ojas1901/spendwise)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ojas1901/spendwise)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/ojas1901/spendwise)

<hr>

## Demo Video


https://github.com/ojas1901/spendwise/assets/122955760/9ec8bc6c-ea94-4253-89b1-f46ee82085a2



# :star: Whats New (Release 3.0.0)

### Major Changes done by Group 17 Fall 2023 for Project 3 (Delta from Project 2)

- Added new feature where users can use voice commands to control the bot
- Added new feature to create and manage groups. Members of groups can split bills among themselves now.
- Added new feature to extract all transactions in the form of CSV file
- Added new feature to upload transactions in bulk by uploading a CSV file.
- Added new feature to add notes to transactions while adding them
- Added new feature to add income and track income for the month.
- Fixed a bug where currency conversion was hard coded. Now currecncy conversion is done in real time using APIs
- Fixed lot of unit tests which were not running before
- Improved repository quality by adding new meaningful badges
- Fixed previously not working github actions
- Streamlined development software development process by using GitFlow technique
- Fixed an issue where Telegram running on Apple Devices would crash the app

## About Spendwise

Spendwise is an easy-to-use Telegram Bot that assists you in recording your daily expenses on a local system without any hassle.  With SpendWise, users can easily record and categorize their spending, set budgets, visualize expenditure patterns, and more, all within the familiar Telegram interface. The new version of spendwise can now take voice inputs for commands
 
With simple voice/typed-in commands, this bot allows you to:
- Add/Record a new spending based on personal or shared expense category
- Add/Record recurring transactions
- Bulk-add transactions by uploading a CSV file.
- Display recurring transactions
- Display upcoming transactions
- Provide Email Alerts when monthly expenses exceeds the savings goal or budget
- Real time currency conversion using public APIs
- Personalised user information stored
- Monthly budget chart
- Show the sum of your expenditure for the current day/month
- Display your spending history
- Clear/Erase all your records
- Edit/Change any spending details if you wish to
- Download your expenditure history in the CSV format
- Visualize your spendings in the form of graphs/pie chart using the /chart option
- Email the history CSV file to yourself
- See the total daily/monthly expenditure in different currencies
- Add the income you receive from various sources and keep track of monthly income

---
Sample demos are shown below. They are run on a local machine.

- [:information_desk_person: Sample Demos](#information_desk_person-Sample-Demos)


---


<!-- [comment]: <> (## Demo) -->

<!-- [comment]: <> (https://user-images.githubusercontent.com/15325746/135395315-e234dc5e-d891-470a-b3f4-04aa1d11ed45.mp4) -->



# :rocket: Installation Guide

## 💻For users 
Check out the bot here: https://t.me/spend_vise_bot

## 💻For developers 
1. Install Python, atleast Python3

2. Clone this repository to your local system at a suitable directory/location of your choice

3. Start a terminal session, and navigate to the directory where the repo has been cloned

4. Run the following command to install the required dependencies:
```
  pip install -r requirements.txt
```
5. Download and install the Telegram desktop application for your system from the following site: https://desktop.telegram.org/

6. Once you login to your Telegram account, search for "BotFather" in Telegram. Click on "Start" --> enter the following command:
```
  /newbot
```
7. Follow the instructions on screen and choose a name for your bot. Post this, select a username for your bot that ends with "bot" (as per the instructions on your Telegram screen)

8. BotFather will now confirm the creation of your bot and provide a TOKEN to access the HTTP API - copy this token for future use.

9. Search for "Edit the system environment variables" on your local computer. Click on Environment Variables and create a new System Variable called "API_TOKEN" and paste the token copied in step 8.

10. In the Telegram app, search for your newly created bot by entering the username and open the same. Once this is done, go back to the terminal session. 
Make sure you export the PYTHONPATH variable to the main project folder
 ```
 python src/bot.py
```
11. A successful run will generate a message on your terminal that says "TeleBot: Started polling." 
12. Post this, navigate to your bot on Telegram, enter the "/start" or "/menu" command, and you are all set to track your expenses!

For more info on deployment(Heroku), check out the doc [here](https://github.com/mtkumar123/MyDollarBot/blob/main/CONTRIBUTING.md#more-tips-for-developers)

## Speech To Text setup
In order to use speech to text you need to setup google cloud and enable speech to text API from within the console. Below
are the detailed steps.
1. Go to `https://console.cloud.google.com` and create an account
2. Create a new project in google cloud console and select the project 
3. From the home page select `APIs and Services`
4. Select `Enable APIS and Services` on the top
5. Search for `speech for text` in the search box
6. Select `Cloud Speech-To-Text API` from search results
7. Click on `Enable` button
8. Click `Enable Billing` and follow the on screen instructions
9. Now from the navigation menu select `APIs and Services` and select `Credentials`
10. Click on `Create Credential` and chose `Service Account`
11. Add `Service Account Name` and click on create and continue
12. Now in the `Select a role` dropdown select `Basic` and then `Owner`
13. Click on `Done`
14. Now go back to `Credential` and select the service account you created under the service account list
15. Go to the `Keys` tab and click on `Add Key`
16. Click on `Create New Key`
17. Select `json` as key type and save the json file it generates
18. Rename the json file as `service_account.json` and copy it inside `/src` directory (The same place where bot.py exists) 

Now we are all done with the google speech to text api

## 💻For testing with Pytest
1. Some modules in testing require CHAT_ID environment variable to be set.
2. This is the specific ID that is maintained for your chat with the Bot.
3. While running the bot.py , get this id from line 72 and set it in your system environment variables.
4. This should ensure effective running of all tests.


# :information_desk_person: Sample Demos
### Voice Commands
I want to use my voice to control the bot
<p align="center"><img width="640" src="./docs/workflows/voice_commands.gif" alt=""></p>

1. Hold down the mic button on the right hand side of telegram window
2. Speak the command which you want to execute

### Budget

I want to increase/decrease my monthly budget.

<p align="center"><img width="700" src="./docs/workflows/budget.gif"></p>

1. Enter the `/budget` command
2. Enter the new budget amount (must be greater than 0)


### Add

I want to add the expenses based on personal or shared category

<p align="center"><img width="700" src="./docs/workflows/add_transaction.gif"></p>

1. Enter the `/add` command
2. Click on the date of the transaction
3. Click on the category to add
4. Give a note for the transaction
5. Type in the amount spent
6. Type the expenditure category "Personal" or "Shared"
7. The amount will be added to the total value

 ### addTransactionsFromCSV

I want to bulk add the expenses using a CSV.

<p align="center"><img width="700" src="./docs/workflows/addTransactionsFromCSV.gif"></p>

1. Enter the `/addTransactionsFromCSV` command
2. Upload the file in the required format: category, date (mm-dd-yyyy), value, notes
3. The transactions will be added.

### addMember

I want to add all the members in a group

<p align="center"><img width="700" src="./docs/workflows/addMember.gif"></p>

1. Enter the `/addMember` command
2. Enter the member name
3. Enter the member email address
4. Member will be added to the group

### memberList

I want to view all the members present in the group

<p align="center"><img width="700" src="./docs/workflows/memberList.gif"></p>

1. Enter the `/memberList` command
2. List of all the members will be visible

### splitBill

I want to split the bill accross all the members

<p align="center"><img width="700" src="./docs/workflows/splitBill.gif"></p>

1. Enter the `/splitBill` command
2. Enter the bill name
3. Enter the bill amount
4. Type/choose a bill creditor
5. Type/choose a bill debator
6. Type/choose 'There are no more debators'

### viewSplitBill

I want to view the bill which was splitted

<p align="center"><img width="700" src="./docs/workflows/viewSplitBill.gif"></p>

1. Enter the `/viewSplitBill` command
2. You will get a description about the bill splitted

### sendBill

I want to get the description of the bill splitted in a mail

<p align="center"><img width="700" src="./docs/workflows/sendBill.gif"></p>

1. Enter the `/sendBill` command
2. You will get a description about the bill splitted in a mail



### Add Recurring

I want to add the repetitive transactions

<p align="center"><img width="700" src="./docs/workflows/add_recurring.gif"></p>

1. Enter the `/addRecurring` command
2. Click the category
3. Click the frequency

### Display Recurring Transactions

I want to see the recurring transactions

<p align="center"><img width="700" src="./docs/workflows/recurring.gif"></p>

1. Enter the `/showRecurringTransactions` command

### Show upcoming transactions

I want to see the transactions which are upcoming

<p align="center"><img width="700" src="./docs/workflows/upcoming.gif"></p>


1. click '/displayUpcomingTransactions'

### Jokes

I am tired I want to listen to some jokes

<p align="center"><img width="700" src="./docs/workflows/joke.gif"></p>

1. Enter '/joke' command

### Export to CSV
I want to export all my transactions as a CSV file to use somewhere else

<p align="center"><img width="640" src="./docs/workflows/export_csv_video.gif" alt=""></p>

1. Use command /exportCSV

### See total Expenditure in different currencies

I want to convert my total daily or monthly expenditure in a different currency.

<p align="center"><img width="700" src="./docs/workflows/currencyWorking.gif"></p>

1. Enter the /displayDifferentCurrency command
2. Choose from the category of day or month
3. Next, Choose your currency from the options
4. You will get the converted price in that currency


### SendEmail 

I want to send myself an email for the savings record


<p align="center"><img width="700" src="./docs/workflows/email.gif"></p>

1. Make sure you add savings using '/addSavingsGoal' command
2. When you are exhausted your limit it will send you an email

# :grey_question: Documentation

The Documentation of the SpendWise application API, can be viewed at [Link to Documentation](https://github.com/ojas1901/spendwise/blob/main/proj2/Documentation%20SpendWise.pdf). For additional reference, refer to [Github Pages](https://mtkumar123.github.io/MyDollarBot/).


:heart: Acknowledgements
---
We would like to thank Dr. Timothy Menzies for helping us understand the process of building a good Software Engineering project. We would also like to thank the teaching assistants Andre Lustosa, San Gilson, Xueqi (Sherry) Yang, Yasitha Rajapaksha, Rahul Yedida for their support throughout the project.

❓ Eager to Contribute:
---
Read the contribution policy [here](https://github.com/ojas1901/spendwise/blob/main/CONTRIBUTING.md)
Also make sure to read development documentations provided above :)


:page_facing_up: License
---
This project is licensed under the terms of the MIT license. Please check [License](https://github.com/ojas1901/spendwise/blob/main/LICENSE) for more details.


:sparkles: Contributors
---

<table>
  <tr>
        <td align="center"><a href="https://github.com/utsavll0"><img src="https://avatars.githubusercontent.com/utsavll0" width="100px;" alt=""/><br /><sub><b>Utsavkumar Lal</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/neha7799"><img src="https://avatars.githubusercontent.com/neha7799" width="100px;" alt=""/><br /><sub><b>Neha Patil</b></sub></a></td>
    <td align="center"><a href="https://github.com/ojas1901"><img src="https://avatars.githubusercontent.com/ojas1901" width="100px;" alt=""/><br /><sub><b>Ojas Kulkarni</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/Viggy12126"><img src="https://avatars.githubusercontent.com/Viggy12126" width="100px;" alt=""/><br /><sub><b>Vighnesh Hegde</b></sub></a><br /></td>
    </tr>
</table>



# :calling: Support

For any support, email us at spendwisebot@gmail.com / mydollarbot@gmail.com / secheaper@gmail.com
