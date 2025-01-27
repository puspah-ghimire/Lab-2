import random

# Recursive Activity Selection function
def activity_selection_recursive(start, finish, n, last_finish_time, selected_activities, index=0):
    # Base case: if we've gone through all activities
    if index == n:
        return selected_activities
    
    # Check if the current activity can be selected
    if start[index] >= last_finish_time:
        selected_activities.append(index)
        # Recurse to select further activities after the current one
        return activity_selection_recursive(start, finish, n, finish[index], selected_activities, index + 1)
    
    # If we can't select this activity, move to the next one
    return activity_selection_recursive(start, finish, n, last_finish_time, selected_activities, index + 1)

def activity_selection(start, finish, n):
    # Sort activities based on finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    # Unzip the sorted activities into separate start and finish times
    sorted_start, sorted_finish = zip(*activities)

    # Start the recursive selection
    selected_activities = activity_selection_recursive(sorted_start, sorted_finish, n, -1, [])

    print("Selected activities using recursive greedy approach are:")
    for i in selected_activities:
        print(f"Activity {i + 1}: Start = {sorted_start[i]}, Finish = {sorted_finish[i]}")

n = 100
start = [random.randint(0, 50) for _ in range(n)]  # random start times between 0 and 50
finish = [random.randint(start[i] + 1, 60) for i in range(n)]  # finish times greater than start time, up to 60

activity_selection(start, finish, n)
