# -*- coding: utf-8 -*-

# Redistribution and use in source and binary forms of this file,
# with or without modification, are permitted. See the Creative
# Commons Zero (CC0 1.0) License for more details.

# Moisture Bricklet communication config

from generators.configs.commonconstants import THRESHOLD_OPTION_CONSTANT_GROUP

from generators.configs.openhab_commonconfig import *

com = {
    'author': 'Olaf Lüke <olaf@tinkerforge.com>',
    'api_version': [2, 0, 0],
    'category': 'Bricklet',
    'device_identifier': 232,
    'name': 'Moisture',
    'display_name': 'Moisture',
    'manufacturer': 'Tinkerforge',
    'description': {
        'en': 'Measures soil moisture',
        'de': 'Misst Erdfeuchtigkeit'
    },
    'released': True,
    'documented': True,
    'discontinued': True, # currently no replacement available
    'features': [
        'device',
        'bricklet_get_identity'
    ],
    'constant_groups': [],
    'packets': [],
    'examples': []
}

com['constant_groups'].append(THRESHOLD_OPTION_CONSTANT_GROUP)

com['packets'].append({
'type': 'function',
'name': 'Get Moisture Value',
'elements': [('Moisture', 'uint16', 1, 'out', {'range': (0, 4095)})],
'since_firmware': [1, 0, 0],
'doc': ['bf', {
'en':
"""
Returns the current moisture value.
A small value corresponds to little moisture, a big
value corresponds to much moisture.

If you want to get the moisture value periodically, it is recommended
to use the :cb:`Moisture` callback and set the period with
:func:`Set Moisture Callback Period`.
""",
'de':
"""
Gibt den aktuellen Feuchtigkeitswert zurück. Ein kleiner Wert entspricht einer
geringen Feuchtigkeit, ein großer Wert entspricht einer hohen
Feuchtigkeit.

Wenn der Feuchtigkeitswert periodisch abgefragt werden soll, wird empfohlen
den :cb:`Moisture` Callback zu nutzen und die Periode mit
:func:`Set Moisture Callback Period` vorzugeben.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Moisture Callback Period',
'elements': [('Period', 'uint32', 1, 'in', {'scale': (1, 1000), 'unit': 'Second', 'default': 0})],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period with which the :cb:`Moisture` callback is triggered
periodically. A value of 0 turns the callback off.

The :cb:`Moisture` callback is only triggered if the moisture value has changed
since the last triggering.
""",
'de':
"""
Setzt die Periode mit welcher der :cb:`Moisture` Callback ausgelöst wird.
Ein Wert von 0 deaktiviert den Callback.

Der :cb:`Moisture` Callback wird nur ausgelöst, wenn sich der Feuchtigkeitswert
seit der letzten Auslösung geändert hat.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Moisture Callback Period',
'elements': [('Period', 'uint32', 1, 'out', {'scale': (1, 1000), 'unit': 'Second', 'default': 0})],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the period as set by :func:`Set Moisture Callback Period`.
""",
'de':
"""
Gibt die Periode zurück, wie von :func:`Set Moisture Callback Period` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Moisture Callback Threshold',
'elements': [('Option', 'char', 1, 'in', {'constant_group': 'Threshold Option', 'default': 'x'}),
             ('Min', 'uint16', 1, 'in', {'default': 0}),
             ('Max', 'uint16', 1, 'in', {'default': 0})],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the thresholds for the :cb:`Moisture Reached` callback.

The following options are possible:

.. csv-table::
 :header: "Option", "Description"
 :widths: 10, 100

 "'x'",    "Callback is turned off"
 "'o'",    "Callback is triggered when the moisture value is *outside* the min and max values"
 "'i'",    "Callback is triggered when the moisture value is *inside* the min and max values"
 "'<'",    "Callback is triggered when the moisture value is smaller than the min value (max is ignored)"
 "'>'",    "Callback is triggered when the moisture value is greater than the min value (max is ignored)"
""",
'de':
"""
Setzt den Schwellwert für den :cb:`Moisture Reached` Callback.

Die folgenden Optionen sind möglich:

.. csv-table::
 :header: "Option", "Beschreibung"
 :widths: 10, 100

 "'x'",    "Callback ist inaktiv"
 "'o'",    "Callback wird ausgelöst, wenn der Feuchtigkeitswert *außerhalb* des min und max Wertes ist"
 "'i'",    "Callback wird ausgelöst, wenn der Feuchtigkeitswert *innerhalb* des min und max Wertes ist"
 "'<'",    "Callback wird ausgelöst, wenn der Feuchtigkeitswert kleiner als der min Wert ist (max wird ignoriert)"
 "'>'",    "Callback wird ausgelöst, wenn der Feuchtigkeitswert größer als der min Wert ist (max wird ignoriert)"
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Moisture Callback Threshold',
'elements': [('Option', 'char', 1, 'out', {'constant_group': 'Threshold Option', 'default': 'x'}),
             ('Min', 'uint16', 1, 'out', {'default': 0}),
             ('Max', 'uint16', 1, 'out', {'default': 0})],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the threshold as set by :func:`Set Moisture Callback Threshold`.
""",
'de':
"""
Gibt den Schwellwert zurück, wie von :func:`Set Moisture Callback Threshold` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Debounce Period',
'elements': [('Debounce', 'uint32', 1, 'in', {'scale': (1, 1000), 'unit': 'Second', 'default': 100})],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Sets the period with which the threshold callback

* :cb:`Moisture Reached`

is triggered, if the threshold

* :func:`Set Moisture Callback Threshold`

keeps being reached.
""",
'de':
"""
Setzt die Periode mit welcher die Schwellwert Callback

* :cb:`Moisture Reached`

ausgelöst wird, wenn der Schwellwert

* :func:`Set Moisture Callback Threshold`

weiterhin erreicht bleibt.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Debounce Period',
'elements': [('Debounce', 'uint32', 1, 'out', {'scale': (1, 1000), 'unit': 'Second', 'default': 100})],
'since_firmware': [1, 0, 0],
'doc': ['ccf', {
'en':
"""
Returns the debounce period as set by :func:`Set Debounce Period`.
""",
'de':
"""
Gibt die Entprellperiode zurück, wie von :func:`Set Debounce Period` gesetzt.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Moisture',
'elements': [('Moisture', 'uint16', 1, 'out', {'range': (0, 4095)})],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered periodically with the period that is set by
:func:`Set Moisture Callback Period`. The :word:`parameter` is the
moisture value of the sensor.

The :cb:`Moisture` callback is only triggered if the moisture value has changed
since the last triggering.
""",
'de':
"""
Dieser Callback wird mit der Periode, wie gesetzt mit :func:`Set Moisture Callback Period`,
ausgelöst. Der :word:`parameter` ist der Feuchtigkeitswert des Sensors.

The :cb:`Moisture` Callback wird nur ausgelöst, wenn sich der Feuchtigkeitswert
seit der letzten Auslösung geändert hat.
"""
}]
})

com['packets'].append({
'type': 'callback',
'name': 'Moisture Reached',
'elements': [('Moisture', 'uint16', 1, 'out', {'range': (0, 4095)})],
'since_firmware': [1, 0, 0],
'doc': ['c', {
'en':
"""
This callback is triggered when the threshold as set by
:func:`Set Moisture Callback Threshold` is reached.
The :word:`parameter` is the moisture value of the sensor.

If the threshold keeps being reached, the callback is triggered periodically
with the period as set by :func:`Set Debounce Period`.
""",
'de':
"""
Dieser Callback wird ausgelöst, wenn der Schwellwert, wie von
:func:`Set Moisture Callback Threshold` gesetzt, erreicht wird.
Der :word:`parameter` ist die Feuchtigkeitswert des Sensors.

Wenn der Schwellwert erreicht bleibt, wird der Callback mit der Periode, wie
mit :func:`Set Debounce Period` gesetzt, ausgelöst.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Set Moving Average',
'elements': [('Average', 'uint8', 1, 'in', {'range': (0, 100), 'default': 100})],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Sets the length of a `moving averaging <https://en.wikipedia.org/wiki/Moving_average>`__
for the moisture value.

Setting the length to 0 will turn the averaging completely off. With less
averaging, there is more noise on the data.
""",
'de':
"""
Setzt die Länge eines `gleitenden Mittelwerts <https://de.wikipedia.org/wiki/Gleitender_Mittelwert>`__
für den Feuchtigkeitswert.

Wenn die Länge auf 0 gesetzt wird, ist das Averaging komplett aus. Desto kleiner
die Länge des Mittelwerts ist, desto mehr Rauschen ist auf den Daten.
"""
}]
})

com['packets'].append({
'type': 'function',
'name': 'Get Moving Average',
'elements': [('Average', 'uint8', 1, 'out', {'range': (0, 100), 'default': 100})],
'since_firmware': [1, 0, 0],
'doc': ['af', {
'en':
"""
Returns the length moving average as set by :func:`Set Moving Average`.
""",
'de':
"""
Gibt die Länge des gleitenden Mittelwerts zurück, wie von
:func:`Set Moving Average` gesetzt.
"""
}]
})

com['examples'].append({
'name': 'Simple',
# FIXME: name mismatch here because of a naming inconsistency in the API
'functions': [('getter', ('Get Moisture Value', 'moisture value'), [(('Moisture', 'Moisture Value'), 'uint16', 1, None, None, None)], [])]
})

com['examples'].append({
'name': 'Callback',
# FIXME: name mismatch here because of a naming inconsistency in the API
'functions': [('callback', ('Moisture', 'moisture value'), [(('Moisture', 'Moisture Value'), 'uint16', 1, None, None, None)], None, None),
              ('callback_period', ('Moisture', 'moisture value'), [], 1000)]
})

com['examples'].append({
'name': 'Threshold',
# FIXME: name mismatch here because of a naming inconsistency in the API
'functions': [('debounce_period', 1000),
              ('callback', ('Moisture Reached', 'moisture value reached'), [(('Moisture', 'Moisture Value'), 'uint16', 1, None, None, None)], None, None),
              ('callback_threshold', ('Moisture', 'moisture value'), [], '>', [(200, 0)])]
})

moisture_channel = oh_generic_old_style_channel('Moisture', 'Moisture')
moisture_channel['getters'][0]['packet'] = 'Get Moisture Value'

com['openhab'] = {
    'imports': oh_generic_channel_imports(),
    'param_groups': oh_generic_channel_param_groups(),
    'params': [{
        'packet': 'Set Moving Average',
        'element': 'Average',

        'name': 'Moving Average Length',
        'type': 'integer',
        'label': {'en': 'Moving Average Length', 'de': 'Länge des gleitenden Mittelwerts'},
        'description': {'en': 'The length of a moving averaging for the moisture value.\n\nSetting the length to 0 will turn the averaging off. With less averaging, there is more noise on the data.',
                        'de': 'Setzt die Länge eines gleitenden Mittelwerts für den Feuchtigkeitswert.\n\nWenn die Länge auf 0 gesetzt wird, ist das Averaging komplett aus. Desto kleiner die Länge des Mittelwerts ist, desto mehr Rauschen ist auf den Daten.'}

    }],
    'init_code': """this.setMovingAverage(cfg.movingAverageLength.shortValue());""",
    'channels': [
        moisture_channel
    ],
    'channel_types': [
        oh_generic_channel_type('Moisture', 'Number', {'en': 'Moisture', 'de': 'Feuchtigkeit'},
                    update_style='Callback Period',
                    description={'en': 'Returns the current moisture value. A small value corresponds to little moisture, a big value corresponds to much moisture.',
                                 'de': 'Gibt den aktuellen Feuchtigkeitswert zurück. Ein kleiner Wert entspricht einer geringen Feuchtigkeit, ein großer Wert entspricht einer hohen Feuchtigkeit.'})
    ],
    'actions': ['Get Moisture Value', 'Get Moving Average']
}
