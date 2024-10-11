# Initialize the data structures
undo_stack = []
renovation_queue = []
project_list = []

# Stack functions for undoing changes
def push(change):
    undo_stack.append(change)

def pop():
    if undo_stack:
        return undo_stack.pop()
    return None

# Queue functions for processing renovation tasks
def add_task(task):
    renovation_queue.append(task)

def process_task():
    if renovation_queue:
        return renovation_queue.pop(0)
    return None

# List functions for managing ongoing projects
def add_project(project):
    project_list.append(project)

def remove_project(project):
    if project in project_list:
        project_list.remove(project)

def list_projects():
    return project_list

# Example usage
if __name__ == "__main__":
    # Adding projects
    add_project("Kitchen Renovation")
    add_project("Bathroom Remodel")

    # Adding tasks to queue
    add_task("Install Cabinets")
    add_task("Tile Flooring")

    # Pushing changes to the stack
    push("Changed kitchen layout")
    push("Updated design plan")

    # Undoing the last change
    last_change = pop()  # This will remove "Updated design plan"
    print(f"Undid change: {last_change}")

    # Processing renovation task
    next_task = process_task()  # This will remove "Install Cabinets"
    print(f"Processing task: {next_task}")

    # Listing ongoing projects
    ongoing_projects = list_projects()
    print("Ongoing projects:", ongoing_projects)
