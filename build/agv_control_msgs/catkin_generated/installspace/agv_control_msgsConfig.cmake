# generated from catkin/cmake/template/pkgConfig.cmake.in

# append elements to a list and remove existing duplicates from the list
# copied from catkin/cmake/list_append_deduplicate.cmake to keep pkgConfig
# self contained
macro(_list_append_deduplicate listname)
  if(NOT "${ARGN}" STREQUAL "")
    if(${listname})
      list(REMOVE_ITEM ${listname} ${ARGN})
    endif()
    list(APPEND ${listname} ${ARGN})
  endif()
endmacro()

# append elements to a list if they are not already in the list
# copied from catkin/cmake/list_append_unique.cmake to keep pkgConfig
# self contained
macro(_list_append_unique listname)
  foreach(_item ${ARGN})
    list(FIND ${listname} ${_item} _index)
    if(_index EQUAL -1)
      list(APPEND ${listname} ${_item})
    endif()
  endforeach()
endmacro()

# pack a list of libraries with optional build configuration keywords
# copied from catkin/cmake/catkin_libraries.cmake to keep pkgConfig
# self contained
macro(_pack_libraries_with_build_configuration VAR)
  set(${VAR} "")
  set(_argn ${ARGN})
  list(LENGTH _argn _count)
  set(_index 0)
  while(${_index} LESS ${_count})
    list(GET _argn ${_index} lib)
    if("${lib}" MATCHES "^(debug|optimized|general)$")
      math(EXPR _index "${_index} + 1")
      if(${_index} EQUAL ${_count})
        message(FATAL_ERROR "_pack_libraries_with_build_configuration() the list of libraries '${ARGN}' ends with '${lib}' which is a build configuration keyword and must be followed by a library")
      endif()
      list(GET _argn ${_index} library)
      list(APPEND ${VAR} "${lib}${CATKIN_BUILD_CONFIGURATION_KEYWORD_SEPARATOR}${library}")
    else()
      list(APPEND ${VAR} "${lib}")
    endif()
    math(EXPR _index "${_index} + 1")
  endwhile()
endmacro()

# unpack a list of libraries with optional build configuration keyword prefixes
# copied from catkin/cmake/catkin_libraries.cmake to keep pkgConfig
# self contained
macro(_unpack_libraries_with_build_configuration VAR)
  set(${VAR} "")
  foreach(lib ${ARGN})
    string(REGEX REPLACE "^(debug|optimized|general)${CATKIN_BUILD_CONFIGURATION_KEYWORD_SEPARATOR}(.+)$" "\\1;\\2" lib "${lib}")
    list(APPEND ${VAR} "${lib}")
  endforeach()
endmacro()


if(agv_control_msgs_CONFIG_INCLUDED)
  return()
endif()
set(agv_control_msgs_CONFIG_INCLUDED TRUE)

# set variables for source/devel/install prefixes
if("FALSE" STREQUAL "TRUE")
  set(agv_control_msgs_SOURCE_PREFIX /home/max/navi_ws/src/agv_control_msgs)
  set(agv_control_msgs_DEVEL_PREFIX /home/max/navi_ws/devel)
  set(agv_control_msgs_INSTALL_PREFIX "")
  set(agv_control_msgs_PREFIX ${agv_control_msgs_DEVEL_PREFIX})
else()
  set(agv_control_msgs_SOURCE_PREFIX "")
  set(agv_control_msgs_DEVEL_PREFIX "")
  set(agv_control_msgs_INSTALL_PREFIX /home/max/navi_ws/install)
  set(agv_control_msgs_PREFIX ${agv_control_msgs_INSTALL_PREFIX})
endif()

# warn when using a deprecated package
if(NOT "" STREQUAL "")
  set(_msg "WARNING: package 'agv_control_msgs' is deprecated")
  # append custom deprecation text if available
  if(NOT "" STREQUAL "TRUE")
    set(_msg "${_msg} ()")
  endif()
  message("${_msg}")
endif()

# flag project as catkin-based to distinguish if a find_package()-ed project is a catkin project
set(agv_control_msgs_FOUND_CATKIN_PROJECT TRUE)

if(NOT "include " STREQUAL " ")
  set(agv_control_msgs_INCLUDE_DIRS "")
  set(_include_dirs "include")
  if(NOT " " STREQUAL " ")
    set(_report "Check the issue tracker '' and consider creating a ticket if the problem has not been reported yet.")
  elseif(NOT " " STREQUAL " ")
    set(_report "Check the website '' for information and consider reporting the problem.")
  else()
    set(_report "Report the problem to the maintainer 'Damjan Miklic <damjan.miklic@fer.hr>' and request to fix the problem.")
  endif()
  foreach(idir ${_include_dirs})
    if(IS_ABSOLUTE ${idir} AND IS_DIRECTORY ${idir})
      set(include ${idir})
    elseif("${idir} " STREQUAL "include ")
      get_filename_component(include "${agv_control_msgs_DIR}/../../../include" ABSOLUTE)
      if(NOT IS_DIRECTORY ${include})
        message(FATAL_ERROR "Project 'agv_control_msgs' specifies '${idir}' as an include dir, which is not found.  It does not exist in '${include}'.  ${_report}")
      endif()
    else()
      message(FATAL_ERROR "Project 'agv_control_msgs' specifies '${idir}' as an include dir, which is not found.  It does neither exist as an absolute directory nor in '/home/max/navi_ws/install/${idir}'.  ${_report}")
    endif()
    _list_append_unique(agv_control_msgs_INCLUDE_DIRS ${include})
  endforeach()
endif()

set(libraries "")
foreach(library ${libraries})
  # keep build configuration keywords, target names and absolute libraries as-is
  if("${library}" MATCHES "^(debug|optimized|general)$")
    list(APPEND agv_control_msgs_LIBRARIES ${library})
  elseif(TARGET ${library})
    list(APPEND agv_control_msgs_LIBRARIES ${library})
  elseif(IS_ABSOLUTE ${library})
    list(APPEND agv_control_msgs_LIBRARIES ${library})
  else()
    set(lib_path "")
    set(lib "${library}-NOTFOUND")
    # since the path where the library is found is returned we have to iterate over the paths manually
    foreach(path /home/max/navi_ws/install/lib;/home/max/navi_ws/devel/lib;/home/max/path_plan_ws/devel/lib;/home/max/workspace/catkin_ws_livom/devel/lib;/home/max/workspace/catkin_ws_sc_lio/devel/lib;/home/max/workspace/catkin_ws_lio/devel/lib;/home/max/workspace/catkin_ws_lins/devel/lib;/home/max/workspace/catkin_ws_ov/devel/lib;/home/max/eskf_ws/devel/lib;/home/max/msckf_ws/devel/lib;/home/max/vins_ws/devel/lib;/home/max/imu_allan_ws/devel/lib;/home/max/kalibr_allan_ws/devel/lib;/home/max/vio_sim_ws/devel/lib;/home/max/catkin_ws/devel/lib;/home/max/kalibr_workspace/devel/lib;/opt/ros/kinetic/lib)
      find_library(lib ${library}
        PATHS ${path}
        NO_DEFAULT_PATH NO_CMAKE_FIND_ROOT_PATH)
      if(lib)
        set(lib_path ${path})
        break()
      endif()
    endforeach()
    if(lib)
      _list_append_unique(agv_control_msgs_LIBRARY_DIRS ${lib_path})
      list(APPEND agv_control_msgs_LIBRARIES ${lib})
    else()
      # as a fall back for non-catkin libraries try to search globally
      find_library(lib ${library})
      if(NOT lib)
        message(FATAL_ERROR "Project '${PROJECT_NAME}' tried to find library '${library}'.  The library is neither a target nor built/installed properly.  Did you compile project 'agv_control_msgs'?  Did you find_package() it before the subdirectory containing its code is included?")
      endif()
      list(APPEND agv_control_msgs_LIBRARIES ${lib})
    endif()
  endif()
endforeach()

set(agv_control_msgs_EXPORTED_TARGETS "agv_control_msgs_generate_messages_cpp;agv_control_msgs_generate_messages_eus;agv_control_msgs_generate_messages_lisp;agv_control_msgs_generate_messages_nodejs;agv_control_msgs_generate_messages_py")
# create dummy targets for exported code generation targets to make life of users easier
foreach(t ${agv_control_msgs_EXPORTED_TARGETS})
  if(NOT TARGET ${t})
    add_custom_target(${t})
  endif()
endforeach()

set(depends "roscpp;std_msgs;geometry_msgs;message_runtime")
foreach(depend ${depends})
  string(REPLACE " " ";" depend_list ${depend})
  # the package name of the dependency must be kept in a unique variable so that it is not overwritten in recursive calls
  list(GET depend_list 0 agv_control_msgs_dep)
  list(LENGTH depend_list count)
  if(${count} EQUAL 1)
    # simple dependencies must only be find_package()-ed once
    if(NOT ${agv_control_msgs_dep}_FOUND)
      find_package(${agv_control_msgs_dep} REQUIRED NO_MODULE)
    endif()
  else()
    # dependencies with components must be find_package()-ed again
    list(REMOVE_AT depend_list 0)
    find_package(${agv_control_msgs_dep} REQUIRED NO_MODULE ${depend_list})
  endif()
  _list_append_unique(agv_control_msgs_INCLUDE_DIRS ${${agv_control_msgs_dep}_INCLUDE_DIRS})

  # merge build configuration keywords with library names to correctly deduplicate
  _pack_libraries_with_build_configuration(agv_control_msgs_LIBRARIES ${agv_control_msgs_LIBRARIES})
  _pack_libraries_with_build_configuration(_libraries ${${agv_control_msgs_dep}_LIBRARIES})
  _list_append_deduplicate(agv_control_msgs_LIBRARIES ${_libraries})
  # undo build configuration keyword merging after deduplication
  _unpack_libraries_with_build_configuration(agv_control_msgs_LIBRARIES ${agv_control_msgs_LIBRARIES})

  _list_append_unique(agv_control_msgs_LIBRARY_DIRS ${${agv_control_msgs_dep}_LIBRARY_DIRS})
  list(APPEND agv_control_msgs_EXPORTED_TARGETS ${${agv_control_msgs_dep}_EXPORTED_TARGETS})
endforeach()

set(pkg_cfg_extras "agv_control_msgs-msg-extras.cmake")
foreach(extra ${pkg_cfg_extras})
  if(NOT IS_ABSOLUTE ${extra})
    set(extra ${agv_control_msgs_DIR}/${extra})
  endif()
  include(${extra})
endforeach()
