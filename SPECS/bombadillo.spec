%global _hardened_build 1

Summary: Bombadillo is a non-web browser for the terminal.
Name: bombadillo
Version: 2.3.3
Release: 1%{?dist}
License: GNU GPL v3
Group: Applications/Internet

Source0: https://tildegit.org/sloum/bombadillo/archive/%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
Bombadillo is a non-web browser for the terminal.

%prep

%setup -n bombadillo

%build
make build

%install
make install DESTDIR=%{buildroot} PREFIX=%{_prefix} MANDIR=%{_mandir}

%clean
rm -rf %{buildroot}

%post

%preun

%postun

%files
%doc README.md
%doc DEVELOPING.md
%license LICENSE
%attr(0755,root,root) %{_bindir}/bombadillo
%{_mandir}/*/*
%{_datarootdir}/*
