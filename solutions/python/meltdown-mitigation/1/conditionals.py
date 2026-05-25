


def is_criticality_balanced(temperature, neutrons_emitted):
    return temperature < 800 and neutrons_emitted > 500 and temperature * neutrons_emitted < 500000


def reactor_efficiency(voltage, current, theoretical_max_power):
    percentage_value = (voltage * current / theoretical_max_power) * 100
    if percentage_value >= 80:
        return "green"
    elif percentage_value >= 60:
        return "orange"
    elif percentage_value >= 30:
        return "red"
    elif percentage_value >= 0:
        return "black"


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if temperature * neutrons_produced_per_second < threshold * 0.9:
        return "LOW"
    elif threshold >= temperature * neutrons_produced_per_second >= threshold * 0.9 or threshold * 1.1 >= temperature * neutrons_produced_per_second >= threshold:
        return "NORMAL"
    else:
        return "DANGER"