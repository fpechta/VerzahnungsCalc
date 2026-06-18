def pitch_diameter(module, tooth_count):
    # Teilkreisdurchmesser: d = m * z
    return module * tooth_count


def addendum_diameter(module, tooth_count):
    # Kopfkreisdurchmesser: da = m * (z + 2)
    return module * (tooth_count + 2)


def root_diameter(module, tooth_count):
    # Fußkreisdurchmesser: df = m * (z - 2.5)
    return module * (tooth_count - 2.5)


def gear_ratio(tooth_count_driven, tooth_count_drive):
    # Übersetzungsverhältnis: i = z2 / z1
    return tooth_count_driven / tooth_count_drive


def calculate_gear(module, tooth_count):
    return {
        'pitch_diameter': pitch_diameter(module, tooth_count),
        'addendum_diameter': addendum_diameter(module, tooth_count),
        'root_diameter': root_diameter(module, tooth_count),
    }
