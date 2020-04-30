%define ns_prefix ea
%define pkg_base  oniguruma
%define pkg_name  %{ns_prefix}-%{pkg_base}
%define _prefix   /opt/cpanel/%{pkg_name}
%define _vernum  6.9.5

Summary:   oniguruma is a regular expression library
Name:      %{pkg_name}
Version:   6.9.5_rev1
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4554 for more details
%define release_prefix 1

Release:   %{release_prefix}%{?dist}.cpanel
License:   BSD
Source:    onig-%{_vernum}-rev1.tar.gz
Vendor:    cPanel, Inc.
Group:     System Environment/Libraries
Provides:  oniguruma = %{version}-%{release}

%description
Oniguruma is a modern and flexible regular expressions library. It encompasses features from different regular expression implementations that traditionally exist in different languages.

Character encoding can be specified per regular expression object.

Supported character encodings:

ASCII, UTF-8, UTF-16BE, UTF-16LE, UTF-32BE, UTF-32LE, EUC-JP, EUC-TW, EUC-KR, EUC-CN, Shift_JIS, Big5, GB18030, KOI8-R, CP1251, ISO-8859-1, ISO-8859-2, ISO-8859-3, ISO-8859-4, ISO-8859-5, ISO-8859-6, ISO-8859-7, ISO-8859-8, ISO-8859-9, ISO-8859-10, ISO-8859-11, ISO-8859-13, ISO-8859-14, ISO-8859-15, ISO-8859-16

%package devel
Summary: Development files of the oniguruma regular expression library
Group: Development/Libraries
Provides: oniguruma-devel = %{version}-%{release}
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
/opt/cpanel/ea-oniguruma/bin

%files devel
%dir /opt/cpanel/ea-oniguruma/share
%{_docdir}
%{_libdir}
%dir /opt/cpanel/ea-oniguruma/include
%{_includedir}/oniggnu.h
%{_includedir}/oniguruma.h

%changelog
* Wed Apr 29 2020 Dan Muey <dan@cpanel.net> - 6.9.5_rev1.1
- ZC-6649: Initial RPM for PHP 7.4 use
