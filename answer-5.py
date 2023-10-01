def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print("Move disk 1 from", source, "to", destination)
        return

    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print("Move disk", n, "from", source, "to", destination)
    tower_of_hanoi(n - 1, auxiliary, source, destination)


num_disks = int(input("Enter the number of disks: "))
source_peg = input("Enter the source peg (A, B, C, ...): ")
auxiliary_peg = input("Enter the auxiliary peg (A, B, C, ...): ")
destination_peg = input("Enter the destination peg (A, B, C, ...): ")


print("Steps to solve Tower of Hanoi:")
tower_of_hanoi(num_disks, source_peg, auxiliary_peg, destination_peg)
