from random import choices

generated_combinations = []


def generate_new_combination() -> dict:
    while True:
        combination = {
            'background_id': choices(population=(0, 1, 2), weights=(10, 45, 45), k=1)[0],
            'body_id': 0,
            'eyes_id': choices(population=(0, 1), weights=(50, 50), k=1)[0],  # TODO: make chances configurable
            'hat_id': choices(population=(0, 1), weights=(50, 50), k=1)[0],
            'mouth_id': choices(population=(0, 1), weights=(50, 50), k=1)[0]
        }

        if combination not in generated_combinations:
            generated_combinations.append(combination)
            return combination

        print('Collision occurred!')
