# HW1
 DSAN 5900 - Homework 1
 
 Group #1: Alivia Castor & Isfar Baset

# 📘 DSAN 5900 Homework 1 Website  

This repository is hosted using **GitHub Pages**, allowing us to view the project’s website online.  

---

## 🔗 How to Access the Webpage  
For now, you can view the website here:  
📌 **[https://isfarbaset.github.io/DSAN-5900-Homework-1/](https://isfarbaset.github.io/DSAN-5900-Homework-1/)**  

**Note:** This is just a placeholder URL from a forked version of the repository. Once we finalize the setup on our shared repository, we can update this link with the correct one.  

---

## 🚀 How GitHub Pages Works  
1. The website is **automatically generated** from Quarto files (`.qmd` in `website-source/`).
2. When rendered, the output is placed in the `docs/` folder.
3. GitHub Pages is configured to serve the website **from the `docs/` directory**.
4. Every time changes are pushed, GitHub Pages updates the live site.

---

## 🔄 Updating the Website  
To make updates:  
1. Modify the `.qmd` files in `website-source/`.  
2. Run:
   ```sh
   quarto render
   ```
   This updates the `docs/` folder.  
3. Commit and push the changes:
   ```sh
   git add .
   git commit -m "Updated website content"
   git push
   ```
4. The changes will appear on **GitHub Pages** within a few minutes.  

---

## 📂 Repository Structure  
- `website-source/` → Contains the **Quarto source files** (`.qmd`).  
- `docs/` → The **rendered website** (this is what GitHub Pages serves).  
- `code/` & `data/` → Supporting files for analysis.  

---