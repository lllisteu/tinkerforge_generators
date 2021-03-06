# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Piezo Buzzer Bricklet communication config

from generators.configs.openhab_commonconfig import *

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 214,
    'name': 'Piezo Buzzer',
    'display_name': 'Piezo Buzzer',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Creates 1kHz beep',
        'de': 'Erzeugt 1kHz Piepton'
    },
    'released': True,
    'documented': True,
    'discontinued': True, # replaced by Piezo Speaker Bricklet 2.0
    'features': [
        'device',
        'bricklet_get_identity'
    ],
    'constant_groups': [],
    'packets': [],
    'examples': []
}

com['packets'].append({
'type': 'function',
'name': 'Beep',
'elements': [('Duration', 'uint32', 1, 'in', {'scale': (1, 1000), 'unit': 'Second'})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Beeps for the given duration.
""",
'de':
"""
Erzeugt einen Piepton für die angegebene Dauer.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Morse Code',
'elements': [('Morse', 'string', 60, 'in', {})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Sets morse code that will be played by the piezo buzzer. The morse code
is given as a string consisting of "." (dot), "-" (minus) and " " (space)
for *dits*, *dahs* and *pauses*. Every other character is ignored.

For example: If you set the string "...---...", the piezo buzzer will beep
nine times with the durations "short short short long long long short
short short".
""",
'de':
"""
Setzt Morsecode welcher vom Piezosummer abgespielt wird. Der Morsecode wird
als Zeichenkette, mit den Zeichen "." (Punkt), "-" (Minus) und " " (Leerzeichen)
für *kurzes Signale*, *langes Signale* und *Pausen*. Alle anderen Zeichen
werden ignoriert.

Beispiel: Wenn die Zeichenkette "...---..." gesetzt wird, gibt der Piezosummer neun
Pieptöne aus mit den Dauern "kurz kurz kurz lang lang lang kurz kurz kurz".
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Beep Finished',
'elements': [],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered if a beep set by :func:`Beep` is finished
""",
'de':
"""
Dieser Callback wird ausgelöst, wenn ein Piepton, wie von :func:`Beep` gesetzt,
beendet wurde.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Morse Code Finished',
'elements': [],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered if the playback of the morse code set by
:func:`Morse Code` is finished.
""",
'de':
"""
Dieser Callback wird ausgelöst, wenn die Wiedergabe des Morsecodes, wie von
:func:`Morse Code` gesetzt, beendet wurde.
"""
}]
})

com['examples'].append({
'name': 'Beep',
'functions': [('setter', 'Beep', [('uint32', 2000)], 'Make 2 second beep', None)]
})

com['examples'].append({
'name': 'Morse Code',
'functions': [('setter', 'Morse Code', [('string', '... --- ...')], 'Morse SOS', None)]
})

com['openhab'] = {
    'imports': oh_generic_channel_imports() + ['org.eclipse.smarthome.core.library.types.StringType'],
    'param_groups': oh_generic_channel_param_groups(),
    'channels': [{
            'id': 'Beep',
            'type': 'Beep',
            'label': 'Beep',

            'setters': [{
                'packet': 'Beep',
                'element': 'Duration',
                'packet_params': ['(long)(cmd.doubleValue(){divisor})'],
                'command_type': "Number"
            }],
        }, {
            'id': 'Morse Code',
            'type': 'Morse Code',
            'label': 'Morse Code',

            'setters': [{
                'packet': 'Morse Code',
                'element': 'Morse',
                'packet_params': ['cmd.toString()'],
                'command_type': "StringType"
            }],
        }, {
            'id': 'Beep Finished',
            'label': 'Beep Finished',
            'type': 'system.trigger',

            'callbacks': [{
                'packet': 'Beep Finished',
                'transform': '""'}],
            'description': 'This channel is triggered if a beep set by the beep action is finished.'
        }, {
            'id': 'Morse Code Finished',
            'label': 'Morse Code Finished',
            'type': 'system.trigger',

            'callbacks': [{
                'packet': 'Morse Code Finished',
                'transform': '""'}],
            'description': 'This channel is triggered if the playback of the morse code set by the morseCode action is finished.'
        },
    ],
    'channel_types': [
        oh_generic_channel_type('Beep', 'Number', 'Beep',
                    update_style=None,
                    description='Beeps with the duration in s.'),
        oh_generic_channel_type('Morse Code', 'String', 'Morse Code',
                    update_style=None,
                    description="Morse code that will be played by the piezo buzzer. The morse code is given as a string consisting of '.' (dot), '-' (minus) and ' ' (space) for dits, dahs and pauses. Every other character is ignored. For example: If you set the string '...---...', the piezo buzzer will beep nine times with the durations 'short short short long long long short short short'. The maximum string size is 60."),
    ],
    'actions': ['Beep', 'Morse Code']
}
