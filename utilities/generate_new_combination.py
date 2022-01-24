from random import choices
from config import background_population, background_weights, body_population, body_weights, eyes_population, \
    eyes_weights, hat_population, hat_weights, mouth_population, mouth_weights

generated_combinations = []


def generate_new_combination() -> dict:
    while True:
        combination = {
            'background_id': choices(population=background_population, weights=background_weights, k=1)[0],
            'body_id': choices(population=body_population, weights=body_weights, k=1)[0],
            'eyes_id': choices(population=eyes_population, weights=eyes_weights, k=1)[0],
            'hat_id': choices(population=hat_population, weights=hat_weights, k=1)[0],
            'mouth_id': choices(population=mouth_population, weights=mouth_weights, k=1)[0]
        }

        if combination not in generated_combinations:
            generated_combinations.append(combination)
            return combination

        print('Collision occurred!')
