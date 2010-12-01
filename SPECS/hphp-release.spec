Name:           hphp-release       
Version:        1.0 
Release:        2%{?dist}
License: GPL
Summary:        HipHop Repository configuration
Group:          System Environment/Base 
URL:            https://github.com/tag1consulting/hphp
Source0:        hphp.repo.el5
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       epel-release
Requires:       ius-release


%description
This package contains the HipHop repository.

%prep
%setup -q  -c -T
install -pm 644 %{SOURCE0} .

%build


%install
rm -rf $RPM_BUILD_ROOT

# yum
install -dm 755 $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

install -pm 644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/hphp.repo

exit 0


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%config(noreplace) /etc/yum.repos.d/*


%changelog
* Wed Dec 01 2010 Rudy Grigar <rudy@tag1consulting.com> - 1.0-2
- fix broken install/postrun and explicit provides

* Thu Nov 18 2010 Rudy Grigar <rudy@tag1consulting.com> - 1.0-1
- create repo config for hphp
