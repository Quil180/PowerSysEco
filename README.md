Power Systems EconomicsThis repository contains homework assignments, computational simulations, and analytical reports for Power Systems Economics.The project focuses on the economic principles governing power systems, including market equilibrium analysis, supply curve generation, and cost optimization using Python.📂 Repository StructureThe repository is organized by week, containing both the computational logic and the written reports.PowerSysEco/
├── HW/
│   ├── hw_week1/       # Intro to market equilibrium
│   ├── hw_week2/       # Elasticity and demand curves
│   ├── hw_week3/       # Supply curves and unilateral markets
│   ├── ...             # Subsequent weeks (Economic dispatch, etc.)
│   └── hw_week12/      # Final analyses
├── shell.nix           # Nix environment configuration
└── .gitignore
🛠️ Technologies UsedPython: Used for mathematical modeling, solving systems of equations, and data analysis.Libraries: pandas, numpy, sympyLaTeX: Used for typesetting professional reports and mathematical proofs.Nix: Used for reproducible development environment management.🚀 Getting StartedYou can set up the environment using Nix (recommended) or standard Python pip.Option A: Using Nix (Recommended)This repository includes a shell.nix file to ensure a reproducible environment.Ensure you have Nix installed.Navigate to the project root and enter the shell:nix-shell
This will automatically install Python and the required dependencies (pandas, numpy, sympy).Option B: Standard Python SetupIf you are not using Nix, you can install the dependencies manually:pip install pandas numpy sympy
📝 UsageRunning SimulationsTo run the Python analysis for a specific week (e.g., Week 3):cd HW/hw_week3
python hw3.py
Generating ReportsThe reports are written in LaTeX. To compile a PDF (assuming you have a TeX distribution installed):cd HW/hw_week3
pdflatex Awad_Yousef_HW3.tex

