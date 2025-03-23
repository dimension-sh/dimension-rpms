Name:           mkuser
Version:        2.1.0
Release:        1%{?dist}
Summary:        mkuser is a simple tool to allow for the easy creation of users on a tilde style server.

License:        MIT
URL:            https://github.com/dimension-sh/mkuser
Source0:        https://github.com/dimension-sh/mkuser/archive/%{version}.tar.gz#/mkuser-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros

Requires:       python3-pyyaml

%description
mkuser is a simple tool to allow for the easy creation of users on a tilde style server.

%prep
%autosetup -n mkuser-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
mkdir -p ${RPM_BUILD_ROOT}%{_bindir}
mkdir -p ${RPM_BUILD_ROOT}%{_mandir}/man1
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/mkuser
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/mkuser/pre.d
mkdir -p ${RPM_BUILD_ROOT}%{_sysconfdir}/mkuser/post.d

install -p mkuser.yaml ${RPM_BUILD_ROOT}%{_sysconfdir}/mkuser/mkuser.yaml
install -p mail.tmpl ${RPM_BUILD_ROOT}%{_sysconfdir}/mkuser/mail.tmpl
install -p mkuser.1 ${RPM_BUILD_ROOT}%{_mandir}/man1/mkuser.1 

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/mkuser/*
%{_bindir}/mkuser
%{_mandir}/*/*
%{python3_sitelib}/*

%changelog
* Mon Apr 1 2024 Andrew Williams <andy@tensixtyone.com> 2.1.0-1
- Updated to v2.1.0
* Sat Nov 20 2021 Andrew Williams <andy@tensixtyone.com> 2.0.0-1
- Updated to v2.0.0
* Wed Jul 14 2021 Andrew Williams <andy@tensixtyone.com> 1.2.1-1
- Updated to v1.2.1
* Tue Jun 22 2021 Andrew Williams <andy@tensixtyone.com> 1.2.0-1
- Updated to v1.2.0
* Sun Jun 13 2021 Andrew Williams <andy@tensixtyone.com> 1.1.1-2
- Fixed package so it doesn't overwrite config files
* Sat Jun 12 2021 Andrew Williams <andy@tensixtyone.com> 1.1.1-1
- Initial RPM package
