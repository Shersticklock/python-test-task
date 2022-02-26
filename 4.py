import argparse
import json

parser = argparse.ArgumentParser(description="File parser script")
parser.add_argument("-f", dest="filename", required=True)


def get_questions(data: dict) -> list:
    rounds = data.get('game').get('rounds')
    questions = list()
    for round in rounds:
        questions_for_round = round.get('questions')
        if questions_for_round:
            questions.extend(questions_for_round)
    return questions


def count_questions(data: dict):
    # вывести количество вопросов (questions)
    questions_count = 0
    questions = get_questions(data)
    questions_count += len(questions)
    print(questions_count)


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    # вывести количество вопросов (questions)
    questions = get_questions(data)
    for question in questions:
        correct_answer = question.get('correct_answer')
        type = question.get('type')
        answers = question.get('answers')
        if correct_answer and type in ['select', 'multiselect']:
            if isinstance(correct_answer, list):
                for answer in correct_answer:
                    print(answers[answer])
            else:
                print(answers[correct_answer])
        elif correct_answer:
            print(correct_answer)


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    questions = get_questions(data)
    if questions:
        max_answer_time = questions[0].get('time_to_answer', 0)
        for question in questions[1:]:
            answer_time = question.get('time_to_answer', 0)
            if answer_time > max_answer_time:
                max_answer_time = answer_time
        print(max_answer_time)


def main(args):
    with open(args.filename) as json_file:
        data = json.load(json_file)
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)


if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
