class Task:
    task_dict = {}
    def __init__(self, task_name, description, due_date, status):
        self.task_name = task_name
        self.description = description
        self.due_date = due_date
        self.status = status
    
    def add_task(self):
        Task.task_dict[self.task_name] = {
            'Description': self.description,
            'Due Date': self.due_date,
            'Status': self.status
        }
        print(f' Task added. Updated task List: {Task.task_dict}')

    def remove_task(self):

        if self.task_name in Task.task_dict:
            if len(Task.task_dict) == 1:
                del Task.task_dict[self.task_name]
                print('Task removed. No tasks currently.')
            else:
                print(f'Task removed. Updated task List: {Task.task_dict}')
        else:
            print(f'{self.task_name} not found.')

    @classmethod
    def view_task(cls):
        if cls.task_dict:
            print(f'Current task list: {Task.task_dict}')
        else:
            print('You do not have any tasks.')
        
    def update_status(self, new_status):
        
        if self.task_name in Task.task_dict:

            Task.task_dict[self.task_name]['Status'] = new_status
            print('Status updated.')
            print(f'Current task list: {Task.task_dict}')
    

def get_valid_input(prompt, valid_responses, exit_avail=True):
    while True:
        user_input = input(prompt).strip().lower()
        if user_input == '5' and exit_avail:
            print('Goodbye!')
            exit()
        elif user_input in valid_responses:
            return user_input # Returning user input back to the function call
        else:
            print("I didn't get that, please try again.")
    

while True:
    welcome_input = get_valid_input("""Welcome to the To Do List! Please enter one of the following:"
1: Add Task
2: Remove Task
3: View Tasks
4: Update Task Status
5: Exit                        
    """, ['1', '2','3', '4',], exit_avail = True)
    if welcome_input == '1':
        task_name = input('Enter a name for your task:')
        description = input("Enter a description for your task (type 'none' to enter a blank description)")
        due_date = input('Enter a due date (YYMMDD):')
        status = input('Enter the current status of your task:')
        if description == 'none':
            description = None
        task = Task(task_name, description, due_date, status)
        task.add_task()
    elif welcome_input == '2':
        task_name = input('Enter the name of the task you would like to remove:')
        task = Task(task_name, None, None, None)
        task.remove_task()
    elif welcome_input == '3':
        task.view_task() 
    elif welcome_input == '4':
        task_name = input('Enter the name of the task you would like to update:')
        new_status = input('Enter the new status of the task:')
        task = Task(task_name, None, None, None)
        task.update_status(new_status)



        




        

