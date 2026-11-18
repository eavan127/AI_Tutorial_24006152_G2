# AI_Tutorial_24006152_G2

**Author** - Eavan Tan (24006152), Group CS_G2

Lab work and assignments for the Artificial Intelligence course. Each lab has its code in `all_experiments/` and the outputs from running it in `results/`. The `Submissions/` folder holds the five submitted assignments, together with the proof (screenshots and figures) and Python files each one asks for.

## Lab Overview

| Date | Lab | Code | Results | Submission |
| :---: | --- | --- | --- | --- |
| 2026/09/30 | Lab 01 - Search Foundations | [lab01_search_foundations.py](all_experiments/lab01_search_foundations.py) | [results/lab01](results/lab01) | - |
| 2026/10/08 | Lab 02 - Informed Search | [lab02_informed_search.py](all_experiments/lab02_informed_search.py) | [results/lab02](results/lab02) | [Lab02_Results](Submissions/Lab02_Results), [Lab02_Assignment](Submissions/Lab02_Assignment) |
| 2026/10/14 | Lab 03 - Search Engineering | [lab03_search_engineering.py](all_experiments/lab03_search_engineering.py) | [results/lab03](results/lab03) | - |
| 2026/10/21 | Lab 04 - Fuzzy Logic and ANFIS | [lab04_fuzzy_anfis.py](all_experiments/lab04_fuzzy_anfis.py) | [results/lab04](results/lab04) | - |
| 2026/10/28 | Lab 05 - Robotics Sensor Control | [lab05_robotics_sensor_control.py](all_experiments/lab05_robotics_sensor_control.py) | [results/lab05](results/lab05) | - |
| 2026/11/04 | Lab 06 - Handwriting OCR Evaluation | [lab06_handwriting_ocr_worked.py](all_experiments/lab06_handwriting_ocr_worked.py) | [results/lab06](results/lab06) | [Lab06_Assignment](Submissions/Lab06_Assignment) |
| 2026/11/11 | Lab 07 - Airline Tweet Sentiment | [lab07_airline_sentiment.py](all_experiments/lab07_airline_sentiment.py) | [results/lab07](results/lab07) | [Assignment_Reasoning_Semantic_NLP](Submissions/Assignment_Reasoning_Semantic_NLP) |
| 2026/11/18 | Lab 08 - Genetic Algorithms | [lab08_genetic_algorithm_regression.py](all_experiments/lab08_genetic_algorithm_regression.py) | [results/lab08](results/lab08) | [GA Assignment](Submissions/GA%20Assignment) |

All submissions are in the [Submissions](Submissions) folder.

## Lab Details

**Lab 01 - Search Foundations.** BFS, DFS and UCS on the OpenFlights airline route graph. Compares route cost, hops and nodes expanded for three airport pairs.
Results: `metrics.csv`, `route_comparison.png`

**Lab 02 - Informed Search.** GBFS, A* and Weighted A* with a Haversine distance heuristic. Checks that the heuristic never overestimates and compares search effort against UCS.
Results: `metrics.csv`, `heuristic_check.csv`, `expanded_nodes.png`

**Lab 03 - Search Engineering.** Packages the search code in `utils/`, runs 8 pytest unit tests, adds a command-line tool (`python -m utils`) and benchmarks four algorithms on ten routes.
Results: `benchmark.csv`, `benchmark_summary.csv`, `benchmark_expansions.png`

**Lab 04 - Fuzzy Logic and ANFIS.** Fuzzy inference and ANFIS on the Air Quality dataset.
Results: `metrics.csv`, `split.csv`, `fuzzy_fixed_points.csv`, `fuzzy_memberships.png`, `fuzzy_control_surface.png`, `predicted_vs_actual.png`, `temperature_humidity.png`

**Lab 05 - Robotics Sensor Control.** Rule-based controller and decision tree on robot sensor readings, with a noise robustness test.
Results: `metrics.csv`, `split.csv`, `feature_scores.csv`, `tree_depth_validation.csv`, `rule_controller.txt`, `rule_per_class.csv`, `noise_robustness.csv`, `noise_robustness.png`, `confusion_matrices.png`

**Lab 06 - Handwriting OCR Evaluation.** Tesseract OCR on 89 handwritten medicine names. Compares raw images with a preprocessing pipeline using exact match, edit distance, CER and blank predictions, then classifies the failures.
Results: `metrics.csv`, `predictions.csv`, `error_analysis.csv`, `sample_grid.png`, `ocr_failures.png`, `preprocessed/`

**Lab 07 - Airline Tweet Sentiment.** Bag-of-words Multinomial Naive Bayes on 14,640 airline tweets with a leakage-safe 70/15/15 split, compared with a majority-class baseline.
Results: `metrics.csv`, `validation_results.csv`, `per_class_metrics.csv`, `per_airline_f1.csv`, `error_analysis.csv`, `test_predictions.csv`, `split.csv`, `confusion_matrix.png`

**Lab 08 - Genetic Algorithms.** A genetic algorithm learns linear regression coefficients for medical insurance charges. Tests reproducibility over ten seeds, compares with ordinary least squares and checks a smaller population size.
Results: `ga_10_runs.csv`, `ga_sensitivity_pop40.csv`, `summary.csv`, `split.csv`, `convergence.png`

## Submissions

Listed in the order given by the lab tutor.

| No. | Submission | Folder | Contents |
| :---: | --- | --- | --- |
| 1 | Assignment for Lab 02: Lab 01 results | [Lab02_Results](Submissions/Lab02_Results) | Screenshots of `metrics.csv` and `route_comparison.png` |
| 2 | Assignment 2: questions on BFS, DFS, UCS, GBFS and A* | [Lab02_Assignment](Submissions/Lab02_Assignment) | `Assignment 2_week05` (PDF and Word) |
| 3 | Handwriting OCR Evaluation | [Lab06_Assignment](Submissions/Lab06_Assignment) | Report (PDF and Word), `evidence/` with the results table, OCR failures and sample images |
| 4 | Logical Reasoning, Semantic Networks and NLP | [Assignment_Reasoning_Semantic_NLP](Submissions/Assignment_Reasoning_Semantic_NLP) | Report (PDF and Word), `semantic_network.png` |
| 5 | Genetic Algorithm for Delivery Route Optimisation | [GA Assignment](Submissions/GA%20Assignment) | Report (PDF and Word), `ga_delivery_route.py`, `ga_console_output.png` |

## Repository Structure

```
AI_Tutorial_24006152_G2/
├── all_datasets/       datasets used by the labs
├── all_experiments/    lab code (lab01 to lab08) and the utils/ search package
├── results/            outputs generated by each lab (lab01 to lab08)
└── Submissions/        completed assignments
    ├── Lab02_Results/
    ├── Lab02_Assignment/
    ├── Lab06_Assignment/
    ├── Assignment_Reasoning_Semantic_NLP/
    └── GA Assignment/
```
