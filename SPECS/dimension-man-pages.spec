%global _hardened_build 1

Summary: A collection of manpages for the Dimension community
Name: dimension-man-pages
Version: 1.0
Release: 1%{?dist}
License: GPL
Group: Applications/Internet

Source0: https://github.com/dimension-sh/dimension-rpms.git#/todo-%{version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

%prep

%setup

%build

%install
make PREFIX=%{?buildroot}%{_prefix} install

%clean
rm -rf %{buildroot}

%post

%preun

%postun

%files
%{_mandir}/*

%changelog
* Fri Jul 10 2020 Andrew Williams <andy@tensixtyone.com> 1.0
- Initial RPM package
