
def redminel_model(default_model):
    return {
        'issue':{
            "id": default_model['redmine_id'] if 'redmine_id' in default_model else None,
            "project_id": default_model['project_id'] if 'project_id' in default_model else None,
            "subject": default_model['title'] if 'title' in default_model else None,
            "priority_id": default_model['priority'] if 'priority' in default_model else None,
            "description": default_model['description'] if 'description' in default_model else None,
            "tracker_id": default_model['type_task'] if 'type_task' in default_model else None,
            "is_private": False,
            "custom_fields": [
                {
                    "id": default_model['to_custom_field'] if 'to_custom_field' in default_model else None,
                    "value": default_model['task_id'] if 'task_id' in default_model else None
                }
            ],
            "status_id": default_model['status'] if 'status' in default_model else None
        }
    }