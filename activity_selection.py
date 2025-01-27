import random

# Activity Selection function
def activity_selection(start, finish, n):
    # sort activities based on finish time
    activities = sorted(zip(start, finish), key=lambda x: x[1])

    # initialize the first activity
    selected_activities = []
    last_finish_time = -1  # to keep track of the last selected activity finish time

    for i in range(n):
        # if the start time of the current activity is greater than or equal to the last finish time
        if activities[i][0] >= last_finish_time:
            # select the activity and update the finish time
            selected_activities.append(i)
            last_finish_time = activities[i][1]

    # print selected activities (index-based)
    print("Selected activities using iterative greedy approach are:")
    for i in selected_activities:
        print(f"Activity {i + 1}: Start = {activities[i][0]}, Finish = {activities[i][1]}")

n = 100
start = [random.randint(0, 50) for _ in range(n)]  # random start times between 0 and 50
finish = [random.randint(start[i] + 1, 60) for i in range(n)]  # finish times greater than start time, up to 60

activity_selection(start, finish, n)
