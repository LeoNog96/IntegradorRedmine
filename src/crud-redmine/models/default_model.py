

def default_model (task_id,redmine_id, title, description, task_id,
    priority, project_id, type_task, status, to_custom_field):
    return {
        'task_id':task_id,
        'redmine_id': redmine_id,
        'title': "title,
        'description': description,
        'priority': priority,
        'project_id': project_id,
        'type_task': type_task,
        'status': status,
        'to_custom_field': to_custom_field
    }