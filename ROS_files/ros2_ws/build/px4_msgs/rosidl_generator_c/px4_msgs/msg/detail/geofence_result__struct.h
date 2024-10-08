// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from px4_msgs:msg/GeofenceResult.idl
// generated code does not contain a copyright notice

#ifndef PX4_MSGS__MSG__DETAIL__GEOFENCE_RESULT__STRUCT_H_
#define PX4_MSGS__MSG__DETAIL__GEOFENCE_RESULT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'GF_ACTION_NONE'.
enum
{
  px4_msgs__msg__GeofenceResult__GF_ACTION_NONE = 0
};

/// Constant 'GF_ACTION_WARN'.
enum
{
  px4_msgs__msg__GeofenceResult__GF_ACTION_WARN = 1
};

/// Constant 'GF_ACTION_LOITER'.
enum
{
  px4_msgs__msg__GeofenceResult__GF_ACTION_LOITER = 2
};

/// Constant 'GF_ACTION_RTL'.
enum
{
  px4_msgs__msg__GeofenceResult__GF_ACTION_RTL = 3
};

/// Constant 'GF_ACTION_TERMINATE'.
enum
{
  px4_msgs__msg__GeofenceResult__GF_ACTION_TERMINATE = 4
};

/// Constant 'GF_ACTION_LAND'.
enum
{
  px4_msgs__msg__GeofenceResult__GF_ACTION_LAND = 5
};

// Struct defined in msg/GeofenceResult in the package px4_msgs.
typedef struct px4_msgs__msg__GeofenceResult
{
  uint64_t timestamp;
  bool geofence_max_dist_triggered;
  bool geofence_max_alt_triggered;
  bool geofence_custom_fence_triggered;
  uint8_t geofence_action;
} px4_msgs__msg__GeofenceResult;

// Struct for a sequence of px4_msgs__msg__GeofenceResult.
typedef struct px4_msgs__msg__GeofenceResult__Sequence
{
  px4_msgs__msg__GeofenceResult * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} px4_msgs__msg__GeofenceResult__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // PX4_MSGS__MSG__DETAIL__GEOFENCE_RESULT__STRUCT_H_
