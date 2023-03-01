from flask import Flask, render_template, request

app = Flask(__name__)

# Define a dictionary to hold employee workload data
employee_data = {
    "John": {"tickets": 5, "working_on": 2},
    "Jane": {"tickets": 3, "working_on": 1},
    "Mike": {"tickets": 2, "working_on": 0},
    "Emily": {"tickets": 1, "working_on": 0}
}

# Define a function to calculate the employee's score based on their workload, number of tickets currently being worked on, and task severity
def calculate_score(workload, working_on, severity):
    # Assign weights to workload, number of tickets being worked on, and severity levels
    workload_weight = 0.4
    working_on_weight = 0.3
    severity_weight = 0.3
    
    # Calculate the score based on the weighted sum of workload, number of tickets being worked on, and severity
    score = (workload * workload_weight) + (working_on * working_on_weight) + (severity * severity_weight)
    
    return score

# Define the route to handle the form submission
@app.route('/', methods=['GET', 'POST'])
def task_allocation():
    if request.method == 'POST':
        # Retrieve form data
        employee_name = request.form['employee_name']
        num_tickets = int(request.form['num_tickets'])
        severity = int(request.form['severity'])
        
        # Calculate the employee's score
        employee_score = calculate_score(employee_data[employee_name]['tickets'], employee_data[employee_name]['working_on'], severity)
        
        # Determine the threshold score for task allocation
        threshold_score = 4.0
        
        # Check if the employee's score meets the threshold
        if employee_score >= threshold_score:
            # Allocate the task to the employee
            allocation_status = "Task allocated to {} successfully.".format(employee_name)
        else:
            # Display an error message indicating that the task cannot be allocated to the employee
            allocation_status = "Task cannot be allocated to {}. Please select another employee.".format(employee_name)
        
        # Render the template with the allocation status message
        return render_template('task_allocation.html', allocation_status=allocation_status)
    
    # If the request method is GET, render the form template
    return render_template('task_allocation.html')

if __name__ == '__main__':
    app.run(debug=True)
