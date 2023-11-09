# K-Means Clustering Visualization Tool

## Overview

This interactive tool allows users to explore the K-means clustering algorithm visually. Users can set the number of clusters (K), place points on the panel, and apply the algorithm. The clusters are represented by colored circles, and points are assigned colors based on their cluster memberships. The tool provides a dynamic way to understand and experiment with K-means clustering.

## Table of Contents

- [Getting Started](#getting-started)
- [Interface Overview](#interface-overview)
- [Interacting with the Panel](#interacting-with-the-panel)
- [Understanding the Display](#understanding-the-display)
- [Error Calculation](#error-calculation)
- [Closing the Program](#closing-the-program)
- [Tips](#tips)

## Getting Started

1. Ensure you have Python and Pygame installed on your system.
2. Run the program by executing the script (e.g., `python kmeans_visualization.py`).

## Interface Overview

- Use the '+' and '-' buttons to adjust the number of clusters (K).
- The 'Run' button applies the K-means algorithm to cluster the points.
- 'Random' button randomly places initial cluster points.
- 'Algorithm' button applies K-means using scikit-learn.
- 'Reset' button clears all points and clusters.

## Interacting with the Panel

- Click on the panel to place points. The mouse coordinates will be displayed.
- Hover over the panel to see the current mouse position.

## Understanding the Display

- Clusters are represented by colored circles.
- Points are displayed as small black circles.
- The color of points corresponds to their assigned cluster.

## Error Calculation

- The 'Error' value represents the sum of distances from points to their assigned clusters.
- The lower the error, the better the clustering.

## Closing the Program

- Click the 'X' button or press 'Quit' to exit the program.

## Tips

- Experiment with different values of K for varied clustering results.
- Use 'Random' to initialize random clusters or 'Algorithm' for automated clustering.
- 'Reset' clears all points and clusters, allowing you to start anew.

Enjoy exploring K-means clustering with this interactive visualization tool!
