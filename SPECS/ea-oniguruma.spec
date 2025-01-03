%define ns_prefix ea
%define pkg_base  oniguruma
%define pkg_name  %{ns_prefix}-%{pkg_base}
%define _prefix   /opt/cpanel/%{pkg_name}
%define _fullvernum %{version}.%{release_prefix}
%define _vernum     %{version}

Summary:   oniguruma is a regular expression library
Name:      %{pkg_name}
Version:   6.9.10
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4554 for more details
%define release_prefix 1

Release:   %{release_prefix}%{?dist}.cpanel
License:   BSD
Source:    onig-%{version}.tar.gz
Vendor:    cPanel, Inc.
Group:     System Environment/Libraries
AutoReqProv: no

%description
Oniguruma is a modern and flexible regular expressions library. It encompasses features from different regular expression implementations that traditionally exist in different languages.

Character encoding can be specified per regular expression object.

Supported character encodings:

ASCII, UTF-8, UTF-16BE, UTF-16LE, UTF-32BE, UTF-32LE, EUC-JP, EUC-TW, EUC-KR, EUC-CN, Shift_JIS, Big5, GB18030, KOI8-R, CP1251, ISO-8859-1, ISO-8859-2, ISO-8859-3, ISO-8859-4, ISO-8859-5, ISO-8859-6, ISO-8859-7, ISO-8859-8, ISO-8859-9, ISO-8859-10, ISO-8859-11, ISO-8859-13, ISO-8859-14, ISO-8859-15, ISO-8859-16

%package devel
Summary: Development files of the oniguruma regular expression library
Group: Development/Libraries
AutoReqProv: no
Requires: ea-oniguruma = %{version}-%{release}

%description devel
Header file and static libraries of the oniguruma regular expression library

%prep
%setup -n onig-%{_vernum}

%build
./configure \
    --prefix=%{_prefix} \
    --libdir=%{_libdir} \
    --disable-dependency-tracking \
    --disable-maintainer-mode

make

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install
find $RPM_BUILD_ROOT -name 'onig-config' -exec rm -rf {} +

mkdir -p ${RPM_BUILD_ROOT}/%{_docdir}
mkdir -p ${RPM_BUILD_ROOT}/opt/cpanel/ea-oniguruma/include
mkdir -p ${RPM_BUILD_ROOT}/opt/cpanel/ea-oniguruma/share

%check
make check

%clean
rm -rf ${RPM_BUILD_ROOT}

%post
ldconfig

%postun
ldconfig

%files
%dir /opt/cpanel/ea-oniguruma
%dir /opt/cpanel/ea-oniguruma/bin

%files devel
%dir /opt/cpanel/ea-oniguruma/share
%{_docdir}
%{_libdir}
%dir /opt/cpanel/ea-oniguruma/include
%{_includedir}/oniggnu.h
%{_includedir}/oniguruma.h

%changelog
* Tue Dec 31 2024 Cory McIntire <cory@cpanel.net> - 6.9.10-1
- EA-12622: Update ea-oniguruma from v6.9.9 to v6.9.10

* Mon Aug 26 2024 Cory McIntire <cory@cpanel.net> - 6.9.9-2
- EA-12204: Prevent objects from being advertised to non-cPanel binaries

* Mon Oct 16 2023 Cory McIntire <cory@cpanel.net> - 6.9.9-1
- EA-11748: Update ea-oniguruma from v6.9.8 to v6.9.9

* Mon May 02 2022 Cory McIntire <cory@cpanel.net> - 6.9.8-1
- EA-10674: Update ea-oniguruma from v6.9.7.1 to v6.9.8

* Fri Apr 23 2021 Cory McIntire <cory@cpanel.net> - 6.9.7.1-1
- EA-9708: Update ea-oniguruma from v6.9.6 to v6.9.7.1

* Mon Dec 07 2020 Cory McIntire <cory@cpanel.net> - 6.9.6-1
- EA-9466: Update ea-oniguruma from v6.9.5_rev1 to v6.9.6

* Wed Apr 29 2020 Dan Muey <dan@cpanel.net> - 6.9.5_rev1.1
- ZC-6649: Initial RPM for PHP 7.4 use
