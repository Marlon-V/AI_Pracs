from collections import deque

class State:
    def __init__(self, disks, source, target, auxiliary, steps):
        self.disks = disks
        self.source = source
        self.target = target
        self.auxiliary = auxiliary
        self.steps = steps

def tower_of_hanoi_bfs(num_disks, source, target, auxiliary):
    initial_state = State(list(range(1, num_disks + 1)), source, target, auxiliary, [])
    queue = deque([initial_state])

    while queue:
        current_state = queue.popleft()
        if not current_state.disks:
            print("Steps to solve the Tower of Hanoi problem:")
            for step in current_state.steps:
                print(step)
            return

        disk = current_state.disks[0]
        if len(current_state.disks) > 1:
            queue.append(State(current_state.disks[1:], current_state.auxiliary, current_state.target, current_state.source, current_state.steps + [f"Move disk {disk} from {current_state.source} to {current_state.auxiliary}"]))
            queue.append(State(current_state.disks[1:], current_state.source, current_state.auxiliary, current_state.target, current_state.steps + [f"Move disk {disk} from {current_state.source} to {current_state.target}"]))
            queue.append(State(current_state.disks[1:], current_state.source, current_state.target, current_state.auxiliary, current_state.steps + [f"Move disk {disk} from {current_state.auxiliary} to {current_state.target}"]))
        else:
            queue.append(State([], current_state.source, current_state.target, current_state.auxiliary, current_state.steps + [f"Move disk {disk} from {current_state.source} to {current_state.target}"]))

if __name__ == "__main__":
    num_disks = 3
    tower_of_hanoi_bfs(num_disks, "A", "C", "B")
