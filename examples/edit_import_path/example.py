# https://docs.scipy.org/doc/scipy-1.11.2/tutorial/optimize.html
import sys
from pathlib import Path

import numpy as np
from scipy.optimize import minimize

# Make ./code/utils.py visible to sys.path
sys.path.insert(1, (Path(__file__).parent / "code").as_posix())
from utils import rosen, rosen_der

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
result = minimize(rosen, x0, method="BFGS", jac=rosen_der, options={"disp": True})
optimized_params = result.x
