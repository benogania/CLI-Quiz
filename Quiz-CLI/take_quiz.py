from quizcode import run_quiz, load_questions

ethics1 = load_questions('SampleFiles/ethics.txt')
ethics2 = load_questions('SampleFiles/ethics2.txt')
complete = ethics1 + ethics2 #combined quiz items


sample = load_questions('SampleFiles/sample.txt')

run_quiz(sample)

    