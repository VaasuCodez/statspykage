# [StatsPykage](https://pypi.org/project/StatsPykage/) <a name="top"></a>

[StatsPykage](https://pypi.org/project/StatsPykage/) is an open source Python package for analysing standard statistical distributions: Gaussian, Binomial, Poisson etc. distributions; hosted on [PyPi.org](https://pypi.org/).

Data can be read from .txt files to instances of the distribution models. The package can be used to:

1. Compute the properties of a distribution, such as the mean and standard deviation.
2. Compute a distribution's probability density function for given values and intervals.
3. Plot the distribution and probability density functions visually .

### Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Contribute](#contribute)
* [License](#license)
* [Footer](#footer)

## Installation <a name="installation"></a>

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install StatsPykage.

```bash
pip install statspykage
```

### Dependencies

The package should run with no issues using Python version 3.

To run the package, users also need to have the following packages installed:

- [python-math](https://pypi.org/project/python-math/)
- [matplotlib](https://pypi.org/project/matplotlib/)

## Usage <a name="usage"></a>

```python
import statspykage

# initialize two gaussian distributions
gaussian_one = Gaussian(25, 3)
gaussian_two = Gaussian(30, 2)

# initialize a third gaussian distribution reading in a data file
gaussian_three = Gaussian()
gaussian_three.read_data_file('filepath/filename.txt')
gaussian_three.calculate_mean()
gaussian_three.calculate_stdev()

# print out the mean and standard deviations
print(gaussian_one.mean) # PRINTS: 25
print(gaussian_two.mean) # PRINTS: 30

print(gaussian_one.stdev) # PRINTS: 3
print(gaussian_two.stdev) # PRINTS: 2

print(gaussian_three.mean)
print(gaussian_three.stdev)

# plot histogram of gaussian three
gaussian_three.plot_histogram_pdf()

# add gaussian_one and gaussian_two together
gaussian_one + gaussian_two

```

## Contribute <a name="contribute"></a>

Contributions are welcomed. For major changes, kindly open an issue first to discuss the same before creating a pull request.

## License <a name="license"></a>
[MIT](https://choosealicense.com/licenses/mit/)

## Footer <a name="footer"></a>

Leave a star in the GitHub repository if you found this project helpful!

[(Back to top)](#top)
