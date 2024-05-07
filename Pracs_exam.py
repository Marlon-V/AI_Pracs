def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return

    # We move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, target, auxiliary)

    # Moving the remaining disk from source to target
    print(f"Move disk {n} from {source} to {target}")

    # Move n-1 disks from auxiliary to target
    tower_of_hanoi(n - 1, auxiliary, source, target)


# Example usage
tower_of_hanoi(3, "A", "B", "C")
