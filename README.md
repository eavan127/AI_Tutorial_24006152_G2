# AI_Tutorial_24006152_G2

**Author** - Eavan Tan (24006152), Group CS_G2

## Submissions

The five submitted assignments, in the order given by the lab tutor. Each folder holds the report together with the proof (screenshots and figures) and Python files the assignment asks for.

| No. | Week | Lab | Assignment | Folder | Contents |
| :---: | :---: | :---: | --- | --- | --- |
| 1 | 4 | Lab 02 | Lab results: `metrics.csv` and `route_comparison.png` | [Lab02_Assignment](Submissions/Lab02_Assignment) | `metrics_screenshot.png`, `route_comparison_screenshot.png` |
| 2 | 5 | Lab 03 | Assignment 2: questions on BFS, DFS, UCS, GBFS and A* | [Lab03_Assignment](Submissions/Lab03_Assignment) | `Assignment 2_week05` (PDF and Word) |
| 3 | 9 | Lab 07 | Handwriting OCR Evaluation | [Lab07_Assignment](Submissions/Lab07_Assignment) | Report (PDF and Word), `evidence/` with the results table, OCR failures and sample images |
| 4 | 10 | Lab 08 | Logical Reasoning, Semantic Networks and NLP | [Lab08_Assignment](Submissions/Lab08_Assignment) | Report (PDF and Word), `semantic_network.png` |
| 5 | 11 | Lab 09 | Genetic Algorithm for Delivery Route Optimisation | [Lab09_Assignment](Submissions/Lab09_Assignment) | Report (PDF and Word), `ga_delivery_route.py`, `ga_console_output.png` |

## Lab Overview

Code files keep the lecturer's original file names, so the number in a file name can differ from the lab number (for example, Lab 09 runs `lab08_genetic_algorithm_regression.py`). Results are the outputs produced by running each lab.

| Week | Date | Lab | Code | Results | Submission |
| :---: | :---: | --- | --- | --- | --- |
| 4 | 2026/09/30 | Lab 02 - Search Foundations | [lab01_search_foundations.py](all_experiments/lab01_search_foundations.py) | [results/lab01](results/lab01) | [Lab02_Assignment](Submissions/Lab02_Assignment) |
| 5 | 2026/10/08 | Lab 03 - Informed Search | [lab02_informed_search.py](all_experiments/lab02_informed_search.py) | [results/lab02](results/lab02) | [Lab03_Assignment](Submissions/Lab03_Assignment) |
| 6 | 2026/10/14 | Lab 04 - Search Engineering | [lab03_search_engineering.py](all_experiments/lab03_search_engineering.py) | [results/lab03](results/lab03) | - |
| 7 | 2026/10/21 | Lab 05 - Fuzzy Logic and ANFIS | [lab04_fuzzy_anfis.py](all_experiments/lab04_fuzzy_anfis.py) | [results/lab04](results/lab04) | - |
| 8 | 2026/10/28 | Lab 06 - Robotics Sensor Control | [lab05_robotics_sensor_control.py](all_experiments/lab05_robotics_sensor_control.py) | [results/lab05](results/lab05) | - |
| 9 | 2026/11/04 | Lab 07 - Handwriting OCR Evaluation | [lab06_handwriting_ocr_worked.py](all_experiments/lab06_handwriting_ocr_worked.py) | [results/lab06](results/lab06) | [Lab07_Assignment](Submissions/Lab07_Assignment) |
| 10 | 2026/11/11 | Lab 08 - Airline Tweet Sentiment | [lab07_airline_sentiment.py](all_experiments/lab07_airline_sentiment.py) | [results/lab07](results/lab07) | [Lab08_Assignment](Submissions/Lab08_Assignment) |
| 11 | 2026/11/18 | Lab 09 - Genetic Algorithms | [lab08_genetic_algorithm_regression.py](all_experiments/lab08_genetic_algorithm_regression.py) | [results/lab08](results/lab08) | [Lab09_Assignment](Submissions/Lab09_Assignment) |

## Repository Structure

```
AI_Tutorial_24006152_G2/
├── Submissions/        the five submitted assignments with their proof and code
│   ├── Lab02_Assignment/
│   ├── Lab03_Assignment/
│   ├── Lab07_Assignment/
│   ├── Lab08_Assignment/
│   └── Lab09_Assignment/
├── all_experiments/    lab code and the utils/ search package
├── results/            outputs from running each lab
└── all_datasets/       datasets used by the labs
```

## Lab Details

**Lab 02 - Search Foundations.** BFS, DFS and UCS on the OpenFlights airline route graph. Compares route cost, hops and nodes expanded for three airport pairs.
Results: `metrics.csv`, `route_comparison.png`

**Lab 03 - Informed Search.** GBFS, A* and Weighted A* with a Haversine distance heuristic. Checks that the heuristic never overestimates and compares search effort against UCS.
Results: `metrics.csv`, `heuristic_check.csv`, `expanded_nodes.png`

**Lab 04 - Search Engineering.** Packages the search code in `utils/`, runs 8 pytest unit tests, adds a command-line tool (`python -m utils`) and benchmarks four algorithms on ten routes.
Results: `benchmark.csv`, `benchmark_summary.csv`, `benchmark_expansions.png`

**Lab 05 - Fuzzy Logic and ANFIS.** Fuzzy inference and ANFIS on the Air Quality dataset.
Results: `metrics.csv`, `split.csv`, `fuzzy_fixed_points.csv`, `fuzzy_memberships.png`, `fuzzy_control_surface.png`, `predicted_vs_actual.png`, `temperature_humidity.png`

**Lab 06 - Robotics Sensor Control.** Rule-based controller and decision tree on robot sensor readings, with a noise robustness test.
Results: `metrics.csv`, `split.csv`, `feature_scores.csv`, `tree_depth_validation.csv`, `rule_controller.txt`, `rule_per_class.csv`, `noise_robustness.csv`, `noise_robustness.png`, `confusion_matrices.png`

**Lab 07 - Handwriting OCR Evaluation.** Tesseract OCR on 89 handwritten medicine names. Compares raw images with a preprocessing pipeline using exact match, edit distance, CER and blank predictions, then classifies the failures.
Results: `metrics.csv`, `predictions.csv`, `error_analysis.csv`, `sample_grid.png`, `ocr_failures.png`, `preprocessed/`

**Lab 08 - Airline Tweet Sentiment.** Bag-of-words Multinomial Naive Bayes on 14,640 airline tweets with a leakage-safe 70/15/15 split, compared with a majority-class baseline.
Results: `metrics.csv`, `validation_results.csv`, `per_class_metrics.csv`, `per_airline_f1.csv`, `error_analysis.csv`, `test_predictions.csv`, `split.csv`, `confusion_matrix.png`

**Lab 09 - Genetic Algorithms.** A genetic algorithm learns linear regression coefficients for medical insurance charges. Tests reproducibility over ten seeds, compares with ordinary least squares and checks a smaller population size.
Results: `ga_10_runs.csv`, `ga_sensitivity_pop40.csv`, `summary.csv`, `split.csv`, `convergence.png`
