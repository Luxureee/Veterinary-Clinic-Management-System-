
**Data Structures Final Project** *Term 3 | A.Y. 2025 - 2026*

---

## 📋 Project Overview
The **Veterinary Clinic Management System** is a menu-driven Python application designed to simulate a real-world clinic workflow. It manages pet registration, tracks medical consultation priorities, handles emergency operations, and features a step-by-step history undo mechanism. 

The core system architecture relies strictly on custom data structure implementations (Linked Lists, Queues, and Stacks) to ensure optimal memory management and algorithmic efficiency without relying on built-in high-level Python collections.

---

## 🛠️ System Architecture & Data Structures

### 1. Pet Record Node
Every registered pet is stored dynamically as an individual element containing the following structural fields:
* **Pet ID** (Unique Identifier)
* **Pet Name**
* **Breed**
* **Owner Name**
* **Condition Severity (1–5)**:
  * `1` = Most Severe / Emergency Case
  * `2` = Urgent Case
  * `3` = Moderate / Semi-Urgent Case
  * `4` = Non-Urgent / Minor Case
  * `5` = Least Severe / Routine Check-up

### 2. Custom Data Structures Used
* **Linked List & Priority Queue:** Used to build the consultation queue where nodes are inserted dynamically based on their severity index. 
* **Stack:** Used to preserve system states for undoing previous registration or scheduling operations.

---

## 👥 Group Members & Code Distribution

Each system module has been strictly modularized and implemented by its respective owner:

### 👤 Mirador — Priority Consultation Queue
* **Module:** `PriorityConsultationQueue.register_pet()`
* **Logic:** * Schedules incoming animals dynamically based on their severity score.
  * Ensures **Lower severity number = Higher priority** (e.g., Level 2 gets served before Level 3).
  * Implements **Stable Sorting (FIFO for ties)**: Pets arriving with identical severity metrics are sorted strictly by their chronological order of arrival.

### 👤 Mercado — Emergency Cases Jump Queue
* **Module:** `Emergency Interception / Boundary Alerts`
* **Logic:** * Intercepts standard insertion patterns. Whenever a pet with a **Severity Level 1** is registered, they instantly bypass standard positions and jump to the absolute front (`head`) of the queue.
  * Dispatches real-time, high-visibility warning notifications to the terminal interface upon arrival.

### 👤 Marcelo — Serve Next Animal
* **Module:** `PriorityConsultationQueue.serve_next_animal()`
* **Logic:** * Extracts and treats the highest priority animal waiting at the head of the queue.
  * Formats and prints comprehensive data profiles of the pet being handled.
  * Includes programmatic exceptions to cleanly handle boundary anomalies (e.g., attempting to serve an empty consultation room).
  * Hooks into the undo stack tracking system to log transactions before finalizing pointer alterations.

### 👤 Adalim — Undo Last Registration
* **Module:** `RegistrationUndoStack`
* **Logic:** * Employs a custom stack array architecture to pop the most recent structural state.
  * Allows operators to roll back mistaken registrations or service commands, seamlessly extracting the reference nodes out of the queue and restoring past arrangements.

### 👤 Legaspi — Register New Pet
* **Module:** `System Menu & Input Intake`
* **Logic:** * Coordinates input validation loops to guarantee type safety (e.g., verifying severity bounds are strictly $1 \le x \le 5$).
  * Handles standard data collection fields, initializes new `PetNode` instances, and interfaces with the registration pipeline.

---

## 🛡️ Modular Operations & Error Handling
The system features dedicated functions designed around the project guidelines:
1. **Insert:** Dynamically creates and adds data entries securely into memory.
2. **Delete:** Shifts pointer targets to safely isolate and strip elements out of active queues.
3. **Display:** Traverses active structures from head to tail to reveal waiting line metrics.
4. **Search / Update:** Locates active data blocks to alter properties or verify record values.

### Boundary Constraints Covered:
* **Empty States:** Active notifications block users from serving or deleting data if head pointers point to `None`.
* **Input Scrubber:** Prevents program crashes when processing mismatched alphanumeric terminal arguments.
* **Overflow Protection:** Handled via programmatic list mutations rather than static structural caps.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.8 or higher installed.

### How to Run
1. Clone this repository onto your desktop:
