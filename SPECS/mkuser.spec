Name:           mkuser
Version:        1.1.1
Release:        1%{?dist}
Summary:        mkuser is a simple tool to allow for the easy creation of users on a tilde style server.

License:        MIT
URL:            https://github.com/dimension-sh/mkuser
Source0:        https://github.com/dimension-sh/mkuser/archive/%{version}.tar.gz#/mkuser-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel

Requires: python3-pyyaml

%description
mkuser is a simple tool to allow for the easy creation of users on a tilde style server.

%prep
%autosetup -n mkuser-%{version}

%build

%install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/mkuser

install -p -m 755 mkuser ${RPM_BUILD_ROOT}%{_bindir}/mkuser
install -p mkuser.yaml ${RPM_BUILD_ROOT}%{_sysconfdir}/mkuser/mkuser.yaml
install -p mail.tmpl ${RPM_BUILD_ROOT}%{_sysconfdir}/mkuser/mail.tmpl
install -p mkuser.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/mkuser.1 

%files
%license LICENSE
%doc README.md
%{_bindir}/mkuser
%config %{_sysconfdir}/mkuser/*
%{_mandir}/*/*

%changelog
* Sat Jun 12 2021 Andrew Williams <andy@tensixtyone.com> 1.1.1-1
- Initial RPM package
