[README.md](https://github.com/user-attachments/files/34541512/README.md)
# Python for Engineers and Scientists: companion code

Every program in the book, one folder per chapter (chapter_0 ... chapter_15).
Inside a chapter folder the files are named after where they appear in the book:

- example_N.k_short_title.py    worked examples
- problem_N.k_short_title.py    solved end-of-chapter problems
- lab_short_title.py            the chapter's Engineering Lab
- listing_N.k_short_title.py    the other numbered listings in the text

Files without one of those prefixes are helper modules that the programs import
(for example fluids.py, fem1d.py, cst.py) or data files they read (.csv, .txt, .npy).
They keep the names used in the book, so leave them next to the programs.

## Running a program in Spyder

Open the .py file (File > Open) and press F5. Spyder runs it in its own chapter
folder, so the helper modules and data files beside it are found.

A few programs in Chapter 2 ask you to type values; the book shows the values used.
Example 7.4 has two versions: the one ending in _fixed.py has the corrected line.

Every program was run with Python 3 and the Anaconda libraries (NumPy, SciPy,
Matplotlib, pandas); the printed outputs match the book.
