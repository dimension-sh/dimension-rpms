%global _hardened_build 1

Summary: Another finger daemon for unix capable of fine-tuning your output.
Name: efingerd
Version: 1.6.5
Release: 3%{?dist}
License: GPL
Group: Applications/Internet

Source0: http://kassiopeia.juls.savba.sk/~garabik/software/efingerd/efingerd_1.6.5.tar.gz
Source1: finger.socket
Source2: finger@.service

Patch1: efingerd-makefile.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: glibc-devel, systemd

%description

Allows to customize finger output by executing programs and displaying
their output.

%prep

%setup
%patch1 -p0 -b .makefile

%build
make %{?_smp_mflags}

%install
make PREFIX=%{_prefix} DESTDIR=%{?buildroot} install

mkdir -p %{buildroot}%{_unitdir}
install -m 644 %{SOURCE1} %{buildroot}%{_unitdir}
install -m 644 %{SOURCE2} %{buildroot}%{_unitdir}

%clean
rm -rf %{buildroot}

%post
%systemd_post finger.socket

%preun
%systemd_preun finger.socket

%postun
%systemd_postun_with_restart finger.socket


%files
%config(noreplace) %{_sysconfdir}/efingerd
%{_unitdir}/finger.socket
%{_unitdir}/finger@.service
%attr(0755,root,root) %{_sbindir}/efingerd
%{_mandir}/man8/efingerd.8*

%changelog
* Sun Jun 13 2021 Andrew Williams <andy@tensixtyone.com> 1.6.5-3
- Fix systemd service to point to the correct binary location
* Tue Jul 07 2020 Andrew Williams <andy@tensixtyone.com> 1.6.5-2
- Fix systemd service to ignore Exit 255 errors
* Fri Jul 03 2020 Andrew Williams <andy@tensixtyone.com> 1.6.5-1
- Initial RPM release
