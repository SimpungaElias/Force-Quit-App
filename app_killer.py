import subprocess

# Here you make app list
app_name = []

def force_quit_app(app_name):
    try:
        subprocess.run(["pkill", "-9", app_name])
        print(f"Force quit {app_name}.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    app_name = input("Enter the name of the application you want to force quit: ")
    force_quit_app(app_name)


