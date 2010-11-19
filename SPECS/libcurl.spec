Name: libcurl
Version: 7.15.5
Release: 1%{?dist}
Summary: Backport of curl libraries
License: MIT
Group: Applications/Internet
Source: http://curl.haxx.se/download/%{name}-%{version}.tar.bz2
Patch0: curl-7.14.1-nousr.patch
Patch1: curl-7.15.0-curl_config-version.patch
Patch2: curl-7.15.3-multilib.patch
Patch3: curl-7.15.5-CVE-2009-0037.patch
Patch4: curl-7.15.5-CVE-2009-2417.patch
Patch5: curl-7.15.5-bz473128.patch
Patch6: curl-7.15.5-bz479967.patch
Patch7: curl-7.15.5-bz517084.patch
Patch8: curl-7.15.5-bz517199.patch
Patch9: curl-7.15.5-bz532069.patch
Patch10: curl-7.15.5-bz563220.patch
URL: http://curl.haxx.se/
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: openssl-devel, libtool, pkgconfig, libidn-devel, autoconf
Requires: openssl
Provides: libcurl.so.3

%description
cURL is a tool for getting files from FTP, HTTP, Gopher, Telnet, and
Dict servers, using any of the supported protocols. cURL is designed
to work without user interaction or any kind of interactivity. cURL
offers many useful capabilities, like proxy support, user
authentication, FTP upload, HTTP post, and file transfer resume.

%package devel
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}, openssl-devel, libidn-devel
Summary: Files needed for building applications with libcurl.

%description devel
cURL is a tool for getting files from FTP, HTTP, Gopher, Telnet, and
Dict servers, using any of the supported protocols. The curl-devel
package includes files needed for developing applications which can
use cURL's capabilities internally.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q 
%patch0 -p1 -b .nousr
%patch1 -p1 -b .ver
%patch2 -p1 -b .multilib
%patch3 -p1 -b .CVE-2009-0037
%patch4 -p1 -b .CVE-2009-2417
%patch5 -p1 -b .bz473128
%patch6 -p1 -b .bz479967
%patch7 -p1 -b .bz517084
%patch8 -p1 -b .bz517199
%patch9 -p1 -b .bz532069
%patch10 -p1 -b .bz563220

%build
aclocal
libtoolize --force
./reconf

if pkg-config openssl ; then
	CPPFLAGS=`pkg-config --cflags openssl`; export CPPFLAGS
	LDFLAGS=`pkg-config --libs openssl`; export LDFLAGS
fi
%configure --with-ssl=/usr --enable-ipv6 \
       --with-ca-bundle=%{_sysconfdir}/pki/tls/certs/ca-bundle.crt \
       --with-gssapi=/usr/kerberos --with-libidn
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libcurl.la
find ${RPM_BUILD_ROOT} -type f ! -name '*.so*' -exec rm -f '{}' \;
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libcurl.so


# don't need curl's copy of the certs; use openssl's
find ${RPM_BUILD_ROOT} -name ca-bundle.crt -exec rm -f '{}' \;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%defattr(-,root,root)
%{_libdir}/libcurl.so.*

%changelog
* Tue Nov 16 2010 Rudy Grigar <rudy@tag1consulting.com> - 7.15.5
- backport for compatability with curl 7.20

