# Max-Profit-Problem

A clean and logical solution to an optimization problem focused on maximizing revenue under time constraints.


## Overview

This project solves the Max Profit Problem, an interview assignment that requires determining the optimal combination of properties to build within a given time limit in order to maximize total earnings.

**The solution focuses on**

Correct interpretation of problem constraints

Sequential construction simulation

Profit optimization logic

## Problem Description

Mr. X owns a large strip of land in Mars Land and can develop it by constructing different types of properties.

| Property        | Symbol | Build Time | Earnings per Time Unit |
| --------------- | ------ | ---------- | ---------------------- |
| Theatre         | T      | 5 units    | $1500                  |
| Pub             | P      | 4 units    | $1000                  |
| Commercial Park | C      | 10 units   | $2000                  |



## Rules & Constraints

Only one property can be built at a time
Construction is sequential, not parallel
A property starts earning immediately after it is completed
Earnings continue for every remaining unit of time
Land availability is unlimited
Goal: maximize total earnings

## Objective

Given an input value n (total available time units):

Determine the best combination of T, P, and C

Ensure total build time ≤ n

Maximize overall earnings


## Solution Strategy

Evaluate all valid combinations of:

Theatres (T)

Pubs (P)

Commercial Parks (C)

Simulate construction step-by-step

Calculate earnings after each building completion

Track and return the combination with maximum profit

**This approach ensures accuracy and alignment with the problem examples.**

## Technologies Used

Programming Language: Python 3

## Concepts Used:

Brute Force Optimization

Simulation

Nested Iteration

Conditional Logic

Tools:

VS Code / Any Python IDE

Command Line / Terminal

Git & GitHub


