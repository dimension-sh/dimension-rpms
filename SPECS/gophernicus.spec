%global _hardened_build 1

Summary: Gophernicus is a modern, full-featured (and hopefully) secure gopher daemon
Name: gophernicus
Version: 3.1.1
Release: 3%{?dist}
License: BSD 2-Clause
Group: Applications/Internet

Source0: https://github.com/gophernicus/gophernicus/releases/download/%{version}/gophernicus-%{version}.tar.gz

Patch1: gophernicus-packaging.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: glibc-devel, systemd, gcc

%description

%prep

%setup
%patch1

%build
./configure --prefix=/usr --listener=systemd --systemd=%{_unitdir}
make %{?_smp_mflags} all

%install
DESTDIR=%{buildroot} make install

%clean
rm -rf %{buildroot}

%post
%systemd_post gophernicus.socket

%preun
%systemd_preun gophernicus.socket

%postun
%systemd_postun_with_restart gophernicus.socket

%files
%config %{_sysconfdir}/default/gophernicus
%config %{_sysconfdir}/sysconfig/gophernicus
%{_unitdir}/gophernicus@.service
%{_unitdir}/gophernicus.socket
%attr(0755,root,root) %{_sbindir}/gophernicus
%{_mandir}/man8/gophernicus.8.gz
%config %{_localstatedir}/gopher
