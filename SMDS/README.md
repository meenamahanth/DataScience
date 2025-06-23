<h1 align='center'> Statistical Methods for Data Science in Python </h1>

## 📈 Linear Regression

### 1. `least_sqr_linearreg.py`

**Model:**
$y = a + bx + cx^2$

**Normal Equations:**
$\sum y = na + b\sum x + c\sum x^2$
$\sum xy = a\sum x + b\sum x^2 + c\sum x^3$
$\sum x^2y = a\sum x^2 + b\sum x^3 + c\sum x^4$

### 2. `linear_reg.py`

#### (a) Linear Regression (y on x)

**Model:**
$y = a + bx$

**Normal Equations:**
$\sum y = na + b\sum x$
$\sum xy = a\sum x + b\sum x^2$

#### (b) Linear Regression (x on y)

**Model:**
$x = a + by$

**Normal Equations:**
$\sum x = na + b\sum y$
$\sum xy = a\sum y + b\sum y^2$

---

## 📉 Nonlinear Regression

### 3. `nonlinear_first_curve.py`

**Model:**
$y = ae^{bx}$

**Linearized Form:**
$\ln y = \ln a + bx$

**Normal Equations:**
$\sum \ln y = n \ln a + b\sum x$
$\sum x \ln y = \ln a\sum x + b\sum x^2$

### 4. `nonlinear_second_curve.py`

**Model:**
$y = ab^x$

**Linearized Form:**
$\ln y = \ln a + x \ln b$

**Normal Equations:**
$\sum \ln y = n \ln a + \ln b \sum x$
$\sum x \ln y = \ln a\sum x + \ln b\sum x^2$

### 5. `power_curve.py`

**Model:**
$y = ax^b$

**Linearized Form:**
$\ln y = \ln a + b \ln x$

**Normal Equations:**
$\sum \ln y = n \ln a + b\sum \ln x$
$\sum \ln x \ln y = \ln a\sum \ln x + b\sum (\ln x)^2$

---

## 🧪 Hypothesis Testing

### 6. `t-pairedtest.py`

**Paired t-test Formula:**
$t = \frac{\bar{d}}{s / \sqrt{n}}$

Where:

* $\bar{d} = \frac{\sum d_i}{n}$: Mean of differences
* $s = \sqrt{\frac{\sum (d_i - \bar{d})^2}{n - 1}}$: Standard deviation of differences
* $n$: Number of paired observations

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/meenamahanth/SMDS.git
cd SMDS
```

### 2. Set Up Python Environment

Ensure Python 3 is installed:

```bash
python --version
```

(Optional) Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install sympy
```

### 4. Run the Script

```bash
python script_name.py
```

Replace `script_name.py` with the actual file name that you want to execute.

---

## 📦 Requirements

* Python 3.x
* `math` (built-in)
* `sympy`

Install required libraries using:

```bash
pip install sympy
```

---
