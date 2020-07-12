import subprocess
import time
import sys

max_retries = 20


def get_id_by_name(applications_running, name):
    for app in applications_running:
        if app.lower().find(name) > -1:
            return app.split(' ')[0]


def resize(applications):
    print(f'applications {applications}')
    retry = 0
    while len(applications) > 0:
        applications_running = subprocess.check_output(["wmctrl", "-lp"]).decode("utf-8").split("\n")
        print(f'applications_running {applications_running}')
        for index, app in enumerate(applications):
            application_id = get_id_by_name(applications_running, app['name'])
            if application_id:
                dimensions = "-e " f"0,{app['x']},{app['y']},{app['width']},{app['height']}"
                command = ["wmctrl", "-i", "-r", application_id, dimensions]
                subprocess.run(command)
                applications.pop(index)

        retry += 1
        if retry > max_retries:
            break

        time.sleep(5)


def handle_args():
    command = [sys.argv[1]]

    for i in range(len(sys.argv) - 7):
        command.append(sys.argv[7 + i])

    output = subprocess.Popen(command)

    applications = [{
        'name': sys.argv[2],
        'pid': output.pid,
        'x': sys.argv[3],
        'y': sys.argv[4],
        'width': sys.argv[5],
        'height': sys.argv[6]
        }]

    resize(applications)


def handle_file(file):
    applications = []
    with open(file) as f:
        for index, line in enumerate(f):
            props = line.split(' ')
            command = [props[0]]

            for i in range(len(props) - 5):
                command.append(props[5+i])

            output = subprocess.Popen(command)
            applications.append({
                'name': props[1],
                'pid': output.pid,
                'x': props[2],
                'y': props[3],
                'width': props[4],
                'height': props[5]
            })
    resize(applications)


def run():
    if len(sys.argv) > 2:
        if sys.argv[1] == "--file":
            handle_file(sys.argv[2])
        else:
            handle_args()
    else:
        print("\nInvalid number of arguments")
        print("\nUse the following arguments: ")
        print("\n<command> <Application name> <X Axios> <Y Axios> <Window width> <Window height>")
        print("\nOr: ")
        print("\n--file <path/to/configuration/file>")

    sys.exit(0)


run()
