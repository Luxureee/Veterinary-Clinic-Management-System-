class PetNode:
    """Represents a single pet record stored as a node."""

    def __init__(self, pet_id, name, breed, owner, severity):
        self.pet_id = pet_id
        self.name = name
        self.breed = breed
        self.owner = owner
        self.severity = int(severity)  # 1 (Critical/Emergency) to 5 (Least Severe)
        self.next = None

    def display_details(self):
        """Helper to print pet details cleanly when served."""
        print(f"--- Animal Being Served ---")
        print(f"Pet ID:            {self.pet_id}")
        print(f"Pet Name:          {self.name}")
        print(f"Breed:             {self.breed}")
        print(f"Owner Name:        {self.owner}")
        print(f"Severity Level:    {self.severity} " +
              ("(EMERGENCY CASE!)" if self.severity == 1 else ""))
        print(f"---------------------------")


class PriorityConsultationQueue:
    """Linked-list based Priority Queue representing the clinic workflow."""

    def __init__(self):
        self.head = None
        self.tail = None  # Keeps track of the end for general cases

    def is_empty(self):
        return self.head is None

    def register_pet(self, pet_node):
        """
        Inserts pet based on severity level priority.
        - Severity 1 (Emergency) jumps to the absolute front.
        - Severities 2-5 are placed in priority order, preserving arrival order for ties.
        """
        # Case 1: Queue is empty
        if self.is_empty():
            self.head = pet_node
            self.tail = pet_node
            if pet_node.severity == 1:
                print("\n[WARNING] Emergency case registered! Placed at the front.")
            return

        # Case 2: Emergency Jump Queue (Severity 1)
        if pet_node.severity == 1:
            print("\n[WARNING] Emergency case registered! Jumping to the front of the queue.")
            pet_node.next = self.head
            self.head = pet_node
            return

        # Case 3: Priority Insertion for levels 2-5
        # If the new pet has higher priority (lower number) than the head node
        if pet_node.severity < self.head.severity:
            pet_node.next = self.head
            self.head = pet_node
            return

        # Traverse to find the correct spot (maintaining FIFO order for identical severities)
        current = self.head
        while current.next is not None and current.next.severity <= pet_node.severity:
            current = current.next

        # Insert node
        pet_node.next = current.next
        current.next = pet_node
        if pet_node.next is None:
            self.tail = pet_node

    def serve_next_animal(self, undo_stack):
        """
        Removes and returns the next pet to be treated.
        Pushes the action/pet info onto the history stack to support undo mechanisms.
        """
        # ERROR HANDLING: Handle empty queue condition safely
        if self.is_empty():
            print("\n[ERROR] Boundary Condition Met: Cannot serve. The consultation queue is completely empty.")
            return None

        # Dequeue operation (Remove from front)
        served_pet = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None  # Queue became empty

        # Display details of the pet being served
        print("\n[SYSTEM ACTION] Serving next animal...")
        served_pet.display_details()

        # STACK-BASED INTEGRATION:
        # Push to undo stack tracking system. We log that this pet was "SERVED"
        # so an undo system can revert them back to the queue if needed.
        undo_stack.push({"action": "SERVE", "pet": served_pet})

        return served_pet


class RegistrationUndoStack:
    """Stack structure tracking actions to handle the undo last registration/service requirements."""

    def __init__(self):
        self.stack = []  # Python list acting as a dynamic stack

    def push(self, action_data):
        self.stack.append(action_data)

    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()