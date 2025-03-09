# Python Simple To-Do List Project

Welcome to my simple to-do list project!

## Overview

This is a simple to-do list project. This program will allow you to add and remove tasks in your task list, as well as view and update the status of tasks. 

## How It Works

When you initialize the program, the following prompt will show:

> ***Welcome to the To Do List! Please enter one of the following:"***
>>1: Add Task
>>
>>2: Remove Task
>>
>>3: View Tasks
>>
>>4: Update Task Status
>>
>>5: Exit

If the input '1' is given, the following message will be displayed:

> ***Enter a name for your task:***

> **Enter a description for your task (type 'none' to enter a blank description***

> ***Enter a due date (YYMMDD):***

>***Enter the current status of your task:***

If the input '2' is given:

>***Enter the name of the task you would like to remove:***

If the input '3' is given, the current task list will be shown. Please note that if there is no current task list, the following will appear:

>***You do not have any tasks.***

If the input '4' is given, you will be prompted with the following:

>***Enter the name of the task you would like to update:***

>***Enter the new status of the task:***

## Update

Bugs Fixed:

Searching for tasks to remove when no tasks are available.
Date format not enforced.
Removing last task in a list would display an empty list.




