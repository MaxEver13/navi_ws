# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from agv_control_msgs/planData.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import agv_control_msgs.msg
import std_msgs.msg

class planData(genpy.Message):
  _md5sum = "f3df86da21172dbd8bb9f18e14c1164e"
  _type = "agv_control_msgs/planData"
  _has_header = True #flag to mark the presence of a Header object
  _full_text = """Header header

float32[] xp
float32[] yp
float32[] fip
float32[] sp

stringArray[] sectors
bool[] pz_control

gridData grid

================================================================================
MSG: std_msgs/Header
# Standard metadata for higher-level stamped data types.
# This is generally used to communicate timestamped data 
# in a particular coordinate frame.
# 
# sequence ID: consecutively increasing ID 
uint32 seq
#Two-integer timestamp that is expressed as:
# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
# time-handling sugar is provided by the client library
time stamp
#Frame this data is associated with
# 0: no frame
# 1: global frame
string frame_id

================================================================================
MSG: agv_control_msgs/stringArray
string[] data

================================================================================
MSG: agv_control_msgs/gridData
arrayData[] xGrid
arrayData[] yGrid
arrayData[] timeInGrid
arrayData[] timeOutGrid

================================================================================
MSG: agv_control_msgs/arrayData
float32[] data
"""
  __slots__ = ['header','xp','yp','fip','sp','sectors','pz_control','grid']
  _slot_types = ['std_msgs/Header','float32[]','float32[]','float32[]','float32[]','agv_control_msgs/stringArray[]','bool[]','agv_control_msgs/gridData']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       header,xp,yp,fip,sp,sectors,pz_control,grid

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(planData, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.xp is None:
        self.xp = []
      if self.yp is None:
        self.yp = []
      if self.fip is None:
        self.fip = []
      if self.sp is None:
        self.sp = []
      if self.sectors is None:
        self.sectors = []
      if self.pz_control is None:
        self.pz_control = []
      if self.grid is None:
        self.grid = agv_control_msgs.msg.gridData()
    else:
      self.header = std_msgs.msg.Header()
      self.xp = []
      self.yp = []
      self.fip = []
      self.sp = []
      self.sectors = []
      self.pz_control = []
      self.grid = agv_control_msgs.msg.gridData()

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.xp)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.xp))
      length = len(self.yp)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.yp))
      length = len(self.fip)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.fip))
      length = len(self.sp)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(struct.pack(pattern, *self.sp))
      length = len(self.sectors)
      buff.write(_struct_I.pack(length))
      for val1 in self.sectors:
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        for val2 in val1.data:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.pack('<I%ss'%length, length, val2))
      length = len(self.pz_control)
      buff.write(_struct_I.pack(length))
      pattern = '<%sB'%length
      buff.write(struct.pack(pattern, *self.pz_control))
      length = len(self.grid.xGrid)
      buff.write(_struct_I.pack(length))
      for val1 in self.grid.xGrid:
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.pack(pattern, *val1.data))
      length = len(self.grid.yGrid)
      buff.write(_struct_I.pack(length))
      for val1 in self.grid.yGrid:
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.pack(pattern, *val1.data))
      length = len(self.grid.timeInGrid)
      buff.write(_struct_I.pack(length))
      for val1 in self.grid.timeInGrid:
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.pack(pattern, *val1.data))
      length = len(self.grid.timeOutGrid)
      buff.write(_struct_I.pack(length))
      for val1 in self.grid.timeOutGrid:
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(struct.pack(pattern, *val1.data))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.sectors is None:
        self.sectors = None
      if self.grid is None:
        self.grid = agv_control_msgs.msg.gridData()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.xp = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.yp = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.fip = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.sp = struct.unpack(pattern, str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.sectors = []
      for i in range(0, length):
        val1 = agv_control_msgs.msg.stringArray()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.data = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8')
          else:
            val2 = str[start:end]
          val1.data.append(val2)
        self.sectors.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sB'%length
      start = end
      end += struct.calcsize(pattern)
      self.pz_control = struct.unpack(pattern, str[start:end])
      self.pz_control = map(bool, self.pz_control)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grid.xGrid = []
      for i in range(0, length):
        val1 = agv_control_msgs.msg.arrayData()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.data = struct.unpack(pattern, str[start:end])
        self.grid.xGrid.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grid.yGrid = []
      for i in range(0, length):
        val1 = agv_control_msgs.msg.arrayData()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.data = struct.unpack(pattern, str[start:end])
        self.grid.yGrid.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grid.timeInGrid = []
      for i in range(0, length):
        val1 = agv_control_msgs.msg.arrayData()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.data = struct.unpack(pattern, str[start:end])
        self.grid.timeInGrid.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grid.timeOutGrid = []
      for i in range(0, length):
        val1 = agv_control_msgs.msg.arrayData()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.data = struct.unpack(pattern, str[start:end])
        self.grid.timeOutGrid.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_3I().pack(_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs))
      _x = self.header.frame_id
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.pack('<I%ss'%length, length, _x))
      length = len(self.xp)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.xp.tostring())
      length = len(self.yp)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.yp.tostring())
      length = len(self.fip)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.fip.tostring())
      length = len(self.sp)
      buff.write(_struct_I.pack(length))
      pattern = '<%sf'%length
      buff.write(self.sp.tostring())
      length = len(self.sectors)
      buff.write(_struct_I.pack(length))
      for val1 in self.sectors:
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        for val2 in val1.data:
          length = len(val2)
          if python3 or type(val2) == unicode:
            val2 = val2.encode('utf-8')
            length = len(val2)
          buff.write(struct.pack('<I%ss'%length, length, val2))
      length = len(self.pz_control)
      buff.write(_struct_I.pack(length))
      pattern = '<%sB'%length
      buff.write(self.pz_control.tostring())
      length = len(self.grid.xGrid)
      buff.write(_struct_I.pack(length))
      for val1 in self.grid.xGrid:
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.data.tostring())
      length = len(self.grid.yGrid)
      buff.write(_struct_I.pack(length))
      for val1 in self.grid.yGrid:
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.data.tostring())
      length = len(self.grid.timeInGrid)
      buff.write(_struct_I.pack(length))
      for val1 in self.grid.timeInGrid:
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.data.tostring())
      length = len(self.grid.timeOutGrid)
      buff.write(_struct_I.pack(length))
      for val1 in self.grid.timeOutGrid:
        length = len(val1.data)
        buff.write(_struct_I.pack(length))
        pattern = '<%sf'%length
        buff.write(val1.data.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.header is None:
        self.header = std_msgs.msg.Header()
      if self.sectors is None:
        self.sectors = None
      if self.grid is None:
        self.grid = agv_control_msgs.msg.gridData()
      end = 0
      _x = self
      start = end
      end += 12
      (_x.header.seq, _x.header.stamp.secs, _x.header.stamp.nsecs,) = _get_struct_3I().unpack(str[start:end])
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.header.frame_id = str[start:end].decode('utf-8')
      else:
        self.header.frame_id = str[start:end]
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.xp = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.yp = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.fip = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sf'%length
      start = end
      end += struct.calcsize(pattern)
      self.sp = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.sectors = []
      for i in range(0, length):
        val1 = agv_control_msgs.msg.stringArray()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        val1.data = []
        for i in range(0, length):
          start = end
          end += 4
          (length,) = _struct_I.unpack(str[start:end])
          start = end
          end += length
          if python3:
            val2 = str[start:end].decode('utf-8')
          else:
            val2 = str[start:end]
          val1.data.append(val2)
        self.sectors.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      pattern = '<%sB'%length
      start = end
      end += struct.calcsize(pattern)
      self.pz_control = numpy.frombuffer(str[start:end], dtype=numpy.bool, count=length)
      self.pz_control = map(bool, self.pz_control)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grid.xGrid = []
      for i in range(0, length):
        val1 = agv_control_msgs.msg.arrayData()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.data = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.grid.xGrid.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grid.yGrid = []
      for i in range(0, length):
        val1 = agv_control_msgs.msg.arrayData()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.data = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.grid.yGrid.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grid.timeInGrid = []
      for i in range(0, length):
        val1 = agv_control_msgs.msg.arrayData()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.data = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.grid.timeInGrid.append(val1)
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.grid.timeOutGrid = []
      for i in range(0, length):
        val1 = agv_control_msgs.msg.arrayData()
        start = end
        end += 4
        (length,) = _struct_I.unpack(str[start:end])
        pattern = '<%sf'%length
        start = end
        end += struct.calcsize(pattern)
        val1.data = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=length)
        self.grid.timeOutGrid.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_3I = None
def _get_struct_3I():
    global _struct_3I
    if _struct_3I is None:
        _struct_3I = struct.Struct("<3I")
    return _struct_3I
