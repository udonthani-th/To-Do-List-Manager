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

Git เป็นเครื่องมือสำคัญที่ใช้ในการ ควบคุมเวอร์ชัน (Version Control System) สำหรับโปรเจกต์ To-Do List Manager
ช่วยให้คุณสามารถติดตาม, บันทึก, และจัดการการเปลี่ยนแปลงโค้ดทั้งหมดได้อย่างเป็นระบบ

นี่คือคำสั่งและแนวคิดหลักของ Git ที่คุณใช้ในโปรเจกต์นี้:
1. แนวคิดความหมายในโปรเจกต์
Repository (Local)	โฟลเดอร์ todo-list-manager ในเครื่อง ที่เก็บโค้ดและประวัติ Git
Repository (Remote)	พื้นที่เก็บโค้ดบน GitHub (udonthani-th/To-Do-List-Manager.git) ที่ใช้สำหรับการสำรองและส่งมอบงาน Commit
การ บันทึก การเปลี่ยนแปลงของไฟล์ (เช่น การเพิ่มฟังก์ชัน edit_task หรือการแก้ไข tasks.json)
Branch (main)เส้นทางการพัฒนาหลักของโค้ด ที่เก็บโค้ดเวอร์ชันล่าสุดที่พร้อมใช้งาน

2. คำสั่งหลักที่ใช้ในการทำงานคำสั่งหน้าที่ในโปรเจกต์ตัวอย่างการใช้งาน git status ตรวจสอบสถานะ ของไฟล์ที่ถูกแก้ไข, ถูกเพิ่ม, หรือมี 
ConflictMinibo@Mini MINGW64 ~/todo-list-manager (main)git add <file>นำไฟล์ ที่ถูกแก้ไข 
(เช่น todo_app.py, tasks.json) เข้าสู่ Staging Areagit add tasks.jsongit commit -m "Msg"บันทึก 
การเปลี่ยนแปลงที่อยู่ใน Staging Area เข้าสู่ประวัติ Gitgit commit -m "FEAT: Implement delete_task"git push origin main
ส่ง Commit ที่บันทึกไว้ในเครื่อง (Local) ขึ้นไปยัง GitHubgit push origin maingit pull origin mainดึง Commit ล่าสุดจาก GitHub
ลงมาในเครื่องของคุณ (Local)git pull origin main

3. การจัดการปัญหา (Merge Conflict)
ในระหว่างการทำงานกับโปรเจกต์นี้ คุณได้พบและแก้ไขปัญหา Merge Conflict ซึ่งเป็นทักษะสำคัญที่ Git ใช้ในการผสานการเปลี่ยนแปลง:
ปัญหา: เมื่อคุณแก้ไขโค้ดทั้งในเครื่อง (Local) และบน GitHub (Remote) ทำให้ประวัติการ Commit แยกออกจากกัน (Diverged)

การแก้ไข:
Git ปฏิเสธการ Push และแนะนำให้ทำ git pull ก่อน
รัน git pull origin main เพื่อดึง Commit ใหม่ลงมา
เมื่อเกิด Conflict (แสดงสถานะ MERGING และแจ้งไฟล์เช่น todo_app.py) คุณต้อง เปิดไฟล์
ลบ Conflict Markers (<<<<<<<, =======, >>>>>>>) และเลือก/รวมโค้ดที่ถูกต้อง
รัน git add . และ git commit เพื่อ จบการ Merge และสร้าง Merge Commit ใหม่ เพื่อรวมประวัติทั้งสองฝั่งเข้าด้วยกัน