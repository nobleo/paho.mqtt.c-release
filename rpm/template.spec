%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/noetic/.*$
%global __requires_exclude_from ^/opt/ros/noetic/.*$

Name:           ros-noetic-paho-mqtt-c
Version:        1.3.9
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS paho-mqtt-c package

License:        Eclipse Public License 2.0
Source0:        %{name}-%{version}.tar.gz

Requires:       openssl-devel
BuildRequires:  cmake
BuildRequires:  openssl-devel
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}

%description
Eclipse Paho C Client Library for the MQTT Protocol

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/noetic" \
    -DCMAKE_PREFIX_PATH="/opt/ros/noetic" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
%make_install -C obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/noetic/setup.sh" ]; then . "/opt/ros/noetic/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/noetic

%changelog
* Mon Aug 23 2021  <paho-success@eclipse.org> - 1.3.9-1
- Autogenerated by Bloom

* Thu Jun 03 2021  <paho-success@eclipse.org> - 1.3.8-8
- Autogenerated by Bloom

* Wed Jun 02 2021  <paho-success@eclipse.org> - 1.3.8-7
- Autogenerated by Bloom

* Wed Jun 02 2021  <paho-success@eclipse.org> - 1.3.8-6
- Autogenerated by Bloom

* Mon May 31 2021  <paho-success@eclipse.org> - 1.3.8-5
- Autogenerated by Bloom

* Fri May 28 2021  <paho-success@eclipse.org> - 1.3.8-4
- Autogenerated by Bloom

* Mon May 17 2021  <paho-success@eclipse.org> - 1.3.8-3
- Autogenerated by Bloom

* Tue May 11 2021  <paho-success@eclipse.org> - 1.3.8-2
- Autogenerated by Bloom

* Tue May 11 2021  <paho-success@eclipse.org> - 1.3.8-1
- Autogenerated by Bloom

