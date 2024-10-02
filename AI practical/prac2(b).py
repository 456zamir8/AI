# Tower of hanoi problem
from colorama import init, Fore, Style

init(autoreset = True)

def tower_of_hanoi(n, source, destination, auxiliary):
    # Base case: If only one disk, move it directly from source to destination
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return

    # Step 1: Move n-1 disks from source to auxiliary, using destination as auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination)

    # Step 2: Move the nth disk from source to destination
    print(f"Move disk {n} from {source} to {destination}")

    # Step 3: Move the n-1 disks from auxiliary to destination, using source as auxiliary
    tower_of_hanoi(n - 1, auxiliary, destination, source)a

    print(f"destination disk{destination}")

# Driver function to start the process
def solve_tower_of_hanoi():
    print(Fore.GREEN + "\n****TOWER OF HANOI****")
    n = int(input("Enter the number of disks: "))
    print(f"Solving Tower of Hanoi for {n} disks:")
    tower_of_hanoi(n, 'A', 'C', 'B')  # A, B, C are names of rods
    print(Fore.GREEN + "****Succesfully solve the tower of hanoi problem****")
    
solve_tower_of_hanoi()