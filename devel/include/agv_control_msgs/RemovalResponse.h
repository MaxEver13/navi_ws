// Generated by gencpp from file agv_control_msgs/RemovalResponse.msg
// DO NOT EDIT!


#ifndef AGV_CONTROL_MSGS_MESSAGE_REMOVALRESPONSE_H
#define AGV_CONTROL_MSGS_MESSAGE_REMOVALRESPONSE_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>


namespace agv_control_msgs
{
template <class ContainerAllocator>
struct RemovalResponse_
{
  typedef RemovalResponse_<ContainerAllocator> Type;

  RemovalResponse_()
    : removalStarted(false)  {
    }
  RemovalResponse_(const ContainerAllocator& _alloc)
    : removalStarted(false)  {
  (void)_alloc;
    }



   typedef uint8_t _removalStarted_type;
  _removalStarted_type removalStarted;





  typedef boost::shared_ptr< ::agv_control_msgs::RemovalResponse_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::agv_control_msgs::RemovalResponse_<ContainerAllocator> const> ConstPtr;

}; // struct RemovalResponse_

typedef ::agv_control_msgs::RemovalResponse_<std::allocator<void> > RemovalResponse;

typedef boost::shared_ptr< ::agv_control_msgs::RemovalResponse > RemovalResponsePtr;
typedef boost::shared_ptr< ::agv_control_msgs::RemovalResponse const> RemovalResponseConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::agv_control_msgs::RemovalResponse_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::agv_control_msgs::RemovalResponse_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace agv_control_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': True, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'agv_control_msgs': ['/home/max/navi_ws/src/agv_control_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::agv_control_msgs::RemovalResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::agv_control_msgs::RemovalResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::agv_control_msgs::RemovalResponse_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::agv_control_msgs::RemovalResponse_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::agv_control_msgs::RemovalResponse_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::agv_control_msgs::RemovalResponse_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::agv_control_msgs::RemovalResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "97ca1ed90cb839ea106e5176948bc63c";
  }

  static const char* value(const ::agv_control_msgs::RemovalResponse_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x97ca1ed90cb839eaULL;
  static const uint64_t static_value2 = 0x106e5176948bc63cULL;
};

template<class ContainerAllocator>
struct DataType< ::agv_control_msgs::RemovalResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "agv_control_msgs/RemovalResponse";
  }

  static const char* value(const ::agv_control_msgs::RemovalResponse_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::agv_control_msgs::RemovalResponse_<ContainerAllocator> >
{
  static const char* value()
  {
    return "bool removalStarted\n\
\n\
";
  }

  static const char* value(const ::agv_control_msgs::RemovalResponse_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::agv_control_msgs::RemovalResponse_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.removalStarted);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct RemovalResponse_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::agv_control_msgs::RemovalResponse_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::agv_control_msgs::RemovalResponse_<ContainerAllocator>& v)
  {
    s << indent << "removalStarted: ";
    Printer<uint8_t>::stream(s, indent + "  ", v.removalStarted);
  }
};

} // namespace message_operations
} // namespace ros

#endif // AGV_CONTROL_MSGS_MESSAGE_REMOVALRESPONSE_H
