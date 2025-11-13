# To-Do List Manager (CLI)

**ผู้พัฒนา:** [ประกรรษวัต/4400090193]

**วันที่:** 13 พฤศจิกายน 2568
---
## 1.  คำอธิบายโปรเจกต์ (Project Description)

โปรเจกต์นี้คือโปรแกรมจัดการรายการ To-Do แบบ Command Line Interface (CLI) ที่พัฒนาด้วยภาษา Python ใช้งานหลักการ **CRUD** 
(Create, Read, Update, Delete) และใช้ **Object-Oriented Programming (OOP)** ในการจัดการข้อมูล Task โดยมีการจัดเก็บข้อมูลแบบถาวร (Persistence) ในรูปแบบไฟล์ JSON

### คุณสมบัติหลัก:
* การจัดการ Task ด้วยคลาส `Task` (มี Attribute: Description, Due Date, Completed Status)
* บันทึกและโหลดข้อมูลอัตโนมัติจากไฟล์ `tasks.json`
* รองรับการเพิ่ม, ดู, แก้ไขสถานะ/คำอธิบาย/วันครบกำหนด, และลบรายการ To-Do
---
## 2. วิธีการรันโปรแกรม (How to Run)
### Prerequisites
* ติดตั้ง Python 3.x
* ติดตั้ง Git
### ขั้นตอนการรัน
1.  **Clone Repository:** ดึงโปรเจกต์จาก GitHub ลงเครื่องของคุณ
    ```bash
    git clone [https://github.com/udonthani-th/To-Do-List-Manager.git](https://github.com/udonthani-th/To-Do-List-Manager.git)
    ```
2.  **เข้าสู่โฟลเดอร์โปรเจกต์:**
    ```bash
    cd To-Do-List-Manager
    ```
3.  **รันโปรแกรม:**
    ```bash
    python todo_app.py
    ```
    *เมื่อโปรแกรมเริ่มต้น จะมีการโหลดข้อมูลจากไฟล์ `tasks.json` (ถ้ามี) และแสดงเมนูหลัก*
---
## 3.  ตัวอย่าง Input/Output 
========== To-Do List Manager ==========

Add Task

View Tasks

Edit/Update Task

Delete Task

Exit and Save ======== Enter your choice (1-5):

เมื่อรันโปรแกรม เมนูหลักจะปรากฏขึ้น:

