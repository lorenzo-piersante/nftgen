from random import randint

generated_combinations = []


def generate_new_combination() -> dict:
    while True:
        combination = {
            'background_id': randint(0, 2),
            'body_id': 0,
            'eyes_id': randint(0, 1),
            'hat_id': randint(0, 1),
            'mouth_id': randint(0, 1)
        }

        if combination not in generated_combinations:
            return combination

        print('Collision occurred!')
