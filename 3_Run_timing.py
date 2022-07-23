
def run_timing():
    times = []
    while True:
        response = input("Enter 10 km run time: ")
        if not response:
            print(f"Average of {sum(times)/len(times)}")
            break
        else:
            times.append(int(response))


run_timing()
