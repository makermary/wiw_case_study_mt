# Mary's Code Challenge
Welcome to my results for the *When I Work code challenge*.

To execute the pipeline, open a terminal window on your local machine, and follow these steps.

### Step 1: Requirements

This pipeline script is executed via the terminal on your local machine using `git` and `python3`.
You will also need the `pandas` module (version 1.3.0 or higher). In the terminal, enter
```
pip show pandas
```
to check if you have the module installed. If you need to install the module, or upgrade your version, enter the following in your terminal (optionally specifying exactly what version you want to install).
```
pip install pandas
```

### Step 2: Clone the repo
In your terminal, navigate to the local directory where you want to save the repository. Then, you'll pull a local version using git:
```
git clone https://github.com/makermary/wiw_case_study_mt.git
```

### Step 3: Run the pipeline script
With the repository saved locally, you're ready to run the pipeline. In your terminal, you'll use `python3` to run the script:
```
python3 web_traffic_agg.py
```
The script will output the result file in your present working directory (the repo). Open and inspect the results!

### Developer notes
Following the challenge document, I committed to keeping the code functional and efficient. To deploy to production, I would use docker to create a python container where the script can be executed.

I used verbose naming conventions to help the reviewer understand the execution path and functionality. In production, I would prefer to define a function with generic naming convention. This would make the pipeline repeatable, using arguments for variables in the pipeline setup such as `URL`, `filename`, `agg_type`, etc. 

I opted not to fill `NaN` values with zero because it could imply a page visit less than 1s (depending on rounding method) even though there was no page visit record in the raw data.


## Where should we go next?
### Data cleanliness
The input data provided for this challenge was clean and clear. If we were not certain about the quality of input data, we could add:
- Tests to check if the columns are in the same order in every file, and logic to correct the order if necessary.
- Tests for null values in columns required for the analysis, and logic to exclude nulls if necessary
- Logging at various stages of the script in case the path, filenames, or filetype change, or the column names change.

### Analysis
The result shows us each user's total path visit length; with more context, we could explore:
1. Does the path visited or the time spent there influence conversion? Time to convert? Churn? (Assuming we have a bridge between these user IDs and the product)
2. Should we look into subpaths? Are the feature pages *in general* engaging and keeping attention?
3. Cross-referencing the `drop` field, is there a particular path where we lose users? Within the tutorial subpath, is there a step where we consistently lose users?

### Experimentation
There are plenty of options for things we could test on the webpage by collecting this data over time. Depending on our goals, we could hypothesize:
1. Users who drop in the middle of a tutorial will likely not convert. We should provide targeted marketing to those users (if we have their contact information) or refine the tutorial based on our ICP and product strategy.
2. Users who spend a lot of time on the features page show strong intent. We should test whether adding a trial call to action influences capturing user intent. We can also add the product console or trial paths to this data to see if there's less drop from features pages after adding the CTAs.
3. Users on mobile are more likely to drop and less likely to convert from tutorials pages. We should test different CTAs or content on tutorials pages depending on if the user agent is a mobile or desktop version.