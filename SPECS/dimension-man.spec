%global _hardened_build 1

Summary: A collection of manpages for the Dimension community
Name: dimension-man
Version: 1.2
Release: 1%{?dist}
License: GPL
Group: Applications/Internet

Source0: https://github.com/dimension-sh/man/archive/refs/tags/%{version}.tar.gz#/dimension-man-%{version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description

%prep

%setup -n man-%{version}

%build

%install
make DESTDIR=%{?buildroot} PREFIX=%{_prefix} install

%clean
rm -rf %{buildroot}

%post

%preun

%postun

%files
%{_mandir}/*

%changelog
* Sat Apr 10 2021 Andrew Williams <andy@tensixtyone.com> 1.2
- Fix build system
* Sat Apr 10 2021 Andrew Williams <andy@tensixtyone.com> 1.1
- Updated dimension documentation for new apps.
* Fri Jul 10 2020 Andrew Williams <andy@tensixtyone.com> 1.0
- Initial RPM package
