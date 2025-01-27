# Thoughtful.AI Interview Submission
This project contains the functionality to determine which stacks to deliver packages to using Thoughtful's robotic arms. 

The potential stacks are:
- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.

A package is deemed bulky if any of its dimensions are greater or equal to 150cm or if the volume is greater than 1,000,000cm<sup>3</sup>

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Installation
1. Clone the repository:
```bash
 git clone https://github.com/MikeKumi/thoughtful_ai.git
```

## Usage
This repository provides a collection of utility functions that you can import into your project. These functions are designed to be used as building blocks within your code, not executed independently.

## Contributing
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`.
3. Make your changes.
4. Push your branch: `git push origin feature-name`.
5. Create a pull request.

P.S. I won't actually be accepting PRs
