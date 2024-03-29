// Generated by gencpp from file agv_control_msgs/CommStatusRequest.msg
// DO NOT EDIT!


#ifndef AGV_CONTROL_MSGS_MESSAGE_COMMSTATUSREQUEST_H
#define AGV_CONTROL_MSGS_MESSAGE_COMMSTATUSREQUEST_H


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
struct CommStatusRequest_
{
  typedef CommStatusRequest_<ContainerAllocator> Type;

  CommStatusRequest_()
    : action()  {
    }
  CommStatusRequest_(const ContainerAllocator& _alloc)
    : action(_alloc)  {
  (void)_alloc;
    }



   typedef std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other >  _action_type;
  _action_type action;





  typedef boost::shared_ptr< ::agv_control_msgs::CommStatusRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::agv_control_msgs::CommStatusRequest_<ContainerAllocator> const> ConstPtr;

}; // struct CommStatusRequest_

typedef ::agv_control_msgs::CommStatusRequest_<std::allocator<void> > CommStatusRequest;

typedef boost::shared_ptr< ::agv_control_msgs::CommStatusRequest > CommStatusRequestPtr;
typedef boost::shared_ptr< ::agv_control_msgs::CommStatusRequest const> CommStatusRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::agv_control_msgs::CommStatusRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::agv_control_msgs::CommStatusRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}

} // namespace agv_control_msgs

namespace ros
{
namespace message_traits
{



// BOOLTRAITS {'IsFixedSize': False, 'IsMessage': True, 'HasHeader': False}
// {'geometry_msgs': ['/opt/ros/kinetic/share/geometry_msgs/cmake/../msg'], 'std_msgs': ['/opt/ros/kinetic/share/std_msgs/cmake/../msg'], 'agv_control_msgs': ['/home/max/navi_ws/src/agv_control_msgs/msg']}

// !!!!!!!!!!! ['__class__', '__delattr__', '__dict__', '__doc__', '__eq__', '__format__', '__getattribute__', '__hash__', '__init__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', '_parsed_fields', 'constants', 'fields', 'full_name', 'has_header', 'header_present', 'names', 'package', 'parsed_fields', 'short_name', 'text', 'types']




template <class ContainerAllocator>
struct IsFixedSize< ::agv_control_msgs::CommStatusRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::agv_control_msgs::CommStatusRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::agv_control_msgs::CommStatusRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::agv_control_msgs::CommStatusRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::agv_control_msgs::CommStatusRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::agv_control_msgs::CommStatusRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::agv_control_msgs::CommStatusRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "7757aad79fa343e61bc69ed7f1b7666d";
  }

  static const char* value(const ::agv_control_msgs::CommStatusRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x7757aad79fa343e6ULL;
  static const uint64_t static_value2 = 0x1bc69ed7f1b7666dULL;
};

template<class ContainerAllocator>
struct DataType< ::agv_control_msgs::CommStatusRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "agv_control_msgs/CommStatusRequest";
  }

  static const char* value(const ::agv_control_msgs::CommStatusRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::agv_control_msgs::CommStatusRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "string action\n\
";
  }

  static const char* value(const ::agv_control_msgs::CommStatusRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::agv_control_msgs::CommStatusRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.action);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct CommStatusRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::agv_control_msgs::CommStatusRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::agv_control_msgs::CommStatusRequest_<ContainerAllocator>& v)
  {
    s << indent << "action: ";
    Printer<std::basic_string<char, std::char_traits<char>, typename ContainerAllocator::template rebind<char>::other > >::stream(s, indent + "  ", v.action);
  }
};

} // namespace message_operations
} // namespace ros

#endif // AGV_CONTROL_MSGS_MESSAGE_COMMSTATUSREQUEST_H
