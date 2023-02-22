from threading import Thread

def task():   # Function for thread to run
  print("Hello from the thread")

def main():
  thread = Thread(target=task)  # Create Thread
  thread.start()  # Start Thread
  print("Waiting for thread")
  thread.join()   # Once thread function finish executing return to main thread

if __name__ == "__main__":
  main()
