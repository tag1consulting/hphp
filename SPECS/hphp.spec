Name: hiphop-php
Summary: HipHop PHP for CentOS 5 64bit
Version: 1.0
Release: 2%{?dist}
License: GPL
Group: Development/Compilers
Source: %{name}.tar.gz
BuildRequires: gcc44,gcc44-c++,cmake,perl,flex,bison
BuildRequires: binutils,binutils-devel
BuildRequires: mysql51-devel
BuildRequires: memcached-devel,libmemcached-devel
BuildRequires: icu >= 4.2
BuildRequires: libicu >= 4.2
BuildRequires: libicu-devel >= 4.2
BuildRequires: libcap-devel
BuildRequires: re2c >= 0.13.0
BuildRequires: boost-devel >= 1.37.0
BuildRequires: curl-devel >= 7.20
BuildRequires: expat-devel
BuildRequires: gd-devel
BuildRequires: libevent-devel >= 1.4.13
BuildRequires: libmcrypt-devel
BuildRequires: libxml2-devel
BuildRequires: oniguruma-devel
BuildRequires: openssl-devel
BuildRequires: pcre-devel
BuildRequires: tbb-devel >= 2.2
BuildRequires: zlib-devel
BuildRequires: bzip2-devel
BuildRequires: openldap-devel
BuildRequires: readline-devel
BuildRequires: ncurses-devel
BuildRequires: libc-client-devel
BuildRoot: %{_tmppath}/build-root-%{name}
BuildArch: x86_64
Requires: gcc44,gcc44-c++,make,cmake
Requires: mysql51
Requires: mysql51-devel
Requires: memcached,libmemcached
Requires: boost >= 1.39.0
Requires: boost-devel >= 1.39.0
Requires: curl >= 7.20
Requires: expat
Requires: gd
Requires: gd-devel
Requires: libevent >= 1.4.13
Requires: icu >= 4.2
Requires: libicu >= 4.2
Requires: libicu-devel >= 4.2
Requires: libcap
Requires: libcap-devel
Requires: libmcrypt
Requires: libmcrypt-devel
Requires: oniguruma >= 5.9.2
Requires: oniguruma-devel >= 5.9.2
Requires: openssl
Requires: openssl-devel
Requires: pcre
Requires: tbb
Requires: tbb-devel
Requires: zlib
Requires: bzip2
Requires: bzip2-devel
Requires: readline
Requires: readline-devel
Requires: ncurses
Requires: ncurses-devel
Requires: php52,php52-cli,php52-common
Requires: php52-gd,php52-mysql,php52-pecl-memcache
Requires: readline-devel
Requires: libc-client-devel
Requires: libmemcached-devel
Requires: binutils-devel
Url: http://tag1consulting.com


%description
HipHop is a source code transformer which transforms PHP source code
into highly optimized C++ and then compiles it using g++.

%prep

%setup -q -n %{name}

%build
export HPHP_HOME=`pwd`
export HPHP_LIB=`pwd`/bin
export CC=/usr/bin/gcc44
export CXX=/usr/bin/g++44
cmake .
make
perl -p -i -e 's/\/usr\/local\/bin\/php/\/usr\/bin\/php/g' bin/crutch.php

%install
ls > filelist
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/hphp
mv `cat filelist` $RPM_BUILD_ROOT/%{_libdir}/hphp/

%post
echo "export HPHP_HOME=/usr/lib64/hphp" > /etc/profile.d/hphp.sh
echo "export HPHP_LIB=/usr/lib64/hphp/bin" >> /etc/profile.d/hphp.sh
echo "export CC=/usr/bin/gcc44" >> /etc/profile.d/hphp.sh
echo "export CXX=/usr/bin/g++44" >> /etc/profile.d/hphp.sh

chmod +x /etc/profile.d/hphp.sh

export HPHP_HOME=/usr/lib64/hphp
export HPHP_LIB=/usr/lib64/hphp/bin
export CC=/usr/bin/gcc44
export CXX=/usr/bin/g++44

ln -sf /usr/lib64/hphp/src/hphp/hphp /usr/bin/hphp
ln -sf /usr/lib64/hphp/src/hphpi/hphpi /usr/bin/hphpi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/hphp/*

%changelog
* Thu Nov 18 2010 Rudy Grigar <rudy@tag1consulting.com> 1.0-2
- Next version, add -f to symlink command

* Mon Oct 25 2010 Rudy Grigar <rudy@tag1consulting.com> 1.0-1
- Next version, clean up for ius deps
- Force use of the gcc44

* Sat Feb 27 2010 Andrey Rogovsky <a.rogovsky@gmail.com> 2
- Next version
  HPHP_HOME moved to /usr/lib64/hphp, export HPHP_LOME and HPHP_LIB
  Binary files symlinked to HPHP_HOME
  Add Req. php52, becouse curl was updated and replace system

* Tue Feb 23 2010 Andrey Rogovsky <a.rogovsky@gmail.com> 1
- First version of the HipHop-PHP

