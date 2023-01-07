%global _hardened_build 1

Summary: a TLS-only terminal IRC client.
Name: catgirl
Version: 2.1
Release: 4%{?dist}
License: BSD 2-Clause
Group: Applications/Internet

Source0: https://git.causal.agency/catgirl/snapshot/catgirl-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: glibc-devel, ctags, libretls-devel, ncurses-devel

Requires: libretls >= 3.5.2
Requires: ncurses-libs

%description

%prep

%setup

%build
./configure
make %{?_smp_mflags} all

%install
DESTDIR=%{buildroot} PREFIX=%{_prefix} MANDIR=%{_mandir} make install

%clean
rm -rf %{buildroot}

%post

%preun

%postun

%files
%attr(0755,root,root) %{_bindir}/catgirl
%{_mandir}/man1/catgirl.1*
