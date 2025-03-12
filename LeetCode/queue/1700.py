# 1700. Number of Students Unable to Eat Lunch

# Topics: Array, Stack, Queue, Simulation

# The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively. All students stand in a queue. Each student either prefers square or circular sandwiches. The number of sandwiches in the cafeteria is equal to the number of students. The sandwiches are placed in a stack. At each step:

# If the student at the front of the queue prefers the sandwich on the top of the stack, they will take it and leave the queue.
# Otherwise, they will leave it and go to the queue's end.
# This continues until none of the queue students want to take the top sandwich and are thus unable to eat.

# You are given two integer arrays students and sandwiches where sandwiches[i] is the type of the i​​​​​​th sandwich in the stack (i = 0 is the top of the stack) and students[j] is the preference of the j​​​​​​th student in the initial queue (j = 0 is the front of the queue). Return the number of students that are unable to eat.


# Example 1:

# Input: students = [1,1,0,0], sandwiches = [0,1,0,1]
# Output: 0 
# Explanation:
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,0,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,0,1,1].
# - Front student takes the top sandwich and leaves the line making students = [0,1,1] and sandwiches = [1,0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [1,1,0].
# - Front student takes the top sandwich and leaves the line making students = [1,0] and sandwiches = [0,1].
# - Front student leaves the top sandwich and returns to the end of the line making students = [0,1].
# - Front student takes the top sandwich and leaves the line making students = [1] and sandwiches = [1].
# - Front student takes the top sandwich and leaves the line making students = [] and sandwiches = [].
# Hence all students are able to eat.
# Example 2:

# Input: students = [1,1,1,0,0,1], sandwiches = [1,0,0,0,1,1]
# Output: 3

from collections import deque

def countStudents(students, sandwiches):
    students = deque(students)  # Queue for students
    sandwiches = sandwiches[::-1]  # Stack (reverse list so last element is the top)

    attempts = 0  # Track unsuccessful rotations
    while students:
        if students[0] == sandwiches[-1]:  # Student can eat
            students.popleft()
            sandwiches.pop()
            attempts = 0  # Reset unsuccessful attempts
        else:  # Student can't eat, move to back
            students.append(students.popleft())
            attempts += 1
        
        if attempts == len(students):  # No one can eat the top sandwich at the top of the stack
            break

    return len(students)

# How to Solve (using stack and deque):

# Initialize a stack for the sandwiches and a deque for the students
# Track a variable "attempts": We need to avoid an infinite loop so if we go through the whole students array and no one can eat the sandwich, we need to break
# Loop until either array is empty
    # If the sandwich can be eaten, pop the student and sandwich off the stack and reset attempts
    # If the sandwich can't be eaten, pop the first ele off the students deque and append to the end
    # Check if attempts is equal to the length of the students -> means that we have looped through the whole students arr and no one can eat the sandwich

# Time Complexity:
# - Each student is processed at most once, either by eating or moving to the back of the queue, making it O(N).
# - The while loop runs at most N times, and deque operations (popleft and append) are O(1), keeping the overall complexity O(N).

# Space Complexity:
# - The deque stores at most N students, and the stack holds at most N sandwiches, leading to O(N) space.
# - No extra auxiliary data structures are used beyond these, so the total space remains O(N).


print(countStudents([1,1,0,0], [0,1,0,1]))
print(countStudents([1,1,1,0,0,1], [1,0,0,0,1,1]))