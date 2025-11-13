import json
import os
from datetime import datetime

# ==============================================================================
# 1. OOP: Class และ Encapsulation 
# ==============================================================================

class Task:
    """แทนรายการ To-Do List แต่ละรายการ"""
    
    def __init__(self, description, due_date=None, completed=False):
        # Encapsulation: ใช้ _ เพื่อระบุ attributes ภายใน
        self._description = description
        self._due_date = due_date
        self._completed = completed
        
    # Getter methods (แสดง Encapsulation)
    def get_description(self):
        return self._description

    def get_due_date(self):
        return self._due_date

    def is_completed(self):
        return self._completed

    # Setter method
    def mark_completed(self, status=True):
        """ตั้งค่าสถานะการทำเสร็จ"""
        self._completed = status

    def update_description(self, new_desc):
        """อัปเดตคำอธิบายงาน"""
        self._description = new_desc

    def update_due_date(self, new_date):
        """อัปเดตวันครบกำหนด"""
        self._due_date = new_date
        
    def __str__(self):
        """กำหนดรูปแบบการแสดงผลของ object"""
        status = " DONE" if self._completed else " PENDING"
        date_str = f" (Due: {self._due_date})" if self._due_date else ""
        return f"[{status}] {self._description}{date_str}"
        
    def to_dict(self):
        """แปลง Task object เป็น Dictionary สำหรับบันทึกใน JSON"""
        return {
            "description": self._description,
            "due_date": self._due_date,
            "completed": self._completed
        }

    @staticmethod
    def from_dict(data):
        """สร้าง Task object จาก Dictionary ที่โหลดมาจาก JSON"""
        return Task(
            description=data['description'],
            due_date=data['due_date'],
            completed=data['completed']
        )

# ==============================================================================
# 2. File Handling 
# ==============================================================================

FILE_NAME = "tasks.json"

def save_tasks(tasks):
    """บันทึกรายการ Task ลงในไฟล์ JSON"""
    data_to_save = [task.to_dict() for task in tasks]
    try:
        with open(FILE_NAME, 'w', encoding='utf-8') as f:
            json.dump(data_to_save, f, indent=4)
        return True
    except IOError as e:
        print(f" Error saving file: {e}")
        return False

def load_tasks():
    """โหลดรายการ Task จากไฟล์ JSON"""
    if not os.path.exists(FILE_NAME):
        return []
    
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # โครงสร้างข้อมูล: ใช้ List และ Dictionary
            return [Task.from_dict(item) for item in data]
    except (IOError, json.JSONDecodeError) as e:
        print(f" Error loading file or decoding JSON: {e}. Starting with an empty list.")
        return []

# ==============================================================================
# 3. Core Logic Functions 
# ==============================================================================

def add_task(tasks):
    """เพิ่ม Task ใหม่เข้าไปในรายการ"""
    description = input(" Enter task description: ").strip()
    if not description:
        print(" Task description cannot be empty.")
        return
        
    due_date = input("Enter due date (YYYY-MM-DD, optional): ").strip()
    
    # ตรวจสอบรูปแบบวันที่ (Conditionals)
    if due_date:
        try:
            datetime.strptime(due_date, "%Y-%m-%d")
        except ValueError:
            print(" Invalid date format. Task added without a due date.")
            due_date = None
            
    new_task = Task(description, due_date)
    tasks.append(new_task)
    print(f" Task '{description}' added.")
    save_tasks(tasks)

def view_tasks(tasks):
    """แสดงรายการ Task ทั้งหมด"""
    if not tasks:
        print("\n Your To-Do List is empty!")
        return

    print("\n---  Current To-Do List ---")
    # Loops: ใช้ enumerate เพื่อแสดงลำดับ
    for index, task in enumerate(tasks):
        print(f"[{index + 1}] {task}")
    print("----------------------------\n")

def edit_task(tasks):
    """แก้ไขรายการ Task (อัปเดตคำอธิบาย/วันที่/สถานะ)"""
    view_tasks(tasks)
    if not tasks:
        return
        
    # User Interaction และ Conditionals
    try:
        task_num = int(input(" Enter the number of the task to edit: ")) - 1
        if 0 <= task_num < len(tasks):
            task_to_edit = tasks[task_num]
            print(f"\nEditing: {task_to_edit}")
            
            # Sub-menu สำหรับการแก้ไข
            print("What do you want to change?")
            print("1. Description")
            print("2. Due Date")
            print("3. Status (Mark as Done/Pending)")
            
            choice = input(" Enter your choice (1-3): ")
            
            if choice == '1':
                new_desc = input(" Enter new description: ").strip()
                if new_desc:
                    task_to_edit.update_description(new_desc)
                    print(" Description updated.")
            elif choice == '2':
                new_date = input(" Enter new due date (YYYY-MM-DD, optional): ").strip()
                if new_date:
                    try:
                        datetime.strptime(new_date, "%Y-%m-%d")
                        task_to_edit.update_due_date(new_date)
                        print(" Due date updated.")
                    except ValueError:
                        print(" Invalid date format. No changes made.")
            elif choice == '3':
                current_status = task_to_edit.is_completed()
                task_to_edit.mark_completed(not current_status)
                print(f" Task status changed to: {'DONE' if not current_status else 'PENDING'}.")
            else:
                print(" Invalid choice. No changes made.")
                
            save_tasks(tasks)
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Invalid input. Please enter a number.")

def delete_task(tasks):
    """ลบ Task ออกจากรายการ"""
    view_tasks(tasks)
    if not tasks:
        return
    
    try:
        task_num = int(input(" Enter the number of the task to delete: ")) - 1
        if 0 <= task_num < len(tasks):
            deleted_task = tasks.pop(task_num)
            print(f" Task '{deleted_task.get_description()}' deleted.")
            save_tasks(tasks)
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Invalid input. Please enter a number.")
        
# ==============================================================================
# 4. Main Menu and Execution 
# ==============================================================================

def main_menu(tasks):
    """แสดงเมนูหลักและรับการโต้ตอบจากผู้ใช้"""
    
    while True: # Loop หลักของโปรแกรม
        print("\n==========  To-Do List Manager ==========")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Edit/Update Task")
        print("4. Delete Task")
        print("5. Exit and Save")
        print("============================================")
        
        choice = input(" Enter your choice (1-5): ")
        
        # Conditionals
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            edit_task(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            # บันทึกข้อมูลอีกครั้งก่อนออก
            if save_tasks(tasks):
                print("\n All tasks saved. Exiting application. Goodbye!")
                break
            else:
                print("\n Failed to save. Please check the error above.")
        else:
            print(" Invalid choice. Please enter a number between 1 and 5.")

# Entry point ของโปรแกรม
if __name__ == "__main__":
    # โหลดข้อมูลเมื่อเริ่มต้น
    todo_list = load_tasks()
    main_menu(todo_list)
