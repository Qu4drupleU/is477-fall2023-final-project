rule prepare:
    output: "data/winequality-red.csv"
    script: "scripts/prepare_data.py"

rule profile:
    input: "data/winequality-red.csv"
    output: "profiling/report.html"
    script: "scripts/profile.py"

rule analyze:
    input: "data/winequality-red.csv"
    output: 
        "results/wine_quality_histogram.png",
        "results/model_performance.txt",
        "results/summary_statistics.csv"
    script: "scripts/analysis.py"