Getting Started
You will **fork this repository**, open it in **GitHub Codespaces**, and run the tool to explore how it works.

---

Steps to Work on This Project

1️⃣ Fork This Repository
Before making any changes, you need to create your own copy of the project:
1. Click the **Fork** button (top right corner of this page).
2. This creates a copy in your **GitHub account**.

2️⃣ Open in GitHub Codespaces
You can edit and run the code without installing anything on your computer:
1. Go to your forked repository.
2. Click the **"Code"** button.
3. Select the **"Codespaces"** tab.
4. Click **"Create Codespace on Main"** (this will launch an online coding environment).

3️⃣ Run the File Replication Tool
Once your Codespace is ready:
1. Open the terminal in GitHub Codespaces.
2. Run the following command to start the script:
   ```sh
   python file_replication_tool/replication_tool.py
   ```
3. Follow the on-screen instructions to test file replication.

---

🔄 Editing and Experimenting
You are encouraged to explore and modify the code **without affecting the original project**.
- **Modify only in your forked repository**.
- **Do not push changes to the main repository**.

To save changes:
```sh
git add .
git commit -m "My updates"
git push origin main
```

---

Troubleshooting
If you face issues:
- Check if all required libraries are installed:
  ```sh
  pip install -r requirements.txt
  ```
- If `tkinter` errors appear, try running the script without the GUI:
  ```sh
  python file_replication_tool/replication_tool.py --nogui
  ```
- For additional help, refer to the **Issues** section or ask your instructor.

---

 Submitting Your Work
1. Make sure all changes are committed and pushed to **your forked repository**.
2. Share the **GitHub link of your fork** with your instructor.


