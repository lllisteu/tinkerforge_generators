# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Analog In Bricklet 3.0 communication config

from generators.configs.commonconstants import THRESHOLD_OPTION_CONSTANT_GROUP
from generators.configs.commonconstants import add_callback_value_function

from generators.configs.openhab_commonconfig import *

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 295,
    'name': 'Analog In V3',
    'display_name': 'Analog In 3.0',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Measures DC voltage between 0V and 42V',
        'de': 'Misst Gleichspannung zwischen 0V und 42V'
    },
    'released': True,
    'documented': True,
    'discontinued': False,
    'features': [
        'device',
        'comcu_bricklet',
        'bricklet_get_identity'
    ],
    'constant_groups': [],
    'packets': [],
    'examples': []
}

com['constant_groups'].append(THRESHOLD_OPTION_CONSTANT_GROUP)

com['constant_groups'].append({
'name': 'Oversampling',
'type': 'uint8',
'constants': [('32', 0),
              ('64', 1),
              ('128', 2),
              ('256', 3),
              ('512', 4),
              ('1024', 5),
              ('2048', 6),
              ('4096', 7),
              ('8192', 8),
              ('16384', 9)]
})

voltage_doc = {
'en':
"""
Returns the measured voltage. The resolution is approximately 10mV to 1mV
depending on the oversampling configuration (:func:`Set Oversampling`).
""",
'de':
"""
Gibt die gemessene Spannung zurück. Die Auflösung ca. 10mV bis 1mV abhängig von der
Überabtastungs-Konfiguration (:func:`Set Oversampling`).
"""
}

add_callback_value_function(
    packets   = com['packets'],
    name      = 'Get Voltage',
    data_name = 'Voltage',
    data_type = 'uint16',
    doc       = voltage_doc,
    scale     = (1, 1000),
    unit      = 'Volt',
    range_    = (0, 42000)
)

com['packets'].append({
'type': 'function',
'name': 'Set Oversampling',
'elements': [('Oversampling', 'uint8', 1, 'in', {'constant_group': 'Oversampling', 'default': 7})],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Sets the oversampling between 32x and 16384x. The Bricklet
takes one 12bit sample every 17.5µs. Thus an oversampling
of 32x is equivalent to an integration time of 0.56ms and
a oversampling of 16384x is equivalent to an integration
time of 286ms.

The oversampling uses the moving average principle. A
new value is always calculated once per millisecond.

With increased oversampling the noise decreases. With decreased
oversampling the reaction time increases (changes in voltage will be
measured faster).
""",
'de':
"""
Stellt die Überabtastung zwischen 32x und 16384x ein. Das Bricklet misst einen
12-Bit Wert alle 17,5µs. Daher entspricht eine Überabtastung von 32x einer
Integrationszeit von 0,56ms und eine Überabtastung von 16384x einer
Integrationszeit von 286ms.

Die Überabtastung arbeitet mit einem gleidenden Mittelwert. Ein neuer Messwert
wird jede Millisekunden bestimmt.

Je höher die Überabtastung desto geringer das Rauschen. Je geringer die
Überabtastung steigt die Reaktionszeit (Änderungen der Eingangsspannung werden
schneller erkannt).
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Oversampling',
'elements': [('Oversampling', 'uint8', 1, 'out', {'constant_group': 'Oversampling', 'default': 7})],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the oversampling value as set by :func:`Set Oversampling`.
""",
'de':
"""
Gibt den Überabtastungsfaktor zurück, wie von :func:`Set Oversampling` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Calibration',
'elements': [('Offset', 'int16', 1, 'in', {'scale': (1, 1000), 'unit': 'Volt'}),
             ('Multiplier', 'uint16', 1, 'in', {}),
             ('Divisor', 'uint16', 1, 'in', {})],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Sets a calibration for the measured voltage value.
The formula for the calibration is as follows::

 Calibrated Value = (Value + Offset) * Multiplier / Divisor

We recommend that you use the Brick Viewer to calibrate
the Bricklet. The calibration will be saved internally and only
has to be done once.
""",
'de':
"""
Setzt die Kalibrierung für die gemessene Spannung. Die Formel lautet::

 Kalibrierter Wert = (Wert + Offset) * Multiplier / Divisor

Wir empfehlen für die Kalibrierung den Brick Viewer zu verwenden. Die
Kalibrierung wird im Bricklet gespeichert und muss daher nur einmal durchgeführt
werden.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Calibration',
'elements': [('Offset', 'int16', 1, 'out', {'scale': (1, 1000), 'unit': 'Volt'}),
             ('Multiplier', 'uint16', 1, 'out', {}),
             ('Divisor', 'uint16', 1, 'out', {})],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the calibration as set by :func:`Set Calibration`.
""",
'de':
"""
Gibt die Kalibrierung zurück, wie von :func:`Set Calibration` gesetzt.
"""
}]
})

com['examples'].append({
'name': 'Simple',
'functions': [('getter', ('Get Voltage', 'voltage'), [(('Voltage', 'Voltage'), 'uint16', 1, 1000.0, 'V', None)], [])]
})

com['examples'].append({
'name': 'Callback',
'functions': [('callback', ('Voltage', 'voltage'), [(('Voltage', 'Voltage'), 'uint16', 1, 1000.0, 'V', None)], None, None),
              ('callback_configuration', ('Voltage', 'voltage'), [], 1000, False, 'x', [(0, 0)])]
})

com['examples'].append({
'name': 'Threshold',
'functions': [('callback', ('Voltage', 'voltage'), [(('Voltage', 'Voltage'), 'uint16', 1, 1000.0, 'V', None)], None, None),
              ('callback_configuration', ('Voltage', 'voltage'), [], 1000, False, '<', [(5, 0)])]
})

com['openhab'] = {
    'imports': oh_generic_channel_imports(),
    'param_groups': oh_generic_channel_param_groups(),
    'params': [{
            'packet': 'Set Oversampling',
            'element': 'Oversampling',

            'name': 'Oversampling',
            'type': 'integer',
            'options': [('32x', 0),
                        ('64x', 1),
                        ('128x', 2),
                        ('256x', 3),
                        ('512x', 4),
                        ('1024x', 5),
                        ('2048x', 6),
                        ('4096x', 7),
                        ('8192x', 8),
                        ('16384x', 9)],
            'limit_to_options': 'true',
            'label': {'en': 'Oversampling', 'de': 'Überabtastung'},
            'description': {'en': 'Sets the oversampling between 32x and 16384x. The Bricklet takes one 12bit sample every 17.5µs. Thus an oversampling of 32x is equivalent to an integration time of 0.56ms and a oversampling of 16384x is equivalent to an integration time of 286ms.\n\nThe oversampling uses the moving average principle. A new value is always calculated once per millisecond.\n\nWith increased oversampling the noise decreases. With decreased oversampling the reaction time increases (changes in voltage will be measured faster).',
                            'de': 'Stellt die Überabtastung zwischen 32x und 16384x ein. Das Bricklet misst einen 12-Bit Wert alle 17,5µs. Daher entspricht eine Überabtastung von 32x einer Integrationszeit von 0,56ms und eine Überabtastung von 16384x einer Integrationszeit von 286ms.\n\nDie Überabtastung arbeitet mit einem gleidenden Mittelwert. Ein neuer Messwert wird jede Millisekunden bestimmt.\n\nJe höher die Überabtastung desto geringer das Rauschen. Je geringer die Überabtastung steigt die Reaktionszeit (Änderungen der Eingangsspannung werden schneller erkannt).'}
        }],
    'channels': [
        oh_generic_channel('Voltage', 'Voltage'),
    ],
    'init_code': 'this.setOversampling(cfg.oversampling);',
    'channel_types': [
        oh_generic_channel_type('Voltage', 'Number', {'en': 'Voltage', 'de': 'Spannung'},
                    update_style='Callback Configuration',
                    description={'en': 'The measured voltage', 'de': 'Die gemessene Spannung'}),
    ],
    'actions': ['Get Voltage', 'Get Oversampling', 'Get Calibration']
}
