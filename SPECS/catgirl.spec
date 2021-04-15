%global _hardened_build 1

Summary: a TLS-only terminal IRC client.
Name: catgirl
Version: 1.7
Release: 1%{?dist}
License: BSD 2-Clause
Group: Applications/Internet

Source0: https://git.causal.agency/catgirl/snapshot/catgirl-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: glibc-devel, ctags, libretls-devel, ncurses-devel

%description

%prep

%setup

%build
./configure
make %{?_smp_mflags} all

%install
DESTDIR=%{buildroot} PREFIX=%{_prefix} make install

%clean
rm -rf %{buildroot}

%post

%preun

%postun

%files
%attr(0755,root,root) %{_bindir}/catgirl
%{_mandir}/man1/catgirl.1*
