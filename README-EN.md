This project is a parser that processes tables containing lists of applicants who have submitted documents and sorts them by universities or merges them into a single file.

Project Installation:
1) Install the VS Code development environment (https://code.visualstudio.com/Download).
2) Open VS Code, click on "Extensions" on the left, search for "Python" in the search bar, select the Microsoft extension (marked with a checkmark), and click "Install."
3) Open the project page on GitHub (https://github.com/trydov1k/test), click the green "Code" button, and select "Download ZIP" from the dropdown menu.
4) Extract the ZIP file to any convenient location, such as the desktop (you can use WinRAR for extraction: https://www.rarlab.com/download.htm).
5) Installation is complete.

Running the Program:
1) Right-click the extracted folder and select "Open with VS Code.
2) In VS Code, run the main.py file (select main.py on the left, then click the triangle icon in the top-right corner).
3) A terminal will open, prompting you to answer a series of questions.

Features and Configuration:
- Change the folder containing tables? (1/0): You can modify the folder from which the program reads files. If you keep the default folder, add your files to the tables folder.
- Remove applicants listed after you? (1/0): If you select 1, the program will remove all applicants listed after you, except for the five following you. You will then need to enter your participant ID (found on the government services website). If you select 0, the program will include all applicants in the final file.
- Distribute programs by universities? (1/0): If you select 0, the program will create a single output file containing all programs. If you select 1, you can specify which program belongs to which university (the program name is the table filename without the date).
- To change settings, navigate to the apps folder and run the changesettings.py file.

Example Usage:
1) Download the tables of applicants from the government services website.
2) Move these tables to the folder you intend to use (if you don’t change the folder, add the files to the tables folder).
3) Run the program.
4) I want to change the folder, so when asked: Change the folder containing tables? (1/0), I enter 1.
5) I enter the path to the folder containing the tables—in my case: C:\Users\trydov1k\OneDrive\Desktop\Списки поступающих.
6) When asked: Remove applicants listed after you? (1/0), I enter 1.
7) I enter my participant ID.
8) I want to distribute programs by universities, so when asked: Distribute programs by universities? (1/0), I enter 1.
9) I enter the number of universities—in my case, 4.
10) I enter the names of the universities, each on a new line.
11) I enter the number of programs (number of tables) for each university and then input the program names (the program name = filename without the date, e.g., Программное_обеспечение_компьютерных_систем_и_сетей_Сетевые_информационные_технологии).
12) After entering the last program, the program generates the final files in the readytables folder.
13) Open the readytables folder (right-click and select "Open in File Explorer").
14) Enjoy the sorted files organized by university!

This text was translated by the neural network, so there may be inaccuracies.
