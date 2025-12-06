import random
from colorama import Fore, Style, init

init(autoreset=True)

TAG_ENUM_RANDOM = '[enum:random]'
TAG_ENUM_SEQUENCE = '[enum:sequence]'
TAG_ENUM_GENERIC = '[enum]'

def style_blue(text):
    return f"{Fore.BLUE}{text}{Style.RESET_ALL}"

def style_highlight(text):
    return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"

def style_green(text):
    return f"{Fore.GREEN}{str(text)}{Style.RESET_ALL}"

def style_cyan(text):
    return f"{Fore.CYAN}{text}{Style.RESET_ALL}"

def style_error(text):
    return f"{Fore.RED}{text}{Style.RESET_ALL}"

def apply_text_highlighting(text):
    if "[" in text and "]" in text:
        try:
            start = text.index("[")
            end = text.index("]")
            full_tag = text[start : end + 1]
            content = text[start + 1 : end]
            return text.replace(full_tag, style_highlight(content))
        except ValueError:
            return text
    return text

def parse_question_entry(entry):
    answer, question_text = entry.split(' - ', 1)
    
    is_enum = False
    enum_mode = 'sequence'

    if TAG_ENUM_RANDOM in question_text:
        is_enum = True
        enum_mode = 'random'
        question_text = question_text.replace(TAG_ENUM_RANDOM, '')
    elif TAG_ENUM_SEQUENCE in question_text:
        is_enum = True
        enum_mode = 'sequence'
        question_text = question_text.replace(TAG_ENUM_SEQUENCE, '')
    elif TAG_ENUM_GENERIC in question_text:
        is_enum = True
        question_text = question_text.replace(TAG_ENUM_GENERIC, '')

    question_text = apply_text_highlighting(question_text)

    return {
        "answer": answer.strip(),
        "question": question_text.strip(),
        "is_enum": is_enum,
        "enum_mode": enum_mode
    }

def load_questions(path):
    questions = []
    invalid_lines = []

    try:
        with open(path, 'r', encoding='utf8') as file:
            content = file.read().strip()
    except FileNotFoundError:
        print(style_error(f"Error: File not found at {path}"))
        return []

    entries = content.split('\n\n')

    for idx, entry in enumerate(entries):
        try:
            q_data = parse_question_entry(entry)
            questions.append(q_data)
        except Exception:
            invalid_lines.append(idx + 1)

    if invalid_lines:
        print(style_error(
            f"\nWarning: Skipped invalid entries at indices {invalid_lines} in {path}. "
            "Ensure they use 'Answer - Question' format."
        ))

    return questions

def check_enumeration_answer(user_input, correct_ans, mode):
    user_list = [x.strip().lower() for x in user_input.split(',') if x.strip()]
    correct_list = [x.strip().lower() for x in correct_ans.split(',') if x.strip()]

    if mode == 'sequence':
        return user_list == correct_list
    
    return sorted(user_list) == sorted(correct_list)

def handle_enum_question(item):
    correct_list = [x.strip() for x in item["answer"].split(',') if x.strip()]
    
    print(style_cyan(f"Enumeration! Enter answers one by one. Total: {len(correct_list)}"))
    if item["enum_mode"] == "sequence":
        print(style_cyan("Strict Order required."))
    else:
        print(style_cyan("Any Order accepted."))

    user_enum = []
    for i in range(1, len(correct_list) + 1):
        ans = input(style_green(f"  {i}. "))
        user_enum.append(ans)
    
    user_ans_str = ','.join(user_enum)
    is_correct = check_enumeration_answer(user_ans_str, item["answer"], item["enum_mode"])
    
    return is_correct, user_ans_str.replace(',', ', ')

def handle_standard_question(item):
    user_ans = input(style_green("Enter Your Answer: "))
    is_correct = user_ans.lower().strip() == item["answer"].lower().strip()
    return is_correct, user_ans

def run_quiz(questions):
    if not questions:
        print("No questions loaded.")
        return

    score = 0
    wrongs = []
    random.shuffle(questions)

    print(style_blue(f"\nStarting Quiz: {len(questions)} items loaded."))

    for idx, item in enumerate(questions, start=1):
        print(f"\n{idx}. {item['question']}")

        if item.get("is_enum"):
            is_correct, user_ans_display = handle_enum_question(item)
        else:
            is_correct, user_ans_display = handle_standard_question(item)

        if is_correct:
            score += 1
        else:
            wrongs.append({
                "question": item["question"],
                "correct": style_green(f"Right answer: {item['answer']}"),
                "user": style_error(f"Your answer: {user_ans_display}")
            })

    print('\n' + '-'*30)
    total_score = int((score / len(questions)) * 100)
    
    msg = f"You got {score}/{len(questions)} ({style_green(total_score)}%)"
    
    if total_score >= 95:
        print(f"Excellent! {msg}. Good job!")
    elif total_score > 75:
        print(f"Well done! {msg}.")
    elif total_score > 50:
        print(f"Not bad. {msg}. Keep practicing.")
    else:
        print(f"Needs improvement. {msg}.")
    
    print('\n\n')

    if wrongs:
        print(style_highlight('_________ Review Mistakes __________'))
        for w in wrongs:
            print(f"Q: {w['question']}")
            print(w['user'])
            print(w['correct'])
            print()
    else:
        print("Perfect Score! Congratulations!\n")