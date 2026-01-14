Differentiation-of-noisy-data

# Project Title:

Differentiation-of-noisy-data -> Applying Finite Differentiation, Savitzky Golary Filter , Smoothing Splines

# Overview:

This project demonstrates the **numerical differentiation of noisy data** and highlights the problem of **noise amplification** when finite difference methods are applied directly to noisy signals.

To overcome this issue, two smoothing techniques are used:
* Savitzky–Golay filter
* Smoothing spline interpolation

The performance of these methods is compared by computing and visualizing the "first derivative" of the signal.


#  Objective of the Project:

1. To generate a clean analytical signal and its true derivative
2. To contaminate the signal with random noise (simulating real-life data)
3. To compute derivatives using:

   * Direct finite difference
   * Savitzky–Golay smoothing
   * Spline smoothing
4. To compare how smoothing improves derivative accuracy
5. To demonstrate "noise amplification" in numerical differentiation


#  Mathematical Formulas Used:

 (a) Signal Definition

The clean signal is defined as:

[
y(x) = \sin(x) + 0.5 \cos(2x)
]

 (b) Analytical Derivative

The exact derivative is:

[
\frac{dy}{dx} = \cos(x) - \sin(2x)
]

 (c) Finite Difference Approximation

Using central difference (implemented by `np.gradient`):

[
\frac{dy}{dx}\Big|*{x_i} \approx \frac{y*{i+1} - y_{i-1}}{2\Delta x}
]

 (d) Savitzky–Golay Polynomial Fit

A local polynomial of order ( p ) is fitted over a window of length ( W ), and the derivative is computed analytically from the polynomial.

 (e) Smoothing Spline

The spline minimizes:

[
\sum_{i}(y_i - s(x_i))^2 + \lambda \int (s''(x))^2 dx
]

where ( \lambda ) controls smoothness.

---

#  Step Size (Δx):

The step size is computed as:

[
\Delta x = x_{i+1} - x_i
]

From the code:

```python
x = np.linspace(0, 4*np.pi, 200)
dx = x[1] - x[0]
```

This ensures "uniform spacing", which is ideal for finite difference methods.

---

# Error Calculation:

Although not explicitly computed in code, the error can be defined as:

  Absolute Error

[
E_{abs} = | y'*{numerical} - y'*{true} |
]

 Mean Squared Error (MSE)

[
MSE = \frac{1}{N} \sum_{i=1}^{N} (y'*{num,i} - y'*{true,i})^2
]

In practice, the **visual comparison** of curves is used to judge accuracy.

---

#  Code Implementation (Explanation):

 Step-by-step logic:

1. Generate clean signal and true derivative
2. Add Gaussian noise
3. Compute derivative using:

   * Finite difference (`np.gradient`)
   * Savitzky–Golay filter
   * Spline derivative
4. Plot:

   * Raw vs smoothed signal
   * Derivative comparison

Key implementations:

```python
dy_noisy = np.gradient(y_noisy, dx)
dy_savgol = savgol_filter(y_noisy, window_length, poly_order, deriv=1, delta=dx)
dy_spline = spline.derivative()(x)

```

---

#  How to Compile and Run:

 Requirements:

* Python 3.x
* NumPy
* Matplotlib
* SciPy

 Install dependencies:

```bash
pip install numpy matplotlib scipy
```

 Run the code:

python filename.py


# Numerical Results:

* Finite difference on noisy data shows large oscillations
* Savitzky–Golay derivative closely follows the true derivative
* Spline derivative produces a smoother global trend
* Noise amplification is clearly visible in the unsmoothed derivative

---

# Data Description:

| Parameter        | Description                                |
| ---------------- | ------------------------------------------ |
| x                | 200 equally spaced points from 0 to (4\pi) |
| y_clean          | Analytical signal                          |
| y_noisy          | Signal + Gaussian noise                    |
| noise level      | 0.15                                       |
| window length    | 31 (odd)                                   |
| polynomial order | 3                                          |


# Discussion:

* Numerical differentiation is highly sensitive to noise
* Finite difference methods amplify high-frequency noise
* Savitzky–Golay filter preserves **local features**
* Spline smoothing provides **global smoothness**
* Choice of method depends on:

  * Noise level
  * Desired smoothness
  * Importance of local vs global behavior

# Conclusion:

* Direct differentiation of noisy data is unreliable
* Smoothing before differentiation is essential
* Savitzky–Golay filtering is effective for local accuracy
* Spline smoothing is better for overall trend estimation
* Proper preprocessing significantly improves numerical derivatives
