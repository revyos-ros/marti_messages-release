Name:           ros-kinetic-marti-can-msgs
Version:        0.5.0
Release:        0%{?dist}
Summary:        ROS marti_can_msgs package

Group:          Development/Libraries
License:        BSD
URL:            https://github.com/swri-robotics/marti_messages
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-std-msgs

%description
marti_can_msgs

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Thu Apr 05 2018 Elliot Johnson <elliot.johnson@swri.org> - 0.5.0-0
- Autogenerated by Bloom

* Wed Nov 08 2017 Elliot Johnson <elliot.johnson@swri.org> - 0.4.0-0
- Autogenerated by Bloom

* Thu Sep 28 2017 Elliot Johnson <elliot.johnson@swri.org> - 0.3.0-0
- Autogenerated by Bloom

* Tue Aug 29 2017 Elliot Johnson <elliot.johnson@swri.org> - 0.2.0-0
- Autogenerated by Bloom

* Tue Aug 15 2017 Elliot Johnson <elliot.johnson@swri.org> - 0.1.0-0
- Autogenerated by Bloom

* Mon May 08 2017 Elliot Johnson <elliot.johnson@swri.org> - 0.0.9-0
- Autogenerated by Bloom

* Sat Mar 18 2017 Elliot Johnson <elliot.johnson@swri.org> - 0.0.8-0
- Autogenerated by Bloom

* Mon Feb 06 2017 Elliot Johnson <elliot.johnson@swri.org> - 0.0.7-0
- Autogenerated by Bloom

* Sun Oct 23 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.0.6-0
- Autogenerated by Bloom

* Sat May 21 2016 Elliot Johnson <elliot.johnson@swri.org> - 0.0.4-0
- Autogenerated by Bloom

