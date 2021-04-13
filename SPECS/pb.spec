%global _hardened_build 1

Summary: A helper utility for using 0x0 pastebin services
Name: pb
Version: 2020.10.27
Release: 1%{?dist}
License: GPL
Group: Applications/Internet

Source0: https://github.com/jamestomasino/pb/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
pb provides an easy-to-use interface for uploading images or piping output to a 0x0 pastebin service. While it comes pre-configured with a specific pastebin, the service endpoint can be overridden.

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
%attr(0755,root,root) %{_bindir}/pb
%{_mandir}/man1/pb.1*

%changelog
* Tue Apr 13 2021 Andrew Williams <andy@tensixtyone.com> 2020.10.27-1
- Initial RPM package
