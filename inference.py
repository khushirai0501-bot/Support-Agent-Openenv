tasks:
  - name: sentiment_task
    input: "I love this product"
    expected_output: "positive"
    grader: exact_match

  - name: summary_task
    input: "Artificial Intelligence is transforming industries by automating tasks and improving efficiency."
    expected_output: "AI is transforming industries"
    grader: llm

  - name: qa_task
    input: "Who is the CEO of Microsoft?"
    expected_output: "Satya Nadella"
    grader: regex
