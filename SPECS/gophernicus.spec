%global _hardened_build 1

Summary: Gophernicus is a modern, full-featured (and hopefully) secure gopher daemon
Name: gophernicus
Version: 3.1.1
Release: 1%{?dist}
License: BSD 2-Clause
Group: Applications/Internet

Source0: https://github.com/gophernicus/gophernicus/releases/download/%{version}/gophernicus-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: glibc-devel, systemd

%description

%prep

%setup

%build
./configure --prefix=/usr --listener=systemd
make %{?_smp_mflags} all

%install
mkdir -p %{buildroot}%{_sbindir}
install -m 755 src/gophernicus %{buildroot}%{_sbindir}

mkdir -p %{buildroot}%{_sysconfdir}/sysconfig
install -m 644 init/gophernicus.env %{buildroot}%{_sysconfdir}/sysconfig/gophernicus

mkdir -p %{buildroot}%{_unitdir}
install -m 644 init/gophernicus@.service %{buildroot}%{_unitdir}
install -m 644 init/gophernicus.socket %{buildroot}%{_unitdir}

mkdir -p %{buildroot}%{_mandir}/man8/
install -m 644 gophernicus.8 %{buildroot}%{_mandir}/man8

mkdir -p %{buildroot}%{_localstatedir}/gopher
install -m 644 gophermap.sample %{buildroot}%{_localstatedir}/gopher

%clean
rm -rf %{buildroot}

%post
%systemd_post gophernicus.socket

%preun
%systemd_preun gophernicus.socket

%postun
%systemd_postun_with_restart gophernicus.socket


%files
%config %{_sysconfdir}/sysconfig/gophernicus
%{_unitdir}/gophernicus@.service
%{_unitdir}/gophernicus.socket
%attr(0755,root,root) %{_sbindir}/gophernicus
%{_mandir}/man8/gophernicus.8.gz
%{_localstatedir}/gopher
