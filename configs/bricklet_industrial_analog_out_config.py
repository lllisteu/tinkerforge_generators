# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Industrial Analog Out Bricklet communication config

from generators.configs.openhab_commonconfig import *

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 258,
    'name': 'Industrial Analog Out',
    'display_name': 'Industrial Analog Out',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Generates configurable DC voltage and current, 0V to 10V and 4mA to 20mA',
        'de': 'Erzeugt konfigurierbare Gleichspannung und -strom, 0V bis 10V und 4mA bis 20mA'
    },
    'released': True,
    'documented': True,
    'discontinued': True, # replaced by Industrial Analog Out Bricklet 2.0
    'features': [
        'device',
        'bricklet_get_identity'
    ],
    'constant_groups': [],
    'packets': [],
    'examples': []
}

com['constant_groups'].append({
'name': 'Voltage Range',
'type': 'uint8',
'constants': [('0 To 5V', 0),
              ('0 To 10V', 1)]
})

com['constant_groups'].append({
'name': 'Current Range',
'type': 'uint8',
'constants': [('4 To 20mA', 0),
              ('0 To 20mA', 1),
              ('0 To 24mA', 2)]
})

com['packets'].append({
'type': 'function',
'name': 'Enable',
'elements': [],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Enables the output of voltage and current.

The default is disabled.
""",
'de':
"""
Aktiviert die Ausgabe von Spannung und Strom.

Der Standardwert ist deaktiviert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Disable',
'elements': [],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Disables the output of voltage and current.

The default is disabled.
""",
'de':
"""
Deaktiviert die Ausgabe von Spannung und Strom.

Der Standardwert ist deaktiviert.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Is Enabled',
'elements': [('Enabled', 'bool', 1, 'out', {'default': False})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns *true* if output of voltage and current is enabled, *false* otherwise.
""",
'de':
"""
Gibt *true* zurück falls die Ausgabe von Spannung und Strom aktiviert ist,
*false* sonst.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Voltage',
'elements': [('Voltage', 'uint16', 1, 'in', {'scale': (1, 1000), 'unit': 'Volt', 'range': (0, 10000)})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Sets the output voltage.

The output voltage and output current are linked. Changing the output voltage
also changes the output current.
""",
'de':
"""
Setzt die Ausgangsspannung.

Die Ausgangsspannung und der Ausgangsstrom sind gekoppelt. Eine Änderung der
Ausgangsspannung führt auch zu einer Änderung des Ausgangsstroms.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Voltage',
'elements': [('Voltage', 'uint16', 1, 'out', {'scale': (1, 1000), 'unit': 'Volt', 'range': (0, 10000)})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the voltage as set by :func:`Set Voltage`.
""",
'de':
"""
Gibt die Spannung zurück, wie von :func:`Set Voltage` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Current',
'elements': [('Current', 'uint16', 1, 'in', {'scale': (1, 10**6), 'unit': 'Ampere', 'range': (0, 24000)})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Sets the output current.

The output current and output voltage are linked. Changing the output current
also changes the output voltage.
""",
'de':
"""
Setzt den Ausgangsstrom.

Der Ausgangsstrom und die Ausgangsspannung sind gekoppelt. Eine Änderung des
Ausgangsstroms führt auch zu einer Änderung der Ausgangsspannung.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Current',
'elements': [('Current', 'uint16', 1, 'out', {'scale': (1, 10**6), 'unit': 'Ampere', 'range': (0, 24000)})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the current as set by :func:`Set Current`.
""",
'de':
"""
Gibt die Spannung zurück, wie von :func:`Set Current` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Configuration',
'elements': [('Voltage Range', 'uint8', 1, 'in', {'constant_group': 'Voltage Range', 'default': 1}),
             ('Current Range', 'uint8', 1, 'in', {'constant_group': 'Current Range', 'default': 0})],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Configures the voltage and current range.

Possible voltage ranges are:

* 0V to 5V
* 0V to 10V

Possible current ranges are:

* 4mA to 20mA
* 0mA to 20mA
* 0mA to 24mA

The resolution will always be 12 bit. This means, that the
precision is higher with a smaller range.
""",
'de':
"""
Konfiguriert die Spannungs- und Stromwertebereiche.

Einstellbare Spannungswertebereiche sind:

* 0V bis 5V
* 0V bis 10V

Einstellbare Stromwertebereiche sind:

* 4mA bis 20mA
* 0mA bis 20mA
* 0mA bis 24mA

Die Auflösung ist immer 12 Bit. Dass heißt, die Genauigkeit erhöht
sich bei kleineren Wertebereichen.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Configuration',
'elements': [('Voltage Range', 'uint8', 1, 'out', {'constant_group': 'Voltage Range', 'default': 1}),
             ('Current Range', 'uint8', 1, 'out', {'constant_group': 'Current Range', 'default': 0})],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the configuration as set by :func:`Set Configuration`.
""",
'de':
"""
Gibt die Konfiguration zurück, wie von :func:`Set Configuration` gesetzt.
"""
}]
})

com['examples'].append({
'name': 'Simple Voltage',
'functions': [('setter', 'Set Voltage', [('uint16', 3300)], 'Set output voltage to 3.3V', None),
              ('setter', 'Enable', [], None, None),
              ('wait',)],
'cleanups': [('setter', 'Disable', [], None, None)]
})

com['examples'].append({
'name': 'Simple Current',
'functions': [('setter', 'Set Current', [('uint16', 4500)], 'Set output current to 4.5mA', None),
              ('setter', 'Enable', [], None, None),
              ('wait',)],
'cleanups': [('setter', 'Disable', [], None, None)]
})

com['openhab'] = {
    'imports': oh_generic_channel_imports() + ['org.eclipse.smarthome.core.library.types.OnOffType'],
    'params': [
        {
            'virtual': True,
            'name': 'Control Voltage',
            'type': 'integer',
            'options': [
                ('Current', 0),
                ('Voltage', 1),
            ],
            'limit_to_options': 'true',
            'default': 1,

            'label': {'en': 'Output Configuration', 'de': 'Ausgabekonfiguration'},
            'description': {'en': 'Sets the output configuration. As the output voltage and current level depend on each other, only one can be controlled at the same time.',
                            'de': 'Setzt die Ausgabekonfiguration. Da die ausgegebene Spannung und Stromstärke von einander abhängen, kann nur einer der Werte gleichzeitig gesteuert werden.'}
        }, {
            'packet': 'Set Configuration',
            'element': 'Voltage Range',

            'name': 'Voltage Range',
            'type': 'integer',

            'label': {'en': 'Voltage Range', 'de': 'Spannungsbereich'},
            'description': {'en': 'Configures the voltage range. The resolution will always be 12 bit. This means, that the precision is higher with a smaller range.',
                            'de': 'Konfiguriert den Spannungswertebereich. Die Auflösung ist immer 12 Bit. Dass heißt, die Genauigkeit erhöht sich bei kleineren Wertebereichen.'}
        }, {
            'packet': 'Set Configuration',
            'element': 'Current Range',

            'name': 'Current Range',
            'type': 'integer',
            'label': {'en': 'Current Range', 'de': 'Stromstärkenbereich'},
            'description': {'en': 'Configures the current range. The resolution will always be 12 bit. This means, that the precision is higher with a smaller range.',
                            'de': 'Konfiguriert den Stromstärken-Wertebereich. Die Auflösung ist immer 12 Bit. Dass heißt, die Genauigkeit erhöht sich bei kleineren Wertebereichen.'}
        }
    ],
    'init_code': """this.setConfiguration(cfg.voltageRange.shortValue(), cfg.currentRange.shortValue());""",
    'channels': [{
            'id': 'Enabled',
            'type': 'Enabled',

            'setters': [{
                    'predicate': 'cmd == OnOffType.ON',
                    'packet': 'Enable',
                    'packet_params': [],
                    'command_type': "OnOffType",
                }, {
                    'predicate': 'cmd == OnOffType.OFF',
                    'packet': 'Disable',
                    'packet_params': [],
                    'command_type': "OnOffType",
                }
            ],

            'getters': [{
                'packet': 'Is Enabled',
                'element': '{title_words}',
                'transform': 'value ? OnOffType.ON : OnOffType.OFF'
            }]
        }, {
            'id': 'Current',
            'type': 'Current',

            'predicate': 'cfg.controlVoltage == 0',

            'setters': [{
                'packet': 'Set {title_words}',
                'element': '{title_words}',
                'packet_params': ['(int)(cmd.doubleValue(){divisor})'],
                'command_type': "Number"
            }],

            'getters': [{
                'packet': 'Get {title_words}',
                'element': '{title_words}',
                'transform': 'new {number_type}(value{divisor}{unit})'}],
        },
        {
            'id': 'Voltage',
            'type': 'Voltage',

            'predicate': 'cfg.controlVoltage == 1',

            'setters': [{
                'packet': 'Set {title_words}',
                'element': '{title_words}',
                'packet_params': ['(int)(cmd.doubleValue(){divisor})'],
                'command_type': "Number"
            }],

            'getters': [{
                'packet': 'Get {title_words}',
                'element': '{title_words}',
                'transform': 'new {number_type}(value{divisor}{unit})'}],
        }
    ],
    'channel_types': [
        oh_generic_channel_type('Enabled', 'Switch', {'en': 'Output', 'de': 'Ausgabe'},
                    update_style=None,
                    description={'en': 'Enables/disables the output of voltage and current.',
                                 'de': 'Aktiviert/Deaktiviert die Ausgabe von Spannung und Strom.'}),
        oh_generic_channel_type('Voltage', 'Number', {'en': 'Output Voltage', 'de': 'Ausgabespannung'},
                    update_style=None,
                    description={'en': 'The output voltage. The output voltage and output current are linked. Changing the output voltage also changes the output current.',
                                 'de': 'Die Ausgabespannung. Die Ausgangsspannung und der Ausgangsstrom sind gekoppelt. Eine Änderung der Ausgangsspannung führt auch zu einer Änderung des Ausgangsstroms.'}),
        oh_generic_channel_type('Current', 'Number', {'en': 'Output Current', 'de': 'Ausgabestrom'},
                    update_style=None,
                    description={'en': 'The output current. The output current and output voltage are linked. Changing the output current also changes the output voltage.',
                                 'de': 'Der Ausgabestrom. Der Ausgangsstrom und die Ausgangsspannung sind gekoppelt. Eine Änderung des Ausgangsstroms führt auch zu einer Änderung der Ausgangsspannung.'})
    ],
    'actions': [{'fn': 'Enable', 'refreshs': ['Enabled']}, {'fn': 'Disable', 'refreshs': ['Enabled']}, 'Is Enabled',
                'Get Voltage', 'Get Current', 'Get Configuration']
}
