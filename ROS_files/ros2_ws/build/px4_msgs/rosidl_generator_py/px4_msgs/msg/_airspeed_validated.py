# generated from rosidl_generator_py/resource/_idl.py.em
# with input from px4_msgs:msg/AirspeedValidated.idl
# generated code does not contain a copyright notice


# Import statements for member types

import rosidl_parser.definition  # noqa: E402, I100


class Metaclass_AirspeedValidated(type):
    """Metaclass of message 'AirspeedValidated'."""

    _CREATE_ROS_MESSAGE = None
    _CONVERT_FROM_PY = None
    _CONVERT_TO_PY = None
    _DESTROY_ROS_MESSAGE = None
    _TYPE_SUPPORT = None

    __constants = {
    }

    @classmethod
    def __import_type_support__(cls):
        try:
            from rosidl_generator_py import import_type_support
            module = import_type_support('px4_msgs')
        except ImportError:
            import logging
            import traceback
            logger = logging.getLogger(
                'px4_msgs.msg.AirspeedValidated')
            logger.debug(
                'Failed to import needed modules for type support:\n' +
                traceback.format_exc())
        else:
            cls._CREATE_ROS_MESSAGE = module.create_ros_message_msg__msg__airspeed_validated
            cls._CONVERT_FROM_PY = module.convert_from_py_msg__msg__airspeed_validated
            cls._CONVERT_TO_PY = module.convert_to_py_msg__msg__airspeed_validated
            cls._TYPE_SUPPORT = module.type_support_msg__msg__airspeed_validated
            cls._DESTROY_ROS_MESSAGE = module.destroy_ros_message_msg__msg__airspeed_validated

    @classmethod
    def __prepare__(cls, name, bases, **kwargs):
        # list constant names here so that they appear in the help text of
        # the message class under "Data and other attributes defined here:"
        # as well as populate each message instance
        return {
        }


class AirspeedValidated(metaclass=Metaclass_AirspeedValidated):
    """Message class 'AirspeedValidated'."""

    __slots__ = [
        '_timestamp',
        '_indicated_airspeed_m_s',
        '_calibrated_airspeed_m_s',
        '_true_airspeed_m_s',
        '_calibrated_ground_minus_wind_m_s',
        '_true_ground_minus_wind_m_s',
        '_airspeed_sensor_measurement_valid',
        '_selected_airspeed_index',
        '_airspeed_derivative_filtered',
        '_throttle_filtered',
        '_pitch_filtered',
    ]

    _fields_and_field_types = {
        'timestamp': 'uint64',
        'indicated_airspeed_m_s': 'float',
        'calibrated_airspeed_m_s': 'float',
        'true_airspeed_m_s': 'float',
        'calibrated_ground_minus_wind_m_s': 'float',
        'true_ground_minus_wind_m_s': 'float',
        'airspeed_sensor_measurement_valid': 'boolean',
        'selected_airspeed_index': 'int8',
        'airspeed_derivative_filtered': 'float',
        'throttle_filtered': 'float',
        'pitch_filtered': 'float',
    }

    SLOT_TYPES = (
        rosidl_parser.definition.BasicType('uint64'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('boolean'),  # noqa: E501
        rosidl_parser.definition.BasicType('int8'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
        rosidl_parser.definition.BasicType('float'),  # noqa: E501
    )

    def __init__(self, **kwargs):
        assert all('_' + key in self.__slots__ for key in kwargs.keys()), \
            'Invalid arguments passed to constructor: %s' % \
            ', '.join(sorted(k for k in kwargs.keys() if '_' + k not in self.__slots__))
        self.timestamp = kwargs.get('timestamp', int())
        self.indicated_airspeed_m_s = kwargs.get('indicated_airspeed_m_s', float())
        self.calibrated_airspeed_m_s = kwargs.get('calibrated_airspeed_m_s', float())
        self.true_airspeed_m_s = kwargs.get('true_airspeed_m_s', float())
        self.calibrated_ground_minus_wind_m_s = kwargs.get('calibrated_ground_minus_wind_m_s', float())
        self.true_ground_minus_wind_m_s = kwargs.get('true_ground_minus_wind_m_s', float())
        self.airspeed_sensor_measurement_valid = kwargs.get('airspeed_sensor_measurement_valid', bool())
        self.selected_airspeed_index = kwargs.get('selected_airspeed_index', int())
        self.airspeed_derivative_filtered = kwargs.get('airspeed_derivative_filtered', float())
        self.throttle_filtered = kwargs.get('throttle_filtered', float())
        self.pitch_filtered = kwargs.get('pitch_filtered', float())

    def __repr__(self):
        typename = self.__class__.__module__.split('.')
        typename.pop()
        typename.append(self.__class__.__name__)
        args = []
        for s, t in zip(self.__slots__, self.SLOT_TYPES):
            field = getattr(self, s)
            fieldstr = repr(field)
            # We use Python array type for fields that can be directly stored
            # in them, and "normal" sequences for everything else.  If it is
            # a type that we store in an array, strip off the 'array' portion.
            if (
                isinstance(t, rosidl_parser.definition.AbstractSequence) and
                isinstance(t.value_type, rosidl_parser.definition.BasicType) and
                t.value_type.typename in ['float', 'double', 'int8', 'uint8', 'int16', 'uint16', 'int32', 'uint32', 'int64', 'uint64']
            ):
                if len(field) == 0:
                    fieldstr = '[]'
                else:
                    assert fieldstr.startswith('array(')
                    prefix = "array('X', "
                    suffix = ')'
                    fieldstr = fieldstr[len(prefix):-len(suffix)]
            args.append(s[1:] + '=' + fieldstr)
        return '%s(%s)' % ('.'.join(typename), ', '.join(args))

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        if self.timestamp != other.timestamp:
            return False
        if self.indicated_airspeed_m_s != other.indicated_airspeed_m_s:
            return False
        if self.calibrated_airspeed_m_s != other.calibrated_airspeed_m_s:
            return False
        if self.true_airspeed_m_s != other.true_airspeed_m_s:
            return False
        if self.calibrated_ground_minus_wind_m_s != other.calibrated_ground_minus_wind_m_s:
            return False
        if self.true_ground_minus_wind_m_s != other.true_ground_minus_wind_m_s:
            return False
        if self.airspeed_sensor_measurement_valid != other.airspeed_sensor_measurement_valid:
            return False
        if self.selected_airspeed_index != other.selected_airspeed_index:
            return False
        if self.airspeed_derivative_filtered != other.airspeed_derivative_filtered:
            return False
        if self.throttle_filtered != other.throttle_filtered:
            return False
        if self.pitch_filtered != other.pitch_filtered:
            return False
        return True

    @classmethod
    def get_fields_and_field_types(cls):
        from copy import copy
        return copy(cls._fields_and_field_types)

    @property
    def timestamp(self):
        """Message field 'timestamp'."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'timestamp' field must be of type 'int'"
            assert value >= 0 and value < 18446744073709551616, \
                "The 'timestamp' field must be an unsigned integer in [0, 18446744073709551615]"
        self._timestamp = value

    @property
    def indicated_airspeed_m_s(self):
        """Message field 'indicated_airspeed_m_s'."""
        return self._indicated_airspeed_m_s

    @indicated_airspeed_m_s.setter
    def indicated_airspeed_m_s(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'indicated_airspeed_m_s' field must be of type 'float'"
        self._indicated_airspeed_m_s = value

    @property
    def calibrated_airspeed_m_s(self):
        """Message field 'calibrated_airspeed_m_s'."""
        return self._calibrated_airspeed_m_s

    @calibrated_airspeed_m_s.setter
    def calibrated_airspeed_m_s(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'calibrated_airspeed_m_s' field must be of type 'float'"
        self._calibrated_airspeed_m_s = value

    @property
    def true_airspeed_m_s(self):
        """Message field 'true_airspeed_m_s'."""
        return self._true_airspeed_m_s

    @true_airspeed_m_s.setter
    def true_airspeed_m_s(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'true_airspeed_m_s' field must be of type 'float'"
        self._true_airspeed_m_s = value

    @property
    def calibrated_ground_minus_wind_m_s(self):
        """Message field 'calibrated_ground_minus_wind_m_s'."""
        return self._calibrated_ground_minus_wind_m_s

    @calibrated_ground_minus_wind_m_s.setter
    def calibrated_ground_minus_wind_m_s(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'calibrated_ground_minus_wind_m_s' field must be of type 'float'"
        self._calibrated_ground_minus_wind_m_s = value

    @property
    def true_ground_minus_wind_m_s(self):
        """Message field 'true_ground_minus_wind_m_s'."""
        return self._true_ground_minus_wind_m_s

    @true_ground_minus_wind_m_s.setter
    def true_ground_minus_wind_m_s(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'true_ground_minus_wind_m_s' field must be of type 'float'"
        self._true_ground_minus_wind_m_s = value

    @property
    def airspeed_sensor_measurement_valid(self):
        """Message field 'airspeed_sensor_measurement_valid'."""
        return self._airspeed_sensor_measurement_valid

    @airspeed_sensor_measurement_valid.setter
    def airspeed_sensor_measurement_valid(self, value):
        if __debug__:
            assert \
                isinstance(value, bool), \
                "The 'airspeed_sensor_measurement_valid' field must be of type 'bool'"
        self._airspeed_sensor_measurement_valid = value

    @property
    def selected_airspeed_index(self):
        """Message field 'selected_airspeed_index'."""
        return self._selected_airspeed_index

    @selected_airspeed_index.setter
    def selected_airspeed_index(self, value):
        if __debug__:
            assert \
                isinstance(value, int), \
                "The 'selected_airspeed_index' field must be of type 'int'"
            assert value >= -128 and value < 128, \
                "The 'selected_airspeed_index' field must be an integer in [-128, 127]"
        self._selected_airspeed_index = value

    @property
    def airspeed_derivative_filtered(self):
        """Message field 'airspeed_derivative_filtered'."""
        return self._airspeed_derivative_filtered

    @airspeed_derivative_filtered.setter
    def airspeed_derivative_filtered(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'airspeed_derivative_filtered' field must be of type 'float'"
        self._airspeed_derivative_filtered = value

    @property
    def throttle_filtered(self):
        """Message field 'throttle_filtered'."""
        return self._throttle_filtered

    @throttle_filtered.setter
    def throttle_filtered(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'throttle_filtered' field must be of type 'float'"
        self._throttle_filtered = value

    @property
    def pitch_filtered(self):
        """Message field 'pitch_filtered'."""
        return self._pitch_filtered

    @pitch_filtered.setter
    def pitch_filtered(self, value):
        if __debug__:
            assert \
                isinstance(value, float), \
                "The 'pitch_filtered' field must be of type 'float'"
        self._pitch_filtered = value