# YAMR (Yet Another MapReduce)

## Overview

This project demonstrates the MapReduce concept using a simple example to count frequency of characters present in a file. It involves splitting a large file into partitions, creating worker nodes for parallel processing, applying a mapper function to each partition, and finally reducing the results to get the output.

## Getting Started

Follow these steps to set up and run the project on your local machine.

### Prerequisites

- Python 3.x installed.
- Make utility (usually pre-installed on Unix-like systems).

### Installation

1. Clone the repository to your local machine:

 ```bash
git clone [URL-of-the-repository]
```
2.Navigate to the project directory (root folder)

### Usage
The project consists of several steps, each executed using the make utility. Here's how to use it:

**Step 1: Write Data**
To split a large file into partitions, run the following command:

```bash
make write
```
You'll be prompted to enter the number of partitions and the path to the file you want to split.

**Step 2: Create Worker Nodes**

To create worker nodes for parallel processing, run the following command:

```bash
make worker_nodes
```
This will start the server and client processes.

**Step 3: Read Data**

To verify that the data is correctly distributed among worker nodes, run:

```bash
make read
```
**Step 4: Apply Mapper**

To apply the mapper function to each partition, use the following command:

```bash
make map
```
You'll be prompted to enter the number of partitions.

**Step 5: Integrate Mapper Output**

To integrate the mapper output, run:

```bash
make shuffle
```
This will create a merged file with the results.

**Step 6: Shuffling and Reducing**

To perform shuffling and reducing, execute:

```bash
make reduce
```
This will generate the final output.
