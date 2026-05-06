# Electric Field and Equipotential Lines Simulation

This repository contains the theoretical and experimental visualization of electric fields and equipotential lines using Python.

The project was developed as part of a physics laboratory analysis involving electric potential measurements and graphical representation of equipotential regions.

## Contents

### Theory and Simulation
The following scripts simulate electric fields and equipotential lines theoretically:

- `teory.py`  
  Simulation of electric field and equipotential lines.

- `cleanTeory.py`  
  Cleaner and simplified visualization of the theoretical model.

## Experimental Visualization

The following scripts focus on plotting experimentally measured equipotential lines:

- `line.py`  
  Basic plotting of equipotential lines from measured data.

- `continue.py`  
  Continuous interpolation and contour visualization of the measured equipotential lines.

## Features

- Electric field visualization
- Equipotential line plotting
- Experimental data interpolation
- Contour map generation
- Comparison between theoretical and experimental behavior

## Technologies Used

- Python 3
- NumPy
- Matplotlib
- Pandas
- SciPy

## Installation

Clone the repository:

```bash
git clone https://github.com/marquistallman/LineasEquipotenciales.git
cd LineasEquipotenciales
```

Install dependencies:

```bash
pip install numpy matplotlib pandas scipy
```

## Usage

Run any script individually:

```bash
python teory.py
```

or

```bash
python continue.py
```

## Objective

The main purpose of this project is to analyze the behavior of electric potential distributions and compare theoretical predictions with experimental measurements obtained in laboratory conditions.

## License

This project is licensed under the MIT License.
