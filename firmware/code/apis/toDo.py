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
        else:
            print("Fehler bei der Anfrage: Status-Code", response.status_code)
    except Exception as error:
        print("Ein Fehler ist aufgetreten:", error)
        tasks = None
    finally:
        if 'response' in locals():
            response.close()
    
    return tasks
