import urequests

def toDoList(token, project_id):

    url = f"https://api.todoist.com/rest/v2/tasks?project_id={project_id}"
    headers = {'Authorization': f'Bearer {token}'}
    
    try:
        response = urequests.get(url, headers=headers)
        tasks = []
        if response.status_code == 200:
            json_response = response.json()
            for task in json_response:
                content = task['content']
                due_info = task['due']
                due_date = due_info['date'] if due_info and 'date' in due_info else "Kein Fälligkeitsdatum"
                tasks.append((content, due_date))
                return tasks
        else:
            print("Fehler bei der Anfrage: Status-Code", response.status_code)
            todo_data = [["Task: Error", "Due to: Unknown"] for _ in range(11)]
            return todo_data
    except Exception as error:
        print("Ein Fehler ist aufgetreten:", error)
        todo_data = [["Error", "Unknown"] for _ in range(11)]
        return todo_data
    finally:
        if 'response' in locals():
            response.close()
    
