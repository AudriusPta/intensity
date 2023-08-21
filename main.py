def illumination_intensity(distance: int) -> float:
    return 3 ** (-(distance / 90) ** 2)

def working_street_lights(road_length: int, not_working_street_lights: list[int]) -> tuple:
    min_intensity = float('inf')
    min_intensity_light = None

    working_lights = [i for i in range(road_length // 20 + 1) if i not in not_working_street_lights]

    for i, light in enumerate(not_working_street_lights):
        closest_working_distance = float('inf')
        for w_light in working_lights:
            distance_to_working = abs(light * 20 - w_light * 20)
            closest_working_distance = min(closest_working_distance, distance_to_working)

        intensity = illumination_intensity(closest_working_distance)

        if intensity < min_intensity or (intensity == min_intensity and light < min_intensity_light):
            min_intensity = intensity
            min_intensity_light = light

    return min_intensity_light, min_intensity

road_length = 2000
not_working_street_lights = [5,6,7,8,15,16,17,18,37,38,39]
min_light, min_illumination = working_street_lights(road_length, not_working_street_lights)
print(min_light, min_illumination)